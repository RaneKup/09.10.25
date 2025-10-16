chose_figure = input('Напишите фигуру (квадрат, круг, треугольник, ромб, звезда, ботинок): ')
symbol_figure = input("выберите символ для фигуры: ")

n = int(input("Размер фигуры (не меньше 3): "))

def draw_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print(symbol_figure, end = ' ')
            else:
                print(" ", end = ' ')
        print()

def draw_boot(n):
    y = n
    x = n
    matrix = [[(' ') for i in range(y)] for j in range(x)]


    for i in range(n):
        matrix[i][n - i - 1] = symbol_figure
    for i in range(n):
        matrix[i][x - 2] = symbol_figure
    for i in range(n):
        matrix[i][x - 3] = symbol_figure
        for j in range(i):
            matrix[i][n - j - 1] = symbol_figure

    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()

if chose_figure == 'квадрат':
    draw_square(int(input('Напишите размер матрицы: ')))
elif chose_figure == 'ботинок':
    draw_boot(int(input('Напишите размер матрицы: ')))