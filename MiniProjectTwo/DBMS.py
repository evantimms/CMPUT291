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

    def runDateQuery(self, date, operator):
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
            
            if append : res.add(row_id)

            curr = self.dates_cursor.next()
        
        self._addToMasterIds(res)


    def runEmailQuery(self, field, email_address):
        """
        Runs an email query and intersets the results with the master ids
        """
        email = str(email_address)
        curr = self.emails_cursor.first()
        res = set()
        while curr:
            row_id = int(curr[1].decode())
            append = (field == "from" and email) \
                or (field == "to" and email) \
                or (field == "cc" and email) \
                or (field == "bcc" and email)
            
            if append : res.add(row_id)

            curr = self.emails_cursor.next()


        self._addToMasterIds(res)

    def runTermQuery(self, field, term):
        """
        Runs a term query and intersets the results with the master ids
        """
        # TODO: Check if the term has a % at the end - if it does, you need to expand the search
        # Its simpler to check it here than to catch it with regex
        term = str(term)
        curr = self.terms_cursor.first()
        res = set()
        while curr:
            row_id = int(curr[1].decode())
            append = (field == "subj" and term) \
                or (field == "body" and term) \
                or (field == "" and term)
            
            if append : res.add(row_id)

            curr = self.dates_cursor.next()

        if term.endswith("%"):
            root_term = term[:-1]
            query_terms = list((key.decode("utf-8").lower() for key, val in self.terms.items()))
        else:
            query_terms = [query_terms.lower()]

        self._addToMasterIds(res)

    def getResults(self, full_output = False):
        """
        Prints all the results from the records database that correspond to id's mast_ids 
        """
        if not len(self.master_ids):
            print("No results for this query.")

        for key in self.master_ids:
            rec = self.recs_DB.get(str(key).encode())
            if full_output:
                print(rec)
            else:
                title = re.search("<subj>(.*)</subj>", str(rec)).group(1)
                print(key, title)
    
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

# Tests

# Date Query
# dbms = DBMS()
# dbms.runDateQuery("2000/10/02", ":")
# dbms.getResults(True)
# dbms.resetQuery()
# dbms.runDateQuery("2000/10/02", ">")
# dbms.getResults(True)
# dbms.resetQuery()
# dbms.runDateQuery("2000/10/02", "<")
# dbms.getResults(False)
# dbms.resetQuery()
# dbms.runDateQuery("2000/10/02", ">=")
# dbms.getResults(False)
# dbms.resetQuery()
# dbms.runDateQuery("2000/10/02", "<=")
# dbms.getResults(True)
# dbms.resetQuery()
