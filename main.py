#Указание файлов ввода и вывода в программе
input = open('input.txt', 'r', encoding = 'utf-8')
output = open('output.txt', 'w', encoding = 'utf-8')

N = int(input.readline()) #Забираем величину высоты и ширины матрицы
main = 0 #Главная диагональ
indirect = 0 #Косвенная диагональ

#Цикл, перебирающий строки матрицы и высчитывающий диагональки
for i in range(N): 
    strings = list(map(int, input.readline(-2).split(' ')))
    main += int(strings[i])
    indirect += int(strings[N-i-1])

output.write(str(main) + ' ' + str(indirect)) #Вывод данных в файл

#Закрытие файлов по окончанию работы с ними
input.close()
output.close()
