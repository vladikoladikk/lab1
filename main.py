try:
    sum = 0
    while True:
        inputNum = input("Input the number: ")
        if (inputNum.isalpha() or inputNum < "0" or inputNum == "0"):
            print("Incorrect value of the number.")
        else:
            break
    # for i in str(input):
    #     if (int(i) % 2 == 0):
    #         sum += int(i)
    #     elif(i == str(a)):
    #         print("0")
    fakeNum = int(inputNum)
    while (fakeNum):
        lastDigit = fakeNum % 10
        if (lastDigit % 2 == 0):
            sum += lastDigit
        fakeNum //= 10
    print(f'The sum is: {sum}')
except ValueError:
    print("Введенное значение не является натуральным числом.")


