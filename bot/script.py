from utils import print_message, get_size, order_latte, order_mocha, order_americano


def coffee_bot():
    print("Добро пожаловать в кафе!")

    order_drink = "да"
    drinks = []

    while order_drink == "да":
        drink_type = get_drink_type()
        size = get_size()

        drink = "{} {}".format(size, drink_type)
        print("Ваш заказ {}.".format(drink))
        drinks.append(drink)

        while True:
            order_drink = input("Что-нибудь еще? (да/нет) \n> ")

            if order_drink == "да" or order_drink == "нет":
                break

    print("Вы заказали:")

    for drink in drinks:
        print("-", drink)

    name = input("Как вас зовут? \n> ")
    print("Спасибо, {}! Ваш заказ скоро будет готов.".format(name))


def get_drink_type():
    res = input("Какой напиток вы хотите заказать? \n[a] Американо \n[b] Мокко \n[c] Латте \n> ")

    if res == "a":
        return order_americano()
    elif res == "b":
        return order_mocha()
    elif res == "c":
        return order_latte()
    else:
        print_message()
        return get_drink_type()


coffee_bot()
