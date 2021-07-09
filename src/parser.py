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
    AMOUNT_ELEMENTS = len(category)
    selected_user_agents = [choice(USER_AGENTS) for _ in range(AMOUNT_ELEMENTS)]
    selected_proxies = [service.get_suitable_proxy(PROXIES) for _ in range(AMOUNT_ELEMENTS)]
    iterable = [*zip(selected_user_agents, selected_proxies, category)]
    with Pool(AMOUNT_ELEMENTS) as p:
        pre_information = []
        for value in tqdm(p.imap_unordered(utils.picking_pre_information, iterable=iterable),
                          total=AMOUNT_ELEMENTS,
                          desc='Getting the information you need',
                          bar_format=config.PROGRESS_BAR_SETTING):
            pre_information.append(value)
    if pre_information:
        product_links = utils.select_links(pre_information, 'links')



if __name__ == '__main__':
    main()
