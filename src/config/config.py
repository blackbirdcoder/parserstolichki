import os
from dotenv import load_dotenv

load_dotenv()
# ============ Proxy data ================
PROXIES = os.getenv('PROXIES').replace(' ', '').split(',')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

# ============ Important data ================
TARGET = {
    'url': 'https://stolichki.ru/',
    'folders': ['drugs', 'catalog', 'stores', 'all', 'stores']
}

PAYLOAD = {
    'city': 'cityId=1',
    'page': 'page='
}

# for request header
ACCEPT = {
    'json': 'application/json',
    'text': 'text/html'
}

# parser HTML
MARKUP_ANALYZER = 'lxml'

# addresses to receive data for making a request
SERVICE_URL = {
    'user-agent': 'https://seolik.ru/user-agents-list',
    'test': 'https://www.google.com/'
}

SERVICE_OPTIONS = {
    'number': 5,
    'timeout': 3,
    'multiplication_attempts': 2
}

# search patterns
REGEX = {
    'user-agent': 'Mozilla/5.0',
}

# user notifications
USER_NOTIFICATION = {
    'attention_block': '[Attention {}]',
    'attention_dialog': f'Returning {SERVICE_OPTIONS["number"]} items from the list. This kept parser going',
    'proxy_error': 'Rancid proxy {} {}',
    'invalid_proxy': 'Invalid proxy data, check the data, the program cannot run.\n'
                     'The proxies you provided: {} \n'
                     'Your login: {} \n'
                     'Your password: {} \n'
                     'I can not work with this data check the data',
    'bad_connect': 'Proxies are probably not valid. The program has stopped. Please check the proxy.\n'
                   'Connection attempts are: {}',
    'success': 'Data received. See the output folder.'
}

# for data output
FOLDERS = ['output', 'Moscow', 'db']

# for data db
DB_NAME = ['different', 'stores']

#  for sleep
SLEEP_PARAMETERS = ((1, 3), (1, 5))

# progress bar settings
PROGRESS_BAR_SETTING = '{l_bar}{bar:10}{r_bar}{bar:-10b}'

# ============== sql code
SQL = {
    'create_address': """CREATE TABLE IF NOT EXISTS address (
                        id INTEGER PRIMARY KEY,
                        stores_id INTEGER,
                        address TEXT,
                        telephone TEXT)""",
    'set_address': """INSERT INTO address VALUES (?, ?, ?, ?)""",
    'create_category': """CREATE TABLE IF NOT EXISTS category (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        link TEXT)""",
    'set_category': """INSERT INTO category VALUES (?, ?, ?)""",
    'create_store': """CREATE TABLE IF NOT EXISTS "{}" (
                id INTEGER PRIMARY KEY,
                product_code INTEGER,
                vendor_code INTEGER,
                product_name TEXT,
                product_link TEXT,
                images_link TEXT,
                online_price REAL,
                address_store TEXT,
                store_price REAL)""",
    'set_store': """INSERT INTO "{}" VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
}
# =========== intro
INTRO = """
╔═╗┌─┐┬─┐┌─┐┌─┐┬─┐  ╔═╗┌┬┐┌─┐┬  ┬┌─┐┬ ┬┬┌─┬
╠═╝├─┤├┬┘└─┐├┤ ├┬┘  ╚═╗ │ │ ││  ││  ├─┤├┴┐│
╩  ┴ ┴┴└─└─┘└─┘┴└─  ╚═╝ ┴ └─┘┴─┘┴└─┘┴ ┴┴ ┴┴                                                                                                                                      
"""

