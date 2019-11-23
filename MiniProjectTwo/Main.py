from bsddb3 import db
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
    termsDB = db.DB()
    emailsDB = db.DB()
    datesDB = db.DB()
    recsDB = db.DB()
    termsDB.open('te.idx', None, db.DB_BTREE, db.DB_RDONLY)
    emailsDB.open('em.idx', None, db.DB_BTREE, db.DB_RDONLY)
    datesDB.open('da.idx', None, db.DB_BTREE, db.DB_RDONLY)
    recsDB.open('re.idx', None, db.DB_HASH, db.DB_RDONLY)
    termsCursor = termsDB.cursor()
    datesCursor = datesDB.cursor()
    emailsCursor = emailsDB.cursor()
    recsCursor = recsDB.cursor()
    full = False
    brief = True
    quit_program = False
    return

    while not quit_program: #Continue until user quits
        query = input("Enter your query. QUIT to exit.\n")
        if query.upper() == 'QUIT':
            quit_program = True
            continue

        if verify(query):
            queries = query.split(expression)
            results = []
            for item in queries:
                for option in item:
                    if option[0] == 'option': #Checks if given query is an option change
                        if option[2] == 'full':
                            full = True
                            brief = False
                        else:
                            brief = True
                            full = False
                        results = None #Indicates no query results
                        break #Breaks current querys search
                    else:
                        current = getResults(option, termsCursor, datesCursor, emailsCursor) #Either a list of aID's or None
                        if current != None:
                            results.append(current)
                if results == None:
                    break
            if results != None and len(results) > 0: #Check that results exits
                if len(results) > 1: #If more than one condition
                    results = findMatches(results) #Find all aID's which satisfy all conditions
                else: #If only one codition
                    results = results[0] #Only one lists in results
                printResults(results, recsCursor, full, brief) #Prints relevant information for all aID's in results
        else:
            print("Your input contains an invalid query. Please try again.")
    print("Goodbye.")

# QUERIES HERE
def printResults(results, recs, full, brief):
    pass

def parseFull(rec):
	pass

def parseBrief(rec):
	pass

def getResults(query, terms, dates, emails):
	pass

def findMatches(results):
	pass

def verify(query):
    """
    Validates a query
    """
    return re.matches(query, query)
    

if __name__ == "__main__":
    main()