import requests
from bs4 import BeautifulSoup

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


def anime_parser():
    anime_list = []
    response = requests.get('https://animevost.org/')
    soup = BeautifulSoup(response.text, 'html.parser')
    # res = soup.select('H2').string
    #     # for elem in res:
    #     #     print(elem)
    #     # print(type(res))
    for tag in soup.find_all("h2"):
        mid_titles = tag.get_text()
        anime_list.append(mid_titles.strip())

    return anime_list


def send_listpy():
    anime_list_previous = []
    count = 0
    while True:
        count +=1
        with open("log.txt", 'w') as log:
            log.write(str(count))
            print(count)
        time.sleep(3600)
        anime_list = anime_parser()
        if anime_list_previous == anime_list:
            print('no changes')

        else:
            port = 587  # для starttls подключения

            """Тут меняется SMTP сервер:"""
            smtp_server = "smtp.gmail.com"

            """Здесь можно поменять тему письма:"""
            subject = "Test email from Python"

            """Здесь можно поменять отправителя:"""
            sender_email = "otsgolyak@gmail.com"
            receiver_email = 'otsgolyak@gmail.com'

            """Пароль отправителя: """
            password = "pzvuk85f"

            msg = MIMEMultipart()

            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(beautifyer(anime_list), 'plain'))

            context = ssl.create_default_context()
            try:
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()  # Может быть опущено
                    server.starttls(context=context)
                    server.ehlo()  # Может быть опущено
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, msg.as_string())
                    print('send')
            except:
                print("error")

            anime_list_previous = anime_list
            continue

def beautifyer(anime_list):
    anime = ''
    for elem in anime_list:
        anime += "\n"+elem
    return anime

send_listpy()