from config import SLEEP_PARAMETERS, ACCEPT, MARKUP_ANALYZER, TARGET, PAYLOAD # noqa
import time
from random import uniform
from . import get_document
from bs4 import BeautifulSoup


def get_collection_goods(data):
    """Extraction data from the site.
    :param data: Object with data user agents, proxies and links to product categories
    :return: Goods and shops are also present
    """
    user_agent, proxy, link = data
    # need to sleep
    time.sleep(uniform(*SLEEP_PARAMETERS[1]))
    collection_goods = []
    blank = {
        'availability': False,
        'product_code': None,
        'vendor_code': None,
        'name': None,
        'link_product': None,
        'link_picture': None,
        'online_price': None,
        'stores': []
    }
    headers = {
        'user-agent': user_agent,
        'accept': ACCEPT['text']
    }
    document = get_document(link, headers=headers, proxy=proxy)
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    found_product = soup.find('p', class_='badge-class product-not-found')
    available = soup.find('p', class_='product-anywhere badge-class badge-secondary-class')
    if not found_product and not available:
        # get goods
        blank['availability'] = True
        crumbs = soup.select('ul.breadCrambs>li:nth-child(3)')
        product_name = crumbs[0].select('span')[0].get_text().strip()
        product_link = crumbs[0].select('meta[content]')[0].attrs['content']
        blank['name'] = product_name
        blank['link_product'] = product_link
        try:
            code = soup.select('div.product-button+p')[0].get_text().split(':')[1].strip()
        except IndexError as error:
            print('Product code not received')
            print(f'The incident happened here {link}')
            code = ''
        if code is not '':
            blank['product_code'] = code
            blank['vendor_code'] = str(100000 + int(code))
        picture = soup.select('picture>source')[0].attrs['srcset']
        path_part = picture.split('/')
        if 'default.jpg' not in path_part:
            blank['link_picture'] = picture
        online_price = soup.find('p', class_='part-price-with-discount '
                                             'font-weight-bold-class d-flex-class '
                                             'align-items-center-class').get_text().strip()
        blank['online_price'] = online_price
        del document, soup
        # get stores
        headers['accept'] = ACCEPT['json']
        url = TARGET['url'] + TARGET['folders'][0] + '/' + str(blank['product_code']) + '/' + TARGET['folders'][2]
        document = get_document(url, headers=headers, proxy=proxy, parameter=PAYLOAD['city'])
        stores = document['stores']
        for store in stores:
            item = {'id_store': store.get('id'), 'address': None, 'price': None}
            if 'Санкт-Петербург' not in store.get('address').split(' '):
                item['address'] = store.get('address')
            parts = store.get('parts')
            for part in parts:
                item['price'] = part.get('priceStore')
                break
            blank['stores'].append(item)
    collection_goods.append(blank)
    return collection_goods
