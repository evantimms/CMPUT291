from bsddb3 import db
from datetime import datetime

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


    def runEmailQuery(self, emailPrefix, firstTerm, secondTerm):
        """
        Runs an email query and intersets the results with the master ids
        """
        res = set()


        self._addToMasterIds(res)

    def runTermQuery(self, prefix, term, suffix):
        """
        Runs a term query and intersets the results with the master ids
        """

    def getResults(self):
        """
        Prints all the results from the records database that correspond to id's mast_ids
        """
        for rec_id in self.master_ids:
            pass
    
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
        print(self.master_ids)
        self.query_count += 1


# Tests
# dbms = DBMS()
# dbms.runDateQuery("2000/10/02", ":")
# dbms.resetQuery()
# dbms.runDateQuery("2000/10/02", ">")
# dbms.resetQuery()
# dbms.runDateQuery("2000/10/02", "<")
# dbms.resetQuery()
# dbms.runDateQuery("2000/10/02", ">=")
# dbms.resetQuery()
# dbms.runDateQuery("2000/10/02", "<=")
# dbms.resetQuery()