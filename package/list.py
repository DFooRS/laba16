def product_list(products):
    """
    Вывод списка товаров
    """
    line = '+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20
    )
    print(line)
    print(
        '| {:^25} | {:^15} | {:^14} |'.format(
            "Товар",
            "Магазин",
            "Стоимость"
        )
    )
    print(line)

    for product in products:
        print(
            '| {:^25} | {:^15} | {:^14} |'.format(
                product.get('product', ''),
                product.get('shop', ''),
                product.get('cost', 0)
            )
        )
    print(line)