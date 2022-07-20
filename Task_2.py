#2- Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Посмотрели, что такое множество? 
# Вот здесь его не используйте.

import random

def rnd_list():
    start_list = []
    for i in range(10):
        start_list.append(random.randint(0,10))
    print('Start list is:  ', start_list)
    return start_list

result_list = []
start_list = rnd_list()
for item in start_list:
    if item in result_list:
        continue
    else:
        result_list.append(item)
print('Result list is: ', result_list)
