from DBMS import DBMS
import sys
import re

mode_change = r'output=(?:(full)|(brief))'  # capture group 1) whole command 2) which mode

term_query_with_prefix = (
    r'(?P<field>'  # Captures field name
    r'(?:subj\s*)|'  # Has either subj zero or more whitespace and colon
    r'(?:body\s*))'  # or body zero or more whitespace and colon
    r':\s*'  # zero or more whitespace are prefix
    r'(?P<term>\w+%?)'  # word that optionally ends with %
    r'\s*'  # space boundary (not \b)
)
term_query_without_prefix = (
    r'(?:^|\s+)'  # starts at beginning of line or with at least one space
    r'(?!subj|body|to|cc|bcc|date|from)'  # prevents grabbing these words, which it will otherwise
    r'(?P<term>\w+%?)'  # Word optionally ending with %
)

print(term_query_with_prefix)
print(term_query_without_prefix)
email_prefix = (
    r'(?P<field>'
    r'(?:from)|(?:to)|(?:cc)|(?:bcc))'  # one of address fields
    r'\s?'  # zero or more spaces
    r':'  # semicolon
)
email = (
    r'(?P<email>'
    r'[\w.]+'  # one or more email chars
    r'@'  # at sign
    r'[\w.]+)'  # one or more email chars
)
email_query = email_prefix + r'\s*' + email  # Group 1) field, 2) email

date_prefix = (
    r'(?:date)'  # starts with date (dont capture)
    r'\s*'  # Zero or more
    r'(?P<operator>:|>=|<=|>|<)'  # Order of operators matters: > before >= won't capture equals
)
date = r'(?P<date>\d{4}/\d{2}/\d{2})'  # yyy/mm/dd format
date_query = date_prefix + r'\s*' + date  # Group 1) operator 2) date

def main(testQuery = None):
    quit_program = False
    full_output = False # Default output is brief
    dbms = DBMS()

    while not quit_program:  # Continue until user quits
        if testQuery:
            user_in = testQuery
            quit_program = True
        else:
            user_in = input("Enter a query. QUIT to exit.\n")

        if user_in.upper() == 'QUIT':
            quit_program = True
            continue

        if re.match(mode_change, user_in):
            output = user_in.split("=")[1]
            if output == "full":
                full_output = True
                print("Output changed to full.")
            elif output == "brief":
                full_output = False
                print("Output changed to brief.")
            else:
                raise ValueError("Invalid argument for output: {}".format(output))

        dbms.resetQuery()
        for date_condition in re.finditer(date_query, user_in):
            dbms.runDateQuery(date_condition['operator'], date_condition['date'])
        for email_condition in re.finditer(email_query, user_in):
            dbms.runEmailQuery(email_condition['field'], email_condition['email'])
        for term_condition in re.finditer(term_query_with_prefix, user_in):
            dbms.runTermQuery(term_condition['field'], term_condition['term'])
        for term_condition in re.finditer(term_query_without_prefix, user_in):
            dbms.runTermQuery(None, term_condition['term'])
        dbms.getResults(full_output)

    print("Thanks! Goodbye.")


test_queries = [
    "subj:gas",
    "subj:gas body:earning",
    "confidential%",
    "from:phillip.allen@enron.com",
    "to:phillip.allen@enron.com",
    "to:kenneth.shulklapper@enron.com  to:keith.holst@enron.com",
    "date:2001/03/15",
    "date>2001/03/10",
    "bcc:derryl.cleaveland@enron.com  cc:jennifer.medcalf@enron.com",
    "body:stock  confidential  shares  date<2001/04/12"
]

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        for test in test_queries:
            try:
                print("============================")
                main(test)
            except Exception as e:
                print("FAILED QUERY TEST {}".format(test))
                print(e)
    else:
        main()


# TODO: Finding &amp;
# TODO: Intersection on terms only seems to grab first time
