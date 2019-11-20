import sqlite3
import datetime

class DBApi():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.pkCntr = 1 # TODO: Primary key counter, could add another param to execute query 
        # to check if its an insert, and if so get the primary key from this counter

    def loadData(self):
        f = open("CreateTables.sql", "r").read()
        self.c.executescript(f)
        f = open("AddBasicData.sql", "r").read()
        self.c.executescript(f)

    def getTableSize(self,table):
        self.c.execute("SELECT * FROM ?", (table,))
        return len(self.c.fetchall())

    def getPerson(self, fname, lname):
        """
        Get a person from the data base
        # TODO: Move to DBApi class
        """
        self.c.execute(
            "SELECT * FROM persons WHERE fname = ? AND lname = ?",
            (fname, lname)
        )
        return self.c.fetchone()

    def createPerson(self, fname, lname):
        """
        Create a new person in the persons table
        """
        bdate = input("Enter birthday: ")
        # Possible Error checking?
        try:
            year, month, day = bdate.split('-')
            datetime.datetime(int(year), int(month), int(day))
            bdate = year + '-' + month + '-' + day
        except ValueError:
            print("Invalid Date")
        
        bplace = input("Enter birth place: ")
        address = input("Enter adress: ")
        phone = input("Enter phone: ")

        self.c.execute(
            """
            INSERT INTO persons (fname,lname,bdate,bplace,address,phone) 
            VALUES (?,?,?,?,?,?)
            """,
            (fname,
             lname,
             bdate,
             bplace,
             address,
             phone
            )
        )

    def getUser(self, uid, pwd):
        self.c.execute(
            "SELECT * FROM users WHERE uid = ? AND pwd = ?",
            (uid, pwd)
        )
        return self.c.fetchone()

    # Change function calls to a dictionary like such
    """
    {
        values: set of tuples for c.execute,
        commit: boolean, wether to commit the changes to the db in case of update or delete
        incrementPk: (boolean, primarykey name) if true, set the primary key to the counter
        and incremenent the counter
    }
    """
    def executeQuery(self, query, params = (), commit = True):
        data = self.c.execute(query, params).fetchall()
        if commit:
            self.conn.commit()

        return None if len(data) == 0 else (data[0] if len(data) == 1 else data)
