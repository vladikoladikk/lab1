
toy_store = {
    'Мяч': ['\nпокрышка, камера, подкладка', 500, 10],
    'Кукла': ['\nвысота куклы: 26 см; рекомендуемый возраст – 4-5 лет, 6-8 лет; размер упаковки: 33х6х22 см; производитель: Mattel', 1000, 5],
    'Пазл': ['\nколичество частей: 500; материал: картон; страна производства: Россия', 800, 7],
    'Машинка': ['\nвозраст: от 3-х лет; материал: пластик, металл; страна производства: Россия', 600, 12],
    'Конструктор': ['\nбренд: LEGO; количество деталей: 345; чтрана происхождения: Чехия', 1500, 8]
}


for toy, info in toy_store.items():
    print(f"{toy} : {info[0]}")
