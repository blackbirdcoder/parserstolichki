import service
import utils


def main():
    USER_AGENTS = service.get_user_agents(10)
    PROXIES = service.get_proxies(USER_AGENTS, 10)
    proxy = service.get_suitable_proxy(PROXIES)
    path_directory = utils.create_folders()
    if path_directory:
        pass


if __name__ == '__main__':
    main()
