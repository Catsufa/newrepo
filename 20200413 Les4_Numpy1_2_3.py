
import numpy as np

print('Задача1. Сумма ряда 0 - 100 =', np.array(sum(range(100)))) # Задание 1. Сумма ряда 0-100

x = int(input('Задача2. Введите число для расчета сумма ряда от 0 до Ваше число: ')) # Задание 2. Сумма ряда 0-input()
print ('Задача2. Ответ. Сумма ряда 0 -', x, '=', np.array(sum(range(x))))

y = np.random.randint(0, 1000, 100)
z = sum(y) / len(y)

print ('Задача3. Среднее среди 100 случайных чисел',y, ' = ',z)
# print('Сумма раяда от 0 до Ваше число составит') 


