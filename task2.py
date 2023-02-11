# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

a = int(input('Введите а: '))
b = int(input('Введите b: '))
def exponentiation(a, b):
    if b > 1:
       return (a * exponentiation(a, b - 1))
    return a
print (exponentiation(a, b))
