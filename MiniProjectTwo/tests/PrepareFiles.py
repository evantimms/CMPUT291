import sys
import re

# load the xml file
xml = open(sys.argv[1], "r")
terms = open("terms.txt", "w")
emails = open("emails.txt", "w")
dates = open("dates.txt", "w")
recs = open("recs.txt", "w")


def write_to_terms(row, subject, body):
    term_pattern = (
        r'\b'    # Beginning of word boundary
        r'[\w-]' # alphanumeric, underscore, dash
        r'{3,}'  # 3 or more times
        r'\b'    # End of word boundary
    )

    # Ignore &#.*;, &#\d;, &lt;, $gt; &amp;, &apos; and &quot;
    subject_with_special_removed = re.sub(r'&.*?;', '', subject)
    body_with_special_removed = re.sub(r'&.*?;', '', body)

    # Get terms
    captured_subject_terms = re.findall(term_pattern, subject_with_special_removed)
    captured_body_terms = re.findall(term_pattern, body_with_special_removed)

    # Print to file
    for subject_term in captured_subject_terms:
        terms.write("s-{}:{}\n".format(subject_term.lower(), row))
    for body_term in captured_body_terms:
        terms.write("b-{}:{}\n".format(body_term.lower(), row))


def write_to_emails(row, frm, to, cc, bcc):
    """
    One line per email (i.e. frm, to, produce 2 lines)
    All emails are made lowercase
    """
    if frm:
        emails.write("from-{}:{}\n".format(frm.lower(), row))
    if to:
        emails.write("to-{}:{}\n".format(to.lower(), row))
    if cc:
        emails.write("from-{}:{}\n".format(cc.lower(), row))
    if bcc:
        emails.write("from-{}:{}\n".format(bcc.lower(), row))


def write_to_dates(row, date):
    """
    Writes the row and the date to dates.txt, where the format is 'd:l'
    where d is the date of the email, and l is the row id.
    """
    if date and len(date):
        dates.write("{}:{}\n".format(date, row))


def write_to_recs(row, line):
    """
    Writes the row and the line in xml to recs.txt, in form 
    I:rec where I is the row id and rec is the full email record in XML.
    """
    if line:
        recs.write("{}:{}".format(row, line))


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

            write_to_terms(row, subj, body)
            write_to_emails(row, frm, to, bcc, cc)
            write_to_dates(row, date)
            write_to_recs(row, l)


if __name__ == "__main__":
    main()
