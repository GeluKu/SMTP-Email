import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    # import the necessary components first


    port = 2525
    smtp_server = "smtp.mailtrap.io"
    login = "e9e4ee09e3e699"  # paste your login generated by Mailtrap
    password = "ebafbbcb0f2b8c"  # paste your password generated by Mailtrap

    sender_email = "star.gekko@gmail.com"
    receiver_email = "gelu.liuta@gmail.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # write the text/plain part
    text = """\
    Hi,
    Check out the new post on the Mailtrap blog:
    SMTP Server for Testing: Cloud-based or Local?
    https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
    Feel free to let us know what content would be useful for you!"""

    # write the HTML part
    html = """\
    <html>
      <body>
        <p>Hi,<br>
           Check out the new post on the Mailtrap blog:</p>
        <p><a href="https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server">SMTP Server for Testing: Cloud-based or Local?</a></p>
        <p> Feel free to <strong>let us</strong> know what content would be useful for you!</p>
      </body>
    </html>
    """

    # convert both parts to MIMEText objects and add them to the MIMEMultipart message
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    # send your email
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(login, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    print('Sent')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    send_email()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
