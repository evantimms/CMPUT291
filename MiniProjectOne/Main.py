import sqlite3
from getpass import getpass

ROLES = {
    "a": [".quit", ".help", ".logout", ".register", ".renew", ".process", ".getAbstract"],
    "o": [".quit", ".help", ".logout"]
}

HELP_COMMANDS = {
    ".logout": "Log current user out",
    ".register": "Register a marriage or a birth",
    ".renew": "Renew a vechicle registration",
    ".process": "Process a bile of sale or a payment",
    ".getAbstract": "Get a drivers abstract",
    ".issue": "Issue a ticket",
    ".findOwner": "Find the owner of a vehicle"
}

class Sanitizer():
    def sanitizeInput(self, *args):
        """ 
        Sanitize a user input to prevent SQL Injection
        """
        # TODO
        return args

class Main():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.user = None
        self.userRole = None
        self.functions = None
        self.quitProgram = False

    def setup(self):
        """
        Load and intialize data and databases
        """
        f = open("CreateTables.sql", "r").read()
        self.c.executescript(f)
        f = open("AddBasicData.sql", "r").read()
        self.c.executescript(f)

    def execute(self, userIn):
        """
        Exectute a user instruction. Format should be COMMAND [ARGUEMENTS]
        """
        args = userIn.split()[1:]
        cmd = userIn.split()[0]
        if len(args) > 2:
            print("Invalid input. Command requires min 2 arguements")
        elif not self.user:
            raise Exception("User not logged in! Killing program")
        elif cmd not in self.functions.keys():
            print("Invalid command")
        else:
            # process input
            if len(args) > 0:
                self.functions[cmd](args[1:])
            else:
                self.functions[cmd]()
    
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
        self.c.execute(
            "SELECT * FROM users WHERE uid = ? AND pwd = ?",
            (uid, pwd)
        )
        user = self.c.fetchone()
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
        Register an object
        """
    
    def renew(self, args):
        """
        Renew an object
        """

    def process(self, args):
        """
        Process an object
        """

    def getAbstract(self, args):
        """
        Return a drivers abstract
        """

    def quit(self):
        """
        Quits the program
        """
        self.quitProgram = True


if __name__ == "__main__":
    m = Main("DB")
    m.setup()
    s = Sanitizer()
    while True:
        if m.quitProgram : break
        elif not m.user:
            user_name = input("Enter your id: ")
            user_pass = getpass("Enter your password: ")
            s.sanitizeInput(user_name, user_pass)
            try:
                m.login(user_name, user_pass)
            except Exception as e:
                print(str(e))
        else:
            user_in = input("Enter a command: ")
            m.execute(user_in)
            s.sanitizeInput(user_in)
