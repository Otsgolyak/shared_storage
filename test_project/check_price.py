import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# response = requests.get('https://rozetka.com.ua/xiaomi_vxn4220gl/p35055167/')
# soup = BeautifulSoup(response.text, 'html.parser')
# res = soup.select(
#     'body > app-root > rz-main-app > pp-product-page > div > div > div > div > pp-tab-all > div.cust-wrap.clearfix > div.cust-content > div:nth-child(1) > pp-price-block > div.pp-goods-details.limited.ng-star-inserted > pp-price-block-label > pp-price-block-label-limited > div > div.detail-main-wrap.clearfix.detail-price-cheaper > div.detail-buy-label.ng-star-inserted > span > span:nth-child(1)')
# a = str(res)
# result = ""
# for i in a:
#     if i.isdigit():
#         result += i
# print(result)
#
#
# if int(result) == 759:
#     print(result)
#     mail_sender()
# else:
#     pass


def mail_sender():
    # create message object instance
    msg = MIMEMultipart()

    message = "Testing email"

    # setup the parameters of the message
    password = "A11235813a"
    msg['From'] = "otsgolyak@gmail.com"
    msg['To'] = "otsgolyak@gmail.com"
    msg['Subject'] = "Test"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.gmail.com: 465')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("successfully sent email")


response = requests.get('https://rozetka.com.ua/xiaomi_vxn4220gl/p35055167/')
soup = BeautifulSoup(response.text, 'html.parser')
res = soup.select(
    'body > app-root > rz-main-app > pp-product-page > div > div > div > div > pp-tab-all > div.cust-wrap.clearfix > div.cust-content > div:nth-child(1) > pp-price-block > div.pp-goods-details.limited.ng-star-inserted > pp-price-block-label > pp-price-block-label-limited > div > div.detail-main-wrap.clearfix.detail-price-cheaper > div.detail-buy-label.ng-star-inserted > span > span:nth-child(1)')
a = str(res)
result = ""
for i in a:
    if i.isdigit():
        result += i
print(result)


if int(result) == 759:
    print(result)
    mail_sender()
else:
    pass