import requests
from bs4 import BeautifulSoup

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

    # return (mid_titles)


anime_parser()