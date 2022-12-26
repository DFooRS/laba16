from package import add
from package import list
from package import select
from package import help
from package import error


def main():
    """
    Главная функция программы.
    """
    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            product = add.add_product()
            products.append(product)
            if len(products) > 1:
                products.sort(key=lambda item: item.get('shop', ''))

        elif command == 'list':
            list.product_list(products)

        elif command == 'select':
            sel_shop = input("Введите магазин: ")
            selected = select.select(products, sel_shop)
            list.product_list(selected)

        elif command == 'help':
            help.get_help()

        else:
            error(command)