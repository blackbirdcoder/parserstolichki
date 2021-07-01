import requests
from config import SERVICE_URL, SERVICE_OPTIONS, USER_NOTIFICATION  # noqa
from random import choice
import sys


class ParserManyFailedConnections(Exception):
    """Reacts to a large number of failed connections."""
    def __init__(self, connection_attempts):
        self.connection_attempts = connection_attempts

    def error_notifi(self):
        print(USER_NOTIFICATION['bad_connect'].format(self.connection_attempts))


def get_suitable_proxy(proxies: list):
    """Finds a suitable proxy.
    There is also a proxy check for suitability.
    If the proxy is bad, it will throw exceptions and stop the program.
    :param proxies: list of correctly configured proxies
    :return: workable proxy
    """
    connection_attempts = len(proxies) * SERVICE_OPTIONS['multiplication_attempts']
    random_proxy = choice(proxies)
    proxies_blank = {
        'http': 'http://{}'.format(random_proxy),
        'https': 'https://{}'.format(random_proxy),
    }

    def _check():
        try:
            requests.get(SERVICE_URL['test'], proxies=proxies_blank, timeout=SERVICE_OPTIONS['timeout'])
        except Exception as error:
            print(USER_NOTIFICATION['attention_block'].format('Check proxy') + ' ' + str(error))
            print(USER_NOTIFICATION['attention_block'].format('Check proxy') + ' '
                  + USER_NOTIFICATION['proxy_error'].format(proxies_blank['http'], proxies_blank['https']))
            return False
        return True

    while True:
        if not _check():
            random_proxy = choice(proxies)
            proxies_blank['http'] = 'http://{}'.format(random_proxy)
            proxies_blank['https'] = 'https://{}'.format(random_proxy)
            connection_attempts -= 1
        else:
            break

        try:
            if connection_attempts == 0:
                raise ParserManyFailedConnections(connection_attempts)
        except Exception as error_connect:
            print(error_connect.error_notifi())
            sys.exit()
    return proxies_blank
