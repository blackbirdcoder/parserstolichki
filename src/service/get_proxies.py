from random import choice, sample
from utils import get_document # noqa
from config import SERVICE_URL, SERVICE_OPTIONS, MARKUP_ANALYZER, REGEX, USER_INTERFACE # noqa
from bs4 import BeautifulSoup
import re


def get_proxies(user_agent: list, num_proxy: int):
    """Retrieves a list of proxy.

    Goes to the resource gets free proxies.
    Returns a random list with the specified number of proxies.

    :param user_agent: list with user-agents
    :param num_proxy: how many proxies do you need, quantity
    :return: proxy list
    """
    pattern = re.compile(REGEX['proxy'])
    headers = {'user-agent': choice(user_agent)}
    document = get_document(SERVICE_URL['proxy'], headers=headers)
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    text = soup.get_text()
    result = pattern.findall(text)
    try:
        return sample(result, num_proxy)
    except ValueError as error:
        print(USER_INTERFACE['attention_block'].format('Proxy') + ' ' + str(error))
        print(USER_INTERFACE['attention_block'].format('Proxy') + ' ' + USER_INTERFACE['attention_dialog'])
        num_proxy = SERVICE_OPTIONS['number']
        return sample(result, num_proxy)
