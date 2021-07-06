def select_links(data: list, key_name: str):
    """Selects non-duplicate links.
    :param data: list with elements where the links are
    :param key_name: the name of the element where the links are
    :return: non-duplicate product links
    """
    result = ()
    for element in data:
        links = element.get(key_name)
        for link in links:
            if link not in result:
                result += link,
    return result
