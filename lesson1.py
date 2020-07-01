class Matrix():
    def __init__(self, matr1, matr2):
        self.matr1 = matr1
        self.matr2 = matr2
        self.matr = 1

    def __add__(self):
        matr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.matr = matr

        for i in range(len(self.matr1)):
            for x in range(len(self.matr2[i])):
                matr[i][x] = self.matr1[i][x]+self.matr2[i][x]
        for i in range(len(matr)):
            print('\n', matr[i][0], matr[i][1], matr[i][2], end='')

    def __str__(self):

        if self.matr != 1:
            print('\n', '\n', 'Матрица после сложения:')
            for i in range(len(self.matr)):
                print('\n', self.matr[i][0], self.matr[i][1], self.matr[i][2], end='')
        else:
            print('\n', 'Имеем две матрицы для сложения:', '\n', f'{self.matr1}', 'и', f'{self.matr2}')


a = Matrix([[3, 5, 3], [4, 5, 2], [1, 2, 1]], [[1, 4, 4], [3, 3, 3], [2, 6, 0]])

print(a.matr1)
print(a.matr2)
a.__add__()
a.__str__()
# Matrix = [[3, 5, 3], [4, 5, 2], [1, 2, 1]]#, [[1,4,4], [3,3,3], [2,6,0]])
# print('\n', Matrix[0][0], Matrix[0][1], Matrix[0][2], '\n', Matrix[1][0], Matrix[1][1], Matrix[1][2], '\n', Matrix[2][0], Matrix[2][1], Matrix[2][2])
# print("".join(str(Matrix[2])))
# print(((for i in Matrix[i][len(i)], '\n') for x in Matrix[len(x)][x])
# for i in range(len(Matrix)):
#     print('\n', Matrix[i][0], Matrix[i][1], Matrix[i][2], end='')