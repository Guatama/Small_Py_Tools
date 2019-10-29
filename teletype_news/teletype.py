#! python
import datetime
import meduza
import platform, os
from time import sleep
import requests
from bs4 import BeautifulSoup


def get_meduza_news(num=10, lang='ru', last=True):
    news_top = []
    # news[0]['og']['url'] - unique url to the news
    for article in meduza.section('news', n=num, lang=lang):
        news_top.append((datetime.datetime.fromtimestamp(article['datetime']), article['title']))
    news_top.sort(reverse=last)
    return news_top


def get_yndx_top_news():
    news_top = []
    r = requests.get('https://yandex.ru')
    # class='news__item-content'
    soup = BeautifulSoup(r.text, features='lxml')
    news = soup.findAll(class_='news__item-content')
    news_titles = [title.text for title in news]
    for article in news_titles:
        news_top.append((datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), article))
    return news_top


def print_news(news_top):
    for i in news_top:
        print(f'{i[0]} >>> {i[1]}')


def teletype(min=5):
    num = 1
    today = datetime.datetime.now()
    while True:
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        stocks = meduza.stocks()
        header = f"Updated: {num:3}. \t    >>> Today is {today.strftime('%d/%m/%Y')}"
        usd_stock = f"\t| Курс USD: {stocks['usd']['current']}{' v ' if stocks['usd']['state'] == 'down' else ' ^ '}"
        brent_stock = f"\tКурс brent: {stocks['brent']['current']}{' v ' if stocks['brent']['state'] == 'down' else ' ^ '}"
        header = header + usd_stock + brent_stock

        print(header)
        print('-' * len(header))
        num += 1
        meduza_news = get_meduza_news()
        print_news(meduza_news)
        print('-' * len(header))
        yndx_news = get_yndx_top_news()
        print_news(yndx_news)
        sleep(60 * min)


if __name__ == '__main__':
    teletype(30)
