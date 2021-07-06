from config import SLEEP_PARAMETERS # noqa
import time
from random import uniform


def get_collection_goods(user_agent: str, proxy: str, links: list):
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
