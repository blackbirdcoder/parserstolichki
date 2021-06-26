import service


def main():
    USER_AGENTS = service.get_user_agents(10)
    PROXIES = service.get_proxies(USER_AGENTS, 10)
    proxy = service.get_suitable_proxy(PROXIES)


if __name__ == '__main__':
    main()
