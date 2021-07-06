from config import ACCEPT, SLEEP_PARAMETERS, MARKUP_ANALYZER, PAYLOAD # noqa
from random import uniform
from . import get_document
from bs4 import BeautifulSoup
import time


def picking_pre_information(user_agent: str, proxy: str, category: tuple):
    """Collects preliminary information for further successful receipt of goods.
    Finds the maximum number of pages for a category and collects category product links.
    :param user_agent: user-agent
    :param proxy: proxy
    :param category: object where the category links are
    :return: object with preliminary information, there are links to each product
    """
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
    numbers = []
    # Finding the number of pages in a category
    document = get_document(link, headers=headers, proxy=proxy)
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    pagination_items = soup.find_all('ul', class_='paging-list')[0].find_all('li', class_='paging-list__item')
    for item in pagination_items:
        link_elem = item.find_all('a')
        if link_elem:
            num = link_elem[0].get_text()
            numbers.append(int(num)) if num.isdigit() else numbers.append(1)
    blank['num'] = max(numbers)
    del document, soup
    # Collection of links to the product
    for number in range(blank['num']):
        document = get_document(link, parameter=PAYLOAD['page'] + str(number + 1), headers=headers, proxy=proxy)
        soup = BeautifulSoup(document, MARKUP_ANALYZER)
        link_product = soup.find_all('a', class_='text-black-class text-success-hover-class')
        for item in link_product:
            blank['links'] += item['href'],
        del document, soup
    information.append(blank)
    return information[0]
