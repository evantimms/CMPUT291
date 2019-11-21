import sys
import re

# load the xml file
xml = open("Input10.xml", "r")
terms = open("terms.txt", "w")
emails = open("emails.txt", "w")
dates = open("dates.txt", "w")
recs = open("recs.txt", "w")

def writeToTerms(row, subject, body):
    pass

def writeToEmails(row, frm, to, cc, bcc):
    pass

def writeToRecs(row, date):
    pass

def writeToDates(row, line):
    pass


def main():
    for l in xml:
        if re.match('<mail>.*</mail>', l):
            row = re.search("<row>(.*)</row>", l).group(1)
            date = re.search("<date>(.*)</date>", l).group(1)
            frm = re.search("<from>(.*)</from>", l).group(1)
            to = re.search("<to>(.*)</to>", l).group(1)
            bcc = re.search("<bcc>(.*)</bcc>", l).group(1)
            cc = re.search("<cc>(.*)</cc>", l).group(1)
            body = re.search("<body>(.*)</body>", l).group(1)
            subj = re.search("<subj>(.*)</subj>", l).group(1)

            writeToTerms(row, subj, body)
            writeToEmails(row, frm, to, bcc, cc)
            writeToDates(row, date)
            writeToRecs(row, l)
        

if __name__ == "__main__":
    main()