import DBMS
import re

# Grammar
alphanumeric = "[0-9a-zA-Z_-]"
numeric = "[0-9]"
date = "{numeric}{numeric}{numeric}{numeric}/{numeric}{numeric}/{numeric}{numeric}"
datePrefix = 'date' whitespace* (':' | '>' | '<' | '>=' | '<=')
dateQuery = datePrefix whitespace* date
emailterm = alphanumeric+ | alphanumeric+ '.' emailterm
email = emailterm '@' emailterm
emailPrefix	= (from | to | cc | bcc) whitespace* ':'
emailQuery = emailPrefix whitespace* email
term = alphanumeric+
termPrefix	= (subj | body) whitespace* ':'
termSuffix = '%' 
termQuery = termPrefix? whitespace* term termSuffix?
expression = dateQuery | emailQuery | termQuery 
query = expression (whitespace expression)*
modeChange = 'output=full' | 'output=brief'
command = query | modeChange

def main():
	# Open the databases
    full = False
    brief = True
    quit_program = False
    
    dbms = DBMS()

    while not quit_program: #Continue until user quits
        user_in = input("Enter your user_in. QUIT to exit.\n")
        if user_in.upper() == 'QUIT':
            quit_program = True
            continue
        
        if verify(user_in):
            queries = buildQueries(user_in)
            dbms.resetQuery()
            for query in query:
                if re.matches(query, dateQuery):
                    # TODO: Build query parts
                    dbms.runDateQuery()
                elif re.matches(query, emailQuery):
                    # TODO: Build query parts
                    ids = dbms.runEmailQuery()
                elif re.matches(query, termQuery):
                    # TODO: Build query parts
                    dbms.runTermQuery()
                else:
                    raise Exception("cannot match query with any type.")
            dbms.getResults()
        else:
            print("Your input contains an invalid query. Please try again.")
    print("Goodbye.") 

if __name__ == "__main__":
    main()