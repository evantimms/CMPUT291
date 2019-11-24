from bsddb3 import db

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

        self.master_ids = set() # set which holds all of the ids

    def runDateQuery(self, date, operator):
        """
        Runs a date query and intersets the results with the master ids
        """

    def runEmailQuery(self):
        """
        Runs an email query and intersets the results with the master ids
        """

    def runTermQuery(self):
        """
        Runs a term query and intersets the results with the master ids
        """

    def getResults(self):
        """
        Prints all the results from the records database that correspond to id's mast_ids
        """
    
    def resetQuery(self):
        """
        Resets the master ids to prepare for a new query
        """
        self.master_ids = set()
