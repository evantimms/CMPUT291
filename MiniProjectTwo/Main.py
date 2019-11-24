from DBMS import DBMS
import re

mode_change = r'output=(?:(full)|(brief))'  # capture group 1) whole command 2) which mode

term_query_with_prefix = (
    r'(?P<field>'  # Captures field name
    r'(?:subj\s*)|'  # Has either subj zero or more whitespace and colon
    r'(?:body\s*))'  # or body zero or more whitespace and colon
    r':\s*'  # zero or more whitespace are prefix
    r'(?P<term>\w+%?)'  # word that optionally ends with %
    r'\s'  # space boundary (not \b)
)
term_query_without_prefix = (
    r'(?:^|\s+)'  # starts at beginning of line or with at least one space
    r'(?P<term>\w+%?)'  # Word optionally ending with %
    r'\s'  # Space boundary
)

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
    '\s*'  # Zero or more
    '(:|>=|<=|>|<)'  # Order of operators matters: > before >= won't capture equals
)
date = r'(\d{4}/\d{2}/\d{2})'  # yyy/mm/dd format
date_query = date_prefix + r'\s*' + date  # Group 1) operator 2) date


def verify(user_in):
    # TODO: how to verify? One big regex is unpredicatable and likely error prone
    return True


def main():
    quit_program = False
    full_output = False # Default output is brief
    dbms = DBMS()

    while not quit_program:  # Continue until user quits
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

        if verify(user_in):
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
        else:
            print("Your input contains an invalid query. Please try again.")
    print("Thanks! Goodbye.")


if __name__ == "__main__":
    main()
