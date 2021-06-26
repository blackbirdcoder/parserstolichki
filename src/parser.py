import service


def main():
    USER_AGENTS = service.get_user_agent(10)
    PROXIES = service.get_proxy(USER_AGENTS, 10)


if __name__ == '__main__':
    main()
