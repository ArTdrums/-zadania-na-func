'''Используя лямбда выражение и функцию filter создать программу,
которая из введенной строки создает список, содержащий только цифровые символы.
'''
a = input()
s = list(filter(lambda a: a.isdigit(), a))
print(s)
