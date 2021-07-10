def filler(element: list, amount: int):
    """Fast large filling with elements.
    :param element: what to fill
    :param amount: how many
    :return:
    """
    result = []
    piece = len(element)
    box_element = [element for _ in range(amount // piece + 1)]
    for item in box_element:
        result.extend(item)
    return result[:amount]

