my_dict = {'a': 12, 'b': 13, 'c': 56, 'd': 400, 'e': 58, 'f': 20}
sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
top_three = sorted_items[:3]
for key, value in top_three:
    print(f'Ключ: {key}, Значение: {value}')
