import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "my@email.com"
you = "your@email.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<!DOCTYPE html>
<html>
<body>

<h2>Image as a Link</h2>
<p>The image is a link. You can click on it.</p>

<a href="https://www.flipkart.com">
htmlBody = "<html><body>Embedded Image:<br><img src="https://www.flipkart.com/miss-chief-track-pant-boy-s/p/itmf3zuyktghfbzs?pid=KPBFF7GHFVSU9NPG&lid=LSTKPBFF7GHFVSU9NPGACIJJR&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Deals%20of%20the%20Day_3_Under%E2%82%B9699%2BExtra%205%25Off_TFGXLYJ565EF_0&fm=neo/merchandising&iid=cb6560b1-cc7e-4d52-a57f-f623253f35c5.KPBFF7GHFVSU9NPG.SEARCH&ppt=StoreBrowse&ppn=Store&ssid=dn9rzo3ols0000001536128871917",alt="For email"></body></html>"
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
s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
s.starttls()
s.login("Enter your mail id")
s.sendmail("Enter your mail id","Reciver Message",msg.as_string())

# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()