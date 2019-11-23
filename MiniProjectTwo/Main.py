from bsddb3 import db
import re
def phase3():
	# Open the databases
	termsDB = db.DB()
	emailsDB = db.DB()
	datesDB = db.DB()
	recsDB = db.DB()
	termsDB.open('te.idx',None,db.DB_HASH,db.DB_CREATE)
	emailsDB.open('em.idx',None,db.DB_BTREE,db.DB_CREATE)
	datesDB.open('da.idx',None,db.DB_BTREE,db.DB_CREATE)
	recsDB.open('re.idx',None,db.DB_BTREE,db.DB_CREATE)
	termsCursor = termsDB.cursor()
	datesCursor = datesDB.cursor()
	emailsCursor = emailsDB.cursor()
	recsCursor = recsDB.cursor()
	full = False
	brief = True
	quit = False
	while not quit: #Continue until user quits
		query = input("Enter your query. QUIT to exit.\n")
		if query.upper() == 'QUIT':
			quit = True
			continue
		valid, queries = verify(query) #Valid is set to True if query is vaild, false otherwise. Queries will be list of tuples or None
		if valid:
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
			print("That is an invalid query. Please try again.")
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

def verify(query): # Should takes in query and returns either True or False and either None or split contents
	pass

def main():
    	phase3()

main()