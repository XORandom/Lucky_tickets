"""
Найти все счастливые билеты.
Сумма первой половины цифр равна сумме второй половине цифр.
Работает только с четным количеством цифр в билете.
"""

lucky_numbers_list = []
length_of_number = 4


def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n//10)


def find_lucky_numbers():
    cnt = 0
    for i in range(1, 10**length_of_number):
        left = i // (10**(length_of_number/2))  # Левая половина
        right = i % (10**(length_of_number/2))  # Правая половина
        if sum_of_digits(left) == sum_of_digits(right):
            cnt += 1
            lucky_numbers_list.append(i)
    return cnt


if __name__ == '__main__':
    count = find_lucky_numbers()
    print(lucky_numbers_list)
    print('Число билетов: ', count)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
