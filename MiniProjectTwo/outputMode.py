def full_output(row_id):
    row_id = 'Row ID: ' + re.findall(r'<row>(.*?)</row>', row_id)[0]
    sent_date = 'Date: ' + re.findall(r'<date>(.*?)</date>', row_id)[0]
    subject_field = 'Subject: ' + re.findall(r'<subj>(.*?)</subj>', row_id)[0]
    body_field = 'Body: ' + re.findall(r'<body>(.*?)</body>', row_id)[0]
    from_field = 'From: ' + re.findall(r'<from>(.*?)</from>', row_id)[0]
    to_field = 'To: ' + re.findall(r'<to>(.*?)</to>', row_id)[0]
    cc_field = 'CC: ' + re.findall(r'<cc>(.*?)</cc>', row_id)[0]
    bcc_field = 'BCC: ' + re.findall(r'<bcc>(.*?)</bcc>', row_id)[0]
    return row_id + '\n' + sent_date + '\n' + subject_field + '\n' + body_field + '\n' + from_field + '\n' + to_field + '\n' + cc_field + '\n' + bcc_field

def brief_output(row_id):
    row_id = 'Row ID: ' + re.findall(r'<row>(.*?)</row>', row_id)[0]
    subject_field = 'Subject: ' + re.findall(r'<subj>(.*?)</subj>', row_id)[0]
    return row_id + '\n' + subject_field