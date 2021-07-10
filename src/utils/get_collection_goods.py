from config import SLEEP_PARAMETERS, ACCEPT, MARKUP_ANALYZER # noqa
import time
from random import uniform
from . import get_document
from bs4 import BeautifulSoup


def get_collection_goods(data):
    user_agent, proxy, link = data
    # need to sleep
    time.sleep(uniform(*SLEEP_PARAMETERS[1]))
    collection_goods = []
    blank = {
        'availability': False,
        'product_code': None,
        'vendor_code': None,
        'name': None,
        'link_product': None,
        'link_picture': None,
        'online_price': None,
        'stores': []
    }
    headers = {
        'user-agent': user_agent,
        'accept': ACCEPT['text']
    }
    document = get_document(link, headers=headers, proxy=proxy)
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    absent = soup.find('p', class_='product-anywhere badge-class badge-secondary-class')
    if not absent:
        pass
