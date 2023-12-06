try:
    n = int(input("Введите натуральное число: "))
    divisors = []
    int(n)
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    if not divisors:
        print("Число ", n, "равно 0 и не имеет делителей")
    else:
        max_divisor = max(divisors)
        min_divisor = min(divisors)
        print("Список делителей числа ", n, ":", divisors)
        print("Максимальный делитель: ", max_divisor)
        print("Минимальный делитель: ", min_divisor)
except ValueError:
    print("Введенное значение не является натуральным числом.")
