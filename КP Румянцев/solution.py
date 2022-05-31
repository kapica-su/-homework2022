                                                    #######################
with open('input.txt', 'r') as INPUT:               #Считываем данные с файла
    N = int(INPUT.readline())                       #-Количество городов
    array = []                                      #
    for i in range(N*(N+1)//2):                     #Собираем массив из чисел
        array.append(int(INPUT.readline().strip())) #
    M = len(array.copy())                           #-Количество строк
print("Количество строк:", M)                       #
print("Количество городов:", N)                     #######################


                                                    #######################
n = 2                                               #Преобразование массива
new_new_array = []                                  #
while n <= N+1:                                     #-Цикл с условием 
    new_array = []                                  #
    for i in range(1,n):                            #-Цикл уменьшения длины массива
        new_array.append(array[-1])                 #
        array.pop(-1)                               #-Удаление элемента старого массива
    new_array.reverse()                             #-Разворот нового подмассива
    new_new_array.append(new_array)                 #-Добавляем в подмасив в полный НОВЫЙ массив
    n += 1                                          #-Инкремент переменной n
new_new_array.reverse()                             #-Разворот всего нашего нового массива
array = new_new_array                               #
print("Длины возможных путей:", array)              ######################



                                                    #####################################
def func(array, x):                                 #Функция, которая, получив элемент находит...
    if x[1] > len(array):                           #...длины последовательностей его путей
        print(x[1], len(array))                     #-Проверка на отсутствие проблем
        print('it\'s problem!')                     #
    elif x[1] == len(array):                        #-Условие выхода из рекурсии
        return x[0]                                 #
    else:                                           #
        List = []                                   #
        for i in range(len(array[x[1]])):           #-Перебор элементов возможных путей
            List.append(x[0] + func(array, [array[x[1]][i],x[1]+1+i]))
        return min(List)                            #Поиск наименьшей стоимости поездки для переданного старта
                                                    #####################################


counter = 0                                         ######################
List = []                                           #Основное тело кода
for element in array[0]:                            #-Перебор точек старта
    counter += 1                                    #-Счётчик переходов
    a = func(array, [element, counter])             #-Запуск функции с переданными "старт"-значениями
    List.append(a)                                  #-Добавление в список наименьших путей от разных стартов
minCost = min(List)                                 #-Меньший по стоимости путь
print('Наименьшая стоимость пути:', minCost)        ######################


                                                    #######################
with open('output.txt', 'w') as output:             #Запись данных в файл
    output.write(str(minCost))                      #######################

