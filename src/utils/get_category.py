from random import choice
from config import ACCEPT, TARGET, MARKUP_ANALYZER  # noqa
import service.get_suitable_proxy # noqa
from . import get_document
from bs4 import BeautifulSoup


def get_category(user_agent: list, proxies: list):
    """Retrieves the category name and links to them.
    :param user_agent: list of user-agents
    :param proxies: Proxy list
    :return: object to insert into the database
    """
    category = []
    headers = {
        'user-agent': choice(user_agent),
        'accept': ACCEPT['text']
    }
    proxy = service.get_suitable_proxy(proxies)
    url = TARGET['url'] + TARGET['folders'][1]
    document = get_document(url, headers=headers, proxy=proxy)
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    items = soup.find_all('div', class_='itemContent__title')
    for item in items:
        # Data is created ready prepared for database insertion
        category.append((None, item.find('a', class_='catalogPreview__caption').get_text(),
                         item.find('a', class_='mainMenu__link').get('href')))
    return category
