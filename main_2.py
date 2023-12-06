input_text = input("Введите строку текста: ")

words = input_text.split()

longest_word = ""
digit_sum = 0
inverted_string = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
    inverted_word = ""
    for char in word:
        if char.islower():
            inverted_word += char.upper()
        elif char.isupper():
            inverted_word += char.lower()
        else:
            inverted_word += char
        if char.isdigit():
            digit_sum += int(char)

    # for char in inverted_word:
    #     if char.isdigit():
    #         digit_sum += int(char)
    inverted_string += inverted_word + " "

print("Самое длинное слово: ", longest_word)

print("Сумма цифр в строке: ", digit_sum)

print("Инвертированная строка: ", inverted_string)
