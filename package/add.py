def add_product():
    """
    Ввод информации о товарах.
    """
    prod = input("Введите название товара: ")
    shop = input("Введите название магазина: ")
    cost = float(input("Введите стоимость товара: "))

    return {
        'product': prod,
        'shop': shop,
        'cost': cost
    }
