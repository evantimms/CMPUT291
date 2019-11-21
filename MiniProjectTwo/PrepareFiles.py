import sys
import re

# load the xml file
xml = open("Input10.xml", "r")
terms = open("terms.txt", "w")
emails = open("emails.txt", "w")
dates = open("dates.txt", "w")
recs = open("recs.txt", "w")

for l in xml:
    if re.match('<mail>.*</mail>', l):
        row = re.search("<row>(.*)</row>", l).group(1)
        date = re.search("<date>(.*)</date>", l).group(1)
        frm = re.search("<from>(.*)</from>", l).group(1)
        to = re.search("<to>(.*)</to>", l).group(1)
        body = re.search("<body>(.*)</body>", l).group(1)

        print(row, date, frm, to, body)
        