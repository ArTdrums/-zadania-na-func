'''

Написать функцию которая принимает 1 аргумент (целое число) и определяет является ли данное число простым.
Число называется простым если оно делится на 1 и на само себя
Если число простое то выводится соответствующее сообщение что число является простым.
'''


def fuck(n):
    for i in range(2, x):
        if x % i == 0:
            print('Число не простое')
            break
        else:
            print('Число простое')
            break


x = int(input())
fuck(x)
