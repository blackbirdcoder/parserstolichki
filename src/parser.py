import service
import utils


def main():
    USER_AGENTS = service.get_user_agents(10)
    PROXIES = service.get_proxies(USER_AGENTS, 10)
    proxy = service.get_suitable_proxy(PROXIES)
    DIRECTORY_OBJ = utils.create_folders()
    if DIRECTORY_OBJ[0]:
        pass


if __name__ == '__main__':
    main()
