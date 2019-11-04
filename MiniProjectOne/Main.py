import sqlite3
import math
import datetime
from getpass import getpass
from random import seed
from random import randint
from DBApi import DBApi
# seed random number generator
seed(1)

ROLES = {
    "a": [".quit", ".help", ".logout", ".register", ".renew", ".process", ".getAbstract"],
    "o": [".quit", ".help", ".logout", ".issue", ".findOwner"]
}

HELP_COMMANDS = {
    ".logout": "Log current user out",
    ".register": "Register a marriage or a birth [ -b fname lname [m | f] birthdate birthplace m_fname m_lname f_fname f_lname] | -m p1fname p1lname p2fname p2lname ]",
    ".renew": "Renew a vechicle registration [ regno ]",
    ".process": "Process a bile of sale or a payment [ -s vin cFname, cLname, nFname, nLname, plate# | -p tck# amount]",
    ".getAbstract": "Get a drivers abstract",
    ".issue": "Issue a ticket",
    ".findOwner": "Find the owner of a vehicle"
}

dt = datetime.datetime

class Main():
    def __init__(self, db_name):
        self.user = None
        self.userRole = None
        self.functions = None
        self.quitProgram = False
        self.api = DBApi(db_name)

    def setup(self):
        """
        Load and intialize data and databases
        """
        self.api.loadData()
        

    def execute(self, userIn):
        """
        Exectute a user instruction. Format should be COMMAND [ARGUEMENTS]
        """
        args = userIn.split()[1:]
        cmd = userIn.split()[0]
        if not self.user:
            raise Exception("User not logged in! Killing program")
        elif cmd not in self.functions.keys():
            print("Invalid command")
        else:
            # process input
            try:
                if len(args) > 0:
                    self.functions[cmd](args)
                else:
                    self.functions[cmd]()
            except Exception as e:
                print(str(e))
    
    def help(self):
        """
        Print a list of commands for the avaliable user
        """
        for cmd in HELP_COMMANDS:
            if cmd in self.functions:
                print("{} -> {}".format(cmd, HELP_COMMANDS[cmd]))


    def login(self, uid, pwd):
        """
        Log in a user
        """
        user = self.api.getUser(uid, pwd)
        if user:
            print("Logging in...")

            # assign user object and role
            self.user = user
            self.userRole = user[2]

            # build set of avaible functions based on user roles
            self.functions = { x: getattr(self, x[1:]) for x in ROLES[self.userRole]}

        else:
            raise Exception("Invalid user id or password!")

    def logout(self):
        """
        Log out current user
        """
        print("Logging out...")
        self.user = self.userRole = self.functions = None

    def register(self, args):
        """
        Register an object, either a marriage or a birth
        """
        if args[0] == "-b" and len(args) == 10:
            fname = args[1]
            lname = args[2]
            gender = args[3]
            bdate = args[4]
            bplace = args[5]
            mFname = args[6] 
            mLname = args[7]
            fFname = args[8]
            fLname = args[9]

            regno = randint(0,999999)
            regdate = str(dt.now())
            regplace = self.user[5] # TODO: Make a user class so we dont have to directly access a tuple
            mother = self.api.getPerson(mFname, mLname)
            father = self.api.getPerson(fFname, fLname)
            if not mother:
                # get information about the mother from the user
                print("No entry for mother. Please enter the following information")
                # enter into persons db
                self.api.createPerson(mFname, mLname)
            if not father:
                # get information about the mother from the user
                print("No entry for father. Please enter the following information")
                # enter into persons db
                self.api.createPerson(fFname, fLname)

            # enter new person into births and persons
            if not self.api.getPerson(fname, lname):

                # enter Mom's phone and address for the newborn
                values = self.api.executeQuery(
                    "SELECT address, phone FROM persons WHERE fname = ? AND lname = ?",
                    (mFname, mLname)
                )

                self.api.executeQuery(
                    """
                    INSERT INTO persons (fname, lname, bdate, bplace, address, phone)
                    VALUES (?,?,?,?,?,?)
                    """,
                    (fname, lname, bdate, bplace, values[0], values[1]) 
                )

                self.api.executeQuery(
                    """
                    INSERT INTO births (regno, fname, lname, regdate, regplace, gender, f_fname, f_lname, m_fname, m_lname)
                    VALUES (?,?,?,?,?,?,?,?,?,?)
                    """,
                    (   
                        regno,
                        fname,
                        lname,
                        regdate,
                        regplace,
                        gender,
                        fFname,
                        fLname,
                        mFname,
                        mLname
                    )
                )
                print("added new birth to database")

        elif args[0] == "-m" and len(args) == 5:
            p1Fname = args[1]
            p1Lname = args[2]
            p2Fname = args[3]
            p2Lname = args[4]
            regno = randint(0,999999)
            regdate = dt.now()
            regplace = self.user[5]
            p1 = self.api.getPerson(p1Fname, p1Lname)
            p2 = self.api.getPerson(p2Fname, p2Lname)
            if not p1:
                # get p1 from user
                print("Cannot find partner 1")
                self.api.getPerson(p1Fname, p1Lname)
            if not p2:
                # get p2 from user
                print("Cannot find partner 2")
                self.api.getPerson(p2Fname, p2Lname)

            # enter marriage
            self.api.executeQuery(
                """
                INSERT INTO marriages (regdate, regplace, p1_fname, p1_lname, p2_fname, p2_lname) 
                VALUES (?,?,?,?,?,?)
                """,
                (   
                    regdate,
                    regplace,
                    p1Fname,
                    p1Lname,
                    p2Fname,
                    p2Lname
                )
            )
            print("added new marriage to database")
        else:
            raise Exception("Missing Argument(s)")
    
    def renew(self, args):
        """
        Renew an object
        """
        if len(args) == 1:
            regno = args[0]
            # get the registration from the db
            registration = self.api.executeQuery(
                "SELECT * FROM registrations WHERE regno = ?",
                (regno,)
            )
            if registration:
                currentExpiry = dt.strptime(registration[2], "%Y-%m-%d") # TODO: Parse Correctly
                newExpiry = currentExpiry + datetime.timedelta(days=(365))

                if currentExpiry <= dt.now():
                    newExpiry = dt.now() + datetime.timedelta(days=(365))

                self.api.executeQuery(
                    "UPDATE registrations SET expiry = ? WHERE regno = ?",
                    (newExpiry, regno),
                    True
                )
                print("updated registration")
        else:
            raise Exception("Missing Argument(s)")

    def process(self, args):
        """
        Process an object
        """
        if args[0] == "-s":
            # TODO: Finish error handling
            vin = args[1]
            currentOwnerFname = args[2]
            currentOwnerLname = args[3]
            newOwnerFname = args[4]
            newOwnerLname = args[5]
            plate = args[6]

            # check if current owner matches most recent owner of the car
            prevRegistraion = self.api.executeQuery(
                """
                SELECT * FROM vehicles v, registrations r WHERE r.vin = v.vin
                AND v.vin = ? AND r.fname = ? and r.lname = ?
                AND r.expiry > ?
                """,
                (vin, currentOwnerFname, currentOwnerLname, dt.now())
            )
            if not prevRegistraion:
                raise Exception("Transaction cannot be processed. Current owner does not match registered.")
           
            # set the expiry date of the current registration
            regnoOld = self.api.executeQuery(
                """
                SELECT regno FROM registrations r, vehicles v WHERE WHERE r.vin = v.vin
                AND r.fname = ? and r.lname = ?
                """,
                (currentOwnerFname, currentOwnerLname)
            )
            newExpiry = dt.now()
            self.api.executeQuery(
                "UPDATE registrations SET expiry = ? WHERE regno = ?",
                (newExpiry, regnoOld),
                True
            )

            # set the registration and expiry date of the new registration
            regno = randint(0,999999)
            regdate = dt.now()
            expiry = dt.now() + datetime.timedelta(days=365)

            # create new registration in the db
            self.api.executeQuery(
                """
                INSERT INTO registrations (regno, regdate, expiry, plate, vin, fname, lname) 
                VALUES (?,?,?,?,?,?,?)
                """,
                (regno, regdate, expiry, plate, vin, newOwnerFname, newOwnerLname),
                True
            )
            print("completed processing bill of sale")

        # Process a payment
        elif args[0] == "-p":
            tno = args[1]
            amount = args[2]
            fine = args[3]
            pdate = dt.now()

            # calculate the amount paid for a given ticket
            amountPaid = self.api.executeQuery(
                            """
                            SELECT SUM(amount) FROM payments p, tickets t WHERE p.tno = t.tno
                            AND p.date < dt.now()
                            """
                        )

            # accept payment if amountPaid + payment Amount <= fine, otherwise raise error
            totalAmount = amountPaid + amount

            if fine >= totalAmount:
                # Update fine amount for the ticket
                fineRemaining = fine - totalAmount
                self.api.executeQuery(
                    "UPDATE tickets SET fine = ? WHERE tno = ?",
                    (fineRemaining, tno),
                    True
                )

                # Insert amount into payments table
                self.api.executeQuery(
                    """
                    INSERT INTO payments (tno, pdate, amount) 
                    VALUES (?,?,?)
                    """,
                    (tno, pdate, amount),
                    True
                )
            else:
                raise Exception("Amount paid exceeds ticket fine")
        else:
            raise Exception("Missing Argument(s)")

    def getAbstract(self, args):
        # get the person's name from the user
        fname = input("Enter first name of the person: ")
        lname = input("Enter last name of the person: ")

        # Ensure the person belongs to database
        person = self.api.executeQuery(
            """
            SELECT regno FROM births b1, births b2 WHERE b1.regno = b2.regno
            AND b1.fname = ? and b2.lname = ?
            """,
            (fname, lname)
        )
        if person == None:
            print("Invalid person entry")
        
        # get driver's abstract
        # ToDo: finish the query

        # sort tickets
        count = 0
        loops = 0
        # get ticket count
    #    todo cursor.execute("SELECT * from tickets where (# enter conditions))
        # ticket_set = self.c.fetchall()

        # Show 5 tickets if more than 5 and allow user to see more
        # if count == 5 or ticket == ticket_set[len(ticket_set) - 1]:
        #     choice = input("Select one of these tickets? (Enter option # or press enter to see more)")
        #     if choice == '':
        #         count = -1
        #         loops +=1
        #     else:
        #         try:
        #             choice = int(choice)
        #             return ticket_set[(loops * 4) + (choice - 1)][0]
        #         except ValueError:
        #             print("Invalid option. Please retry.")
        #             # return 
        # count += 1


    def issue(self, args):
        rno = args[1]
        fname = args[2]
        lname = args[3]
        make = args[4]
        model = args[5]
        year = args[6]
        color = args[7]
        violation = args[8]
        fine = args[9]
        vdate = str(dt.now())
        tno = randint(0,999999)

        # get registration number, fname and lname
        rno = ("Please enter a registration number to issue ticket: ")
        registration = self.api.executeQuery(
            "SELECT * FROM registrations WHERE rno = ?",
            (rno)
        )

        if registration:
            fname = registration[5]
            lname = registration[6]

        # Get vehicle details
        vehicle = self.api.executeQuery(
            """" "SELECT * FROM vehicles v, registration r WHERE r.vin = v.vin
                AND r.rno = ? """,
                (rno)
        )
        if vehicle:
            make = vehicle[1]
            model = vehicle[2]
            year = vehicle[3]
            color = vehicle[4]

        # Issue a ticket
        violation = input("Pleaser enter the violation description.")
        fine = input("Please enter the fine amount")
        try:
            if fine > 0:
                self.api.executeQuery(
                    """
                    INSERT INTO tickets (tno,regno,fine,violation,vdate) 
                    VALUES (?,?,?,?,?)
                    """,
                    (tno,
                    rno,
                    fine,
                    violation,
                    vdate
                    ),
                    True
                )
                print("The ticket is issued")
        except Exception as e:
            print("Invalid fine amount")
 

    def findOwner(self, args):
        """Find car owner along with vehicle and registration details
        # TODO: Implement
        """

    def quit(self):
        """
        Quits the program
        """
        self.quitProgram = True

if __name__ == "__main__":
    m = Main("DB")
    m.setup()
    while True:
        if m.quitProgram : break
        elif not m.user:
            user_name = input("Enter your id: ")
            user_pass = getpass("Enter your password: ")
            try:
                m.login(user_name, user_pass)
            except Exception as e:
                print(str(e))
        else:
            user_in = input("Enter a command: ")
            m.execute(user_in)
