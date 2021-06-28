import service
import utils
import config


def main():
    USER_AGENTS = service.get_user_agents(10)
    PROXIES = service.get_proxies(USER_AGENTS, 10)
    DIRECTORY = utils.create_folders()
    addresses = utils.get_store_addresses(USER_AGENTS, PROXIES)
    if addresses:
        utils.db.create_table(DIRECTORY, config.DB_NAME[0], config.SQL['create_address'])
        utils.db.set_data_table(DIRECTORY, config.DB_NAME[0], config.SQL['set_address'], addresses)


if __name__ == '__main__':
    main()
