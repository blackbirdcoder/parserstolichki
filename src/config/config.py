# ============ Important data ================
TARGET = {
    'url': 'https://stolichki.ru/',
    'folders': ['drugs', 'catalog', 'stores', 'all', 'stores']
}

PAYLOAD = {
    'city_id': 'cityId=1',
    'page': 'page='
}

# parser HTML
MARKUP_ANALYZER = 'lxml'

# addresses to receive data for making a request
SERVICE_URL = {
    'user-agent': 'https://seolik.ru/user-agents-list',
    'proxy': 'https://free-proxy-list.net/'
}

# search patterns
REGEX = {
    'user-agent': 'Mozilla/'
}

