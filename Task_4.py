#4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# немного подправил входной файл, приблизил к канонам ))


def define_digits(s: list):
    '''
    Принимает на вход список.
    Находит слова с цифрами, заносит их в вспомогательный список, удаляет слова содержащиеся в вспомогательном списке
    из полученного списка и возвращает исправленный список.
    '''
    aux_list = []
    for i in s:
        for j in i:
            if j.isdigit():
                aux_list.append(i)
 
    for i in aux_list:
        try:
            s.remove(i)
        except ValueError:
            continue
    return s


with open('poem.txt', 'r', encoding = 'utf-8') as data:
    s = data.read().split(' ')
define_digits(s)

with open('new poem.txt', 'w', encoding ='utf-16') as wrt:
    wrt.write(str(s))

                
           
            
           
            
