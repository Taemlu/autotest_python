import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime
import yaml

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)
def send_email():
    fromaddr = data["fromaddr"]
    toaddr = data["toaddr"]
    mypass = data["mail_passwd"]
    reportname = 'log.txt'

    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = f'Отчет о тестировании {datetime.datetime.now()}'

    with open(reportname, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = 'attachment; filename=%s"' % basename(reportname)
        msg.attach(part)

    body = "Автоматический отчет об тестировании"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smpt.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


if __name__ == '__main__':
    send_email()