import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# create family members and list for repeating email task
class Family:
    def __init__(self, name, secretsanta, email):
        self.name = name
        self.secretsanta = secretsanta
        self.email = email


family1 = Family("Kevin", "Frances", "apicella.kevin@gmail.com")
family2 = Family("Frances", "Joe", "lovethydrum@gmail.com")
family_list = [family1, family2]
# back to reality, oops there goes gravity

sender_email = "apicellasecretsanta@gmail.com"
password = "burrito2020"

for people in family_list:
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = people.email

    text = f"""\
    Good evening {people.name}!
    
    This email is a test to send out the holiday christmas secret santa information.
    LET'S DO IT AT RANDOM!
    Your person is {people.secretsanta}.  You can find their information at www.cnn.com """

    html = f"""\
    <html>
      <p>Good evening {people.name}!</p>
        This email is a test to send out the holiday christmas secret santa information.<b>
        LET'S DO IT AT RANDOM!<b>
        Your person is {people.secretsanta}.  You can find their information at 
        <a href="http://www.cnn.com">Family Excel Sheet</a>"""
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, people.email, message.as_string())
