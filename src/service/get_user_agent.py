from src.utils.get_document import get_document
from bs4 import BeautifulSoup
from config import MARKUP_ANALYZER, SERVICE_URL, REGEX  # noqa
import re
from random import sample


def get_user_agent(num_ua: int):
    """Retrieves a list of user-agents.

    Receives data from a resource, makes a list of them.
    Returns the required number of user-agents.

    :param num_ua: number of user-agents
    :return: list of random user-agents
    """
    result = []
    document = get_document(SERVICE_URL['user-agent'])
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    cells = soup.find_all('td')
    for cell in cells:
        if re.match(REGEX['user-agent'], cell.get_text()):
            result.append(''.join(cell.get_text().split('\n')).strip())
    try:
        return sample(result, num_ua)
    except ValueError as error:
        print('[Attention] ' + str(error))
        print('[Attention] Returning five items from the list. This kept parser going')
        num_ua = 5
        return sample(result, num_ua)

