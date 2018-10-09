'''import smtplib
FROM = "aishuyadav2233@gmail.com"
TO = "suriya.prakash64@gmail.com"
SUBJECT = "Test"
TEXT = "https://www.w3.org"
# Prepare actual message
message = """From: %s\nTo: %s\nSubject: %s\n\n%s
 """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("Enter your email id", "Enter your email password")
    server.sendmail(FROM, TO, message)
    server.close()
    print("successfully sent the mail")
except:
    print("failed to send mail")'''

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "aishuyadav2233@gmail.com"
you = "suriya.prakash64@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://localhost:63342/task%201/task%203/table.html?_ijt=i2t14jg2av83q62rb0sh4826ts"
html = """\
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
    border: 3px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 15px;
    text-align: middle;
}
</style>
</head>
<body>

<h2>Table</h2>

<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Date</th>
    <th>utc_Time</th>
    <th>File_size</th>
    <th>Arrival</th>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>

  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>

  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>

  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>

  </tr>

</table>

</body>
</html>

"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()
mail.login('Enter your email id', 'Enter your email password')
mail.sendmail(me, you, msg.as_string())
mail.quit()

