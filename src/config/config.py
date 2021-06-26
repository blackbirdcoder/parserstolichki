# ============ Important data ================
TARGET = {
    'url': 'https://stolichki.ru/',
    'folders': ['drugs', 'catalog', 'stores', 'all', 'stores']
}

PAYLOAD = {
    'city': 'cityId=1',
    'page': 'page='
}

# parser HTML
MARKUP_ANALYZER = 'lxml'

# addresses to receive data for making a request
SERVICE_URL = {
    'user-agent': 'https://seolik.ru/user-agents-list',
    'proxy': 'https://free-proxy-list.net/',
    'test': 'https://www.google.com/'
}

SERVICE_OPTIONS = {
    'number': 5,
    'timeout': 3
}

# search patterns
REGEX = {
    'user-agent': 'Mozilla/5.0',
    'proxy': '[0-9]{3}.[0-9]{3}.[0-9]{3}.[0-9]{3}:[0-9]{2,5}'
}

# user notifications
USER_INTERFACE = {
    'attention_block': '[Attention {}]',
    'attention_dialog': f'Returning {SERVICE_OPTIONS["number"]} items from the list. This kept parser going',
    'proxy_error': 'Rancid proxy {}'
}

# for data output
FOLDERS = ['output', 'Moscow', 'db']

# for data db
DB_NAME = ['different', 'stores']

