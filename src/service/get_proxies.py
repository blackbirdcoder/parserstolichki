from config import PROXIES, LOGIN, PASSWORD, USER_NOTIFICATION  # noqa
import sys


class ParserInvalidProxyData(Exception):
    """Responding to an error with data from the config."""
    def __init__(self, proxy, login, password):
        self.proxy = proxy
        self.login = login
        self.password = password

    def error_notifi(self):
        print(USER_NOTIFICATION['invalid_proxy'].format(self.proxy, self.login, self.password))


def get_proxies():
    """Forms a list of proxies for connection.
    Data is taken from the config.
    If the data is not correct, throws an exception and terminates the program.
    :return: Proxy list for connection
    """
    proxies = []
    try:
        if not PROXIES or not LOGIN or not PASSWORD:
            raise ParserInvalidProxyData(PROXIES, LOGIN, PASSWORD)
        else:
            for proxy in PROXIES:
                proxies.append(f'{LOGIN}:{PASSWORD}@{proxy}')
        return proxies
    except Exception as error:
        print(error.error_notifi())
        sys.exit()

