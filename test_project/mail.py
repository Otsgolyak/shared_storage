import smtplib, ssl

port = 587  # для starttls подключения
smtp_server = "smtp.gmail.com"
sender_email = "otsgolyak@gmail.com"
receiver_email = "otsgolyak@gmail.com"
password = "A11235813a"
message = "Testing how the mail works"

context = ssl.create_default_context()
try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Может быть опущено
        server.starttls(context=context)
        server.ehlo()  # Может быть опущено
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Mail sended succesfuly")
except:
    print("Something went wrong")


