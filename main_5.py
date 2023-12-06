
toy_store = {
    'Мяч': ['\nпокрышка, камера, подкладка', 500, 10],
    'Кукла': ['\nвысота куклы: 26 см; рекомендуемый возраст – 4-5 лет, 6-8 лет; размер упаковки: 33х6х22 см; производитель: Mattel', 1000, 5],
    'Пазл': ['\nколичество частей: 500; материал: картон; страна производства: Россия', 800, 7],
    'Машинка': ['\nвозраст: от 3-х лет; материал: пластик, металл; страна производства: Россия', 600, 12],
    'Конструктор': ['\nбренд: LEGO; количество деталей: 345; чтрана происхождения: Чехия', 1500, 8]
}


def show_description():
    print("\nОписание игрушек:")
    for toy, info in toy_store.items():
        print(f"{toy}: {info[0]}")


def show_price():
    print("\nЦены на игрушки:")
    for toy, info in toy_store.items():
        print(f"{toy}: {info[1]} рублей")


def show_quantity():
    print("\nКоличество игрушек в магазине:")
    for toy, info in toy_store.items():
        print(f"{toy}: {info[2]} штук")


def show_all_info():
    print("\nПолная информация о игрушках:")
    for toy, info in toy_store.items():
        print(f"{toy}: {info[0]}, Цена: {info[1]} рублей, Количество: {info[2]} штук")


def purchase():
    total_cost = 0
    while True:
        toy_name = input("\nВведите название игрушки для покупки (или 'n' для выхода): ").capitalize()
        if toy_name == 'N':
            break
        if toy_name in toy_store:
            try:
                quantity = int(input(f"Введите количество {toy_name}: "))
                if 0 < quantity <= toy_store[toy_name][2]:
                    cost = quantity * toy_store[toy_name][1]
                    total_cost += cost
                    toy_store[toy_name][2] -= quantity
                    print(f"Вы купили {quantity} {toy_name}(ов) за {cost} рублей.")
                else:
                    print(f"Недостаточно товара {toy_name} на складе.")
            except ValueError:
                print("Введите корректное число.")
        else:
            print("Такой игрушки нет в магазине. Попробуйте еще раз.")
    print(f"Общая стоимость покупок: {total_cost} рублей")


while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        show_description()
    elif choice == '2':
        show_price()
    elif choice == '3':
        show_quantity()
    elif choice == '4':
        show_all_info()
    elif choice == '5':
        purchase()
    elif choice == '6':
        print("До свидания! Спасибо за покупки.")
        break
    else:
        print("Пожалуйста, введите действие из меню (1-6).")
