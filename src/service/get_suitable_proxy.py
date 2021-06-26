import requests
from config import SERVICE_URL, SERVICE_OPTIONS, USER_INTERFACE # noqa
from random import choice


def get_suitable_proxy(proxies: list):
    """Gets a random proxy from the list.
     Check the proxy for working, if it works, it will return proxy.

    :param proxies: list of received proxies
    :rtype: dict
    :return: working proxy
    """
    proxy_blank = {
        'http': 'http://' + choice(proxies)
    }

    def _check():
        try:
            requests.get(SERVICE_URL['test'], proxies=proxy_blank, timeout=SERVICE_OPTIONS['timeout'])
        except Exception as error:
            print(USER_INTERFACE['attention_block'].format('Check proxy') + ' ' + error)
            print(USER_INTERFACE['attention_block'].format('Check proxy') + ' '
                  + USER_INTERFACE['proxy_error'].format(proxy_blank['http']))
            return False
        return True

    while True:
        if not _check():
            proxy_blank['http'] = 'http://'
            proxy_blank['http'] += choice(proxies)
        else:
            break
    return proxy_blank
