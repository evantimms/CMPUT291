from bsddb3 import db
import re

mode_change = r'output=(?:(full)|(brief))' # capture group 1) whole command 2) which mode

term_query_with_prefix = (
	r'((subj\s*:)'	# Has either subj zero or more whitespace and colon
	r'|(body\s*:))'	# or body zero or more whitespace and colon
	r'\s*'			# zero or more whitespace are prefix
	r'(\w+%?)'		# word that optionally ends with %
	r'\s'			# space boundary (not \b)
)
term_query_without_prefix = (
	r'(^|\s+)'	# starts at beginning of line or with at least one space
	r'\w+%?'	# Word optionally ending with %
	r'\s'		# Space boundary
)

email_prefix = (
	r'((from)|(to)|(cc)|(bcc))' # one of address fields
	r'\s?'						# zero or more spaces
	r':'						# semicolon
)
email = (
	r'[\w.]+'	# one or more email chars
	r'@'		# at sign
	r'[\w.]+'	# one or more email chars
)
email_query = email_prefix + r'\s*' + email

date_prefix = (
	r'(date)'		# starts with date
	'\s*'			# Zero or more
	'(:|>=|<=|>|<)' # Order of operators matters: > before >= won't capture equals
)
date = r'\d{4}/\d{2}/\d{2}'  # yyy/mm/dd format
date_query = date_prefix + r'\s*' + date

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
