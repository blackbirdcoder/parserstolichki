import service
import utils
import config
from multiprocessing import Pool
from random import choice
from tqdm import tqdm


def main():
    USER_AGENTS = service.get_user_agents(10)
    PROXIES = service.get_proxies()
    DIRECTORY = utils.create_folders()
    addresses = utils.get_store_addresses(USER_AGENTS, PROXIES)
    if addresses:
        utils.db.create_table(DIRECTORY, config.DB_NAME[0], config.SQL['create_address'])
        utils.db.set_data_table(DIRECTORY, config.DB_NAME[0], config.SQL['set_address'], addresses)
    category = utils.get_category(USER_AGENTS, PROXIES)
    if category:
        utils.db.create_table(DIRECTORY, config.DB_NAME[0], config.SQL['create_category'])
        utils.db.set_data_table(DIRECTORY, config.DB_NAME[0], config.SQL['set_category'], category)
    # The same number of elements is needed for the correct work of multiprocessing queries
    AMOUNT_CATEGORY = len(category)
    selected_user_agents = [choice(USER_AGENTS) for _ in range(AMOUNT_CATEGORY)]
    selected_proxies = [service.get_suitable_proxy(PROXIES) for _ in range(AMOUNT_CATEGORY)]
    iterable = [*zip(selected_user_agents, selected_proxies, category)]
    with Pool(AMOUNT_CATEGORY) as p:
        pre_information = []
        for result in tqdm(p.imap_unordered(utils.picking_pre_information, iterable=iterable),
                           total=AMOUNT_CATEGORY,
                           desc='Getting the information you need',
                           bar_format=config.PROGRESS_BAR_SETTING):
            pre_information.append(result)
    if pre_information:
        product_links = utils.select_links(pre_information, 'links')
        AMOUNT_LINKS = len(product_links)
        del selected_user_agents, selected_proxies
        selected_user_agents = utils.filler(USER_AGENTS, AMOUNT_LINKS)
        gang_proxies = [service.get_suitable_proxy(PROXIES) for _ in range(10)]
        selected_proxies = utils.filler(gang_proxies, AMOUNT_LINKS)
        iterable = [*zip(selected_user_agents, selected_proxies, product_links)]
        with Pool(AMOUNT_LINKS // 1000) as p:
            goods = []
            for result in tqdm(p.imap_unordered(utils.get_collection_goods, iterable=iterable),
                               total=AMOUNT_LINKS,
                               desc='test goods',
                               bar_format=config.PROGRESS_BAR_SETTING):
                pass


if __name__ == '__main__':
    main()
