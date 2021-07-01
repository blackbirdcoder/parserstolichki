from config import ACCEPT, SLEEP_PARAMETERS, MARKUP_ANALYZER # noqa
from random import uniform
import service.get_suitable_proxy # noqa
from . import get_document
from bs4 import BeautifulSoup
import time


def picking_pre_information(user_agent: str, proxy: str, category: tuple):
    # The function is not ready!
    # need to sleep
    time.sleep(uniform(*SLEEP_PARAMETERS[0]))
    information = []
    blank = {
        'category': category[1],
        'num': None,
        'links': ()
    }
    headers = {
        'user-agent': user_agent,
        'accept': ACCEPT['text']
    }
    link = category[-1]
    document = get_document(link, headers=headers, proxy=proxy)
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    pagination_item = soup.find_all('ul', class_='paging-list')[0].find_all('li', class_='paging-list__item')
