def select_store_id(goods):
    """Selects a store identifier and puts it in a shared object.
    :param goods: an object with goods in it there is a field stores
    :return: all id stores
    """
    store_id = ()
    if goods['availability']:
        for item in goods['stores']:
            store_id += item.get('id_store'),
    return store_id


