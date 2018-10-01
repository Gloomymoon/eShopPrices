import urllib.request

from bs4 import BeautifulSoup
from datetime import datetime

from app import db
from app.main.models import eShopPrice


def test_job():
    print("test job run.")


def get_page():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url="https://eshop-prices.com/prices", headers=headers)

    fp = urllib.request.urlopen(req)
    mybytes = fp.read()

    html_doc = mybytes.decode("utf8")

    soup = BeautifulSoup(html_doc)

    fp.close()
    print(datetime.now(), soup.select('div.prices > table'))

    price = eShopPrice(datetime=datetime.now(), content=str(soup.select('div.prices > table')[0]))
    #price = eShopPrice(datetime=datetime.now(), content=html_doc)
    with db.app.app_context():
        db.session.add(price)
        db.session.commit()


