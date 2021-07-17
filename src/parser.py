import service
import utils
import config
from multiprocessing import Pool
from random import choice
from tqdm import tqdm


def main():
    print(config.INTRO)
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
                               desc='Receiving goods',
                               bar_format=config.PROGRESS_BAR_SETTING):
                goods.append(result[0])
    if goods:
        AMOUNT_GOODS = len(goods)
        with Pool(AMOUNT_GOODS // 1000) as p:
            stores_id = ()
            for result in tqdm(p.imap_unordered(utils.select_store_id, iterable=goods),
                               total=AMOUNT_GOODS,
                               desc='Retrieving store ID',
                               bar_format=config.PROGRESS_BAR_SETTING):
                if result:
                    # additional sorting exclude repetitions
                    for current_value in result:
                        if current_value not in stores_id:
                            stores_id += current_value,
        for identifier in tqdm(stores_id, desc='Create store tables in the database',
                               bar_format=config.PROGRESS_BAR_SETTING):
            utils.db.create_table(DIRECTORY, config.DB_NAME[1], config.SQL['create_store'].format(identifier))
        collection_goods = utils.preparation_goods_rec(goods)
        for item in tqdm(collection_goods, desc='Writing products to the database table',
                         bar_format=config.PROGRESS_BAR_SETTING):
            identifier_store, value = list(item.items())[0]
            utils.set_data_table(DIRECTORY, config.DB_NAME[1], config.SQL['set_store'].format(identifier_store), value)
        print(config.USER_NOTIFICATION['success'])


if __name__ == '__main__':
    main()
