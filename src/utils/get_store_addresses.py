from random import choice
from config import ACCEPT, TARGET, PAYLOAD  # noqa
import service.get_suitable_proxy # noqa
from . import get_document


def get_store_addresses(user_agent: list, proxies: list):
    """Pull out store addresses.
    Goes to the desired URL, gets the json object.
    Gets the addresses and prepares the data for writing to the database.
    :param user_agent: list of user-agents
    :param proxies: Proxy list
    :return: object to insert into the database
    """
    addresses = []
    headers = {
        'user-agent': choice(user_agent),
        'accept': ACCEPT['json']
    }
    proxy = service.get_suitable_proxy(proxies)
    url = TARGET['url'] + TARGET['folders'][2] + '/' + TARGET['folders'][3]
    document = get_document(url, parameter=PAYLOAD['city'], headers=headers, proxy=proxy)
    stores = document['stores']
    for store in stores:
        # Data is created ready prepared for database insertion
        addresses.append((None, store.get('id'), store.get('address'),
                         (store.get('phoneNumber').rstrip('..') if store.get('phoneNumber') != '' else None)))
    return addresses
