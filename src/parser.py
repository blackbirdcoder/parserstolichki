import service
import utils
import config


def main():
    USER_AGENTS = service.get_user_agents(10)
    PROXIES = service.get_proxies(USER_AGENTS, 10)
    DIRECTORY = utils.create_folders()


if __name__ == '__main__':
    main()
