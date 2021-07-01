import service
import utils
import config
from multiprocessing import Pool


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
    selected_proxies = [service.get_suitable_proxy(PROXIES) for _ in range(5)]
    with Pool(5) as p:
        p.starmap(utils.picking_pre_information, iterable=[*zip(USER_AGENTS, selected_proxies, category)])


if __name__ == '__main__':
    main()
