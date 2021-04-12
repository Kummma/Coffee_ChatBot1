def print_message():
    print("Извините, я не понимаю. Пожалуйста, введите Ваш ответ в соответсвии с вариантами.")


# Получаем размер напитка
def get_size():
    res = input("Какой размер напитка Вы предпочитаете? \n[a] Маленький \n[b] Средний \n[c] Большой \n> ")

    if res == "a":
        return "маленький"
    elif res == "b":
        return "средний"
    elif res == "c":
        return "большой"
    else:
        print_message()
        return get_size()


# Заказ американо
def order_americano():
    while True:
        res = input("[a] Обычный американо "
                    "\n[b] Айс американо "
                    "\n[c] Двойной американо \n>")

        if res == "a":
            return "обычный американо"
        elif res == "b":
            return "айс американо"
        elif res == "c":
            return "двойной американо"
        print_message()
        return order_americano()


# Заказ мокко
def order_mocha():
    while True:
        res = input(
            "Не желаете попробовать наше сезонное предложение - Орео-Мокко? "
            "\n[a] Конечно "
            "\n[b] Может в следующий раз \n>")

        if res == "a":
            return "орео-мокко"
        elif res == "b":
            return "мокко"

        print_message()
        return order_mocha()


# Заказ латте
def order_latte():
    res = input("На каком молоке сделать Латте? "
                "\n[a] Соевое молоко "
                "\n[b] Миндальное молоко "
                "\n[c] Обезжиренное молоко \n> ")

    if res == "a":
        return "латте на соевом молоке"
    elif res == "b":
        return "латте на миндальном молоке"
    elif res == "c":
        return "латте на обезжиренном молоке"
    else:
        print_message()
        return order_latte()
