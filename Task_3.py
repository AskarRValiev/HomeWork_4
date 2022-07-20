#3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#README: можно было конечно сократить число функций и совместить в одну несколько, но я подумал, что пусть лучше
#каждая функция выполняет свою уникальную работу - на будущее. 

def is_simple(n: int):
    '''
    Принимает на вход целое число, если число простое, возвращает True, в противном случае False.
    '''
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def simple_dividers(n: int):
    '''
    Принимает на вход целое число и возвращает список список простых чисел входящих в его состав - возможные 
    простые множители.
    '''
    simp_divider_list = []
    for i in range(2, n+1):
        if(is_simple(i) == True):
            simp_divider_list.append(i)
    return simp_divider_list


def dividers(n: int, simp_divider_list: list):
    '''
    Принимает на вход целое число и список простых чисел, входящих в его состав.
    Возвращает список простых множителей введенного числа.
    '''
    divider_list = []
    for i in simp_divider_list:
        if n % i == 0:
            divider_list.append(i)
    return divider_list


n = input('Введите целое положительное число: ')
if n.isdigit() == False:
    print('Введенные данные не соответствуют условиям')
    exit()

print(dividers(int(n), simple_dividers(int(n))))
