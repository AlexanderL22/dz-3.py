# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print(' ')
print('Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')
print(' ')
data = '2 3 5 9 3'.split()
data = list(map(int, data))
even=[(data[i]) for i in range(0, len(data)) if i%2 != 0]
print('Для списка - ', data, '\nЭлементы стоящие на нечётной позиции - ',even,'\nСумма которых равна - ',sum(even))