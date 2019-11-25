from bsddb3 import db
from datetime import datetime
import re

class DBMS:
    def __init__(self):
        self.terms_DB = db.DB()
        self.dates_DB = db.DB()
        self.emails_DB = db.DB()
        self.recs_DB = db.DB()
        self.terms_DB.open('te.idx', None, db.DB_BTREE, db.DB_RDONLY)
        self.emails_DB.open('em.idx', None, db.DB_BTREE, db.DB_RDONLY)
        self.dates_DB.open('da.idx', None, db.DB_BTREE, db.DB_RDONLY)
        self.recs_DB.open('re.idx', None, db.DB_HASH, db.DB_RDONLY)
        self.terms_cursor = self.terms_DB.cursor()
        self.dates_cursor = self.dates_DB.cursor()
        self.emails_cursor = self.emails_DB.cursor()
        self.recs_cursor = self.recs_DB.cursor()

        self.master_ids = None
        self.query_count = 0

    def runDateQuery(self, operator, date):
        """
        Runs a date query and intersets the results with the master ids
        """
        date = datetime.strptime(date, "%Y/%m/%d")
        curr = self.dates_cursor.first()
        res = set()
        while curr:
            curr_date = datetime.strptime(curr[0].decode(), "%Y/%m/%d")
            row_id = int(curr[1].decode())
            append = (operator == ":" and date == curr_date) \
                     or (operator == ">" and curr_date > date) \
                     or (operator == "<" and curr_date < date) \
                     or (operator == ">=" and curr_date >= date) \
                     or (operator == "<=" and curr_date <= date)

            if append: res.add(row_id)

            curr = self.dates_cursor.next()

        self._addToMasterIds(res)

    def runEmailQuery(self, field, email_address):
        """
        Runs an email query and intersets the results with the master ids
        """
        curr = self.emails_cursor.first()
        res = set()
        while curr:
            row_id = int(curr[1].decode())
            row_field = re.search(r'((?:to)|(?:from)|(?:cc)|(?:bcc))-', curr[0].decode()).group(1)
            row_email = re.search(r'(?:(?:to)|(?:from)|(?:cc)|(?:bcc))-(.*)', curr[0].decode()).group(1)

            # Add row if conditionals match
            terms_match = (re.fullmatch(row_email, email_address) is not None)
            if row_field == field and terms_match:
                res.add(row_id)

            curr = self.emails_cursor.next()

        self._addToMasterIds(res)


    def runTermQuery(self, field, term):
        """
        Runs a term query and intersets the results with the master ids
        """
        # curr[0] = {b,s}-term, curr[1] =  rowid
        curr = self.terms_cursor.first()
        res = set()
        while curr:
            # Get the values from the DB
            row_id = int(curr[1].decode())
            row_field = ('body' if curr[0].decode()[0] == 'b' else 'subj')
            row_term = re.search(r'[bs]-(.*)', curr[0].decode()).group(1)

            # Do partial or full match
            if term.endswith("%"):
                terms_match = (re.match(term[:-1], row_term) is not None)
            else:
                terms_match = (re.fullmatch(term, row_term) is not None)

            # Add row if conditionals match
            if not field and terms_match:
                res.add(row_id)
            elif row_field == field and terms_match:
                res.add(row_id)

            curr = self.terms_cursor.next()

        self._addToMasterIds(res)

    def getResults(self, full_output = False):
        """
        Prints all the results from the records database that correspond to id's mast_ids
        """
        print("-----------------")
        for key in self.master_ids:
            rec = self.recs_DB.get(str(key).encode())
            if full_output:
                print(rec)
            else:
                title = re.search("<subj>(.*)</subj>", str(rec)).group(1)
                print(key, title)

        print("End of results.")
        print("-----------------")

    def resetQuery(self):
        """
        Resets the master ids to prepare for a new query
        """
        self.master_ids = set()
        self.query_count = 0

    def _addToMasterIds(self, res):
        """
        Intersects a set of ids to the master copy held in mem.
        """
        if not self.query_count:
            self.master_ids = res
        else:
            self.master_ids = self.master_ids.intersection(res)
        self.query_count += 1