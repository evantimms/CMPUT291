import sqlite3

class Main():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.user = None

    def setup(self):
        """
        Load and intialize data and databases
        """

    def execute(self, cmd):
        """
        Exectute a user instruction
        """
        args = cmd.split()
        if len(args) > 2:
            raise Exception('Invalid input. Command requires min 2 arguements')
        elif not self.user:
            raise Exception('Please login')

        fns = {
            'login': self.login,
            'logout': self.logout,
            'register': self.register,
            'renew': self.renew,
            'process': self.process,
            'getabstract': self.getAbstract
        }
        fns[args[0]](args[1:])

    def login(self):
        """
        Log in a user
        """

    def logout(self):
        """
        Log out current user
        """

    def register(self):
        """
        Register an object
        """
    
    def renew(self):
        """
        Renew an object
        """

    def process(self):
        """
        Process an object
        """

    def getAbstract(self):
        """
        Return a drivers abstract
        """


if __name__ == "__main__":
    m = Main(':memory:') # replace with db name
    m.setup()
    if m.login() or True: # remove after login implemented
        while True:
            user_in = input("Enter a command: ")
            m.execute(user_in)
            if user_in == "quit":
                m.logout()
                break
