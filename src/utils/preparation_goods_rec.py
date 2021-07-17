from tqdm import tqdm


def preparation_goods_rec(goods):
    """Prepare products for insertion into the database.
    :param goods: Data received from the site
    :return: Data ready for writing to database tables
    """
    _temp = []
    _keys = []
    result = []
    # Attach a product to a specific store
    for item in goods:
        if item.get('availability'):
            temp_data = (None, item.get('product_code'), item.get('vendor_code'),
                         item.get('name'), item.get('link_product'),
                         item.get('link_picture'), item.get('online_price'),)
            for store in item.get('stores'):
                id_store = store.get('id_store')
                temp_data += store.get('address'), store.get('price')
                _temp.append({id_store: temp_data})
                temp_data = temp_data[:len(temp_data) - 2]
    # Collect keys (store identifier) from the object
    for item in _temp:
        current_key = list(item.keys())[0]
        if current_key not in _keys:
            _keys.append(current_key)
    # Packing goods into the store. Prepares an object for bids in a db table.
    for key in tqdm(_keys, desc='Necessary preparations before recording'):
        data = {key: []}
        for item in _temp:
            for current_key, current_value in item.items():
                if current_key == key:
                    data[key].append(current_value),
        result.append(data)
    return result
