import requests
from config import ACCEPT # noqa


def get_document(url, parameter=None, headers=None, proxy=None):
    """Create session makes a request to the specified address,
    returns content on success, otherwise it will show an error.
    :param url: string with the site address
    :param parameter: parameters for address
    :param headers: request header
    :param proxy: proxy, ip address of the intermediate server
    :return: page content or json
    """
    session = requests.Session()
    response = session.get(url, params=parameter, headers=headers, proxies=proxy)
    try:
        response.raise_for_status()
        if response.headers.get('content-type') == ACCEPT['json']:
            return response.json()
        else:
            return response.text
    except requests.exceptions.HTTPError as error:
        print(error)
