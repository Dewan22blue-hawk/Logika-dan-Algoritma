# matrix1 = [[7, 1], [4, 5]]
# matrix2 = [[2, 3], [2, 2]]
# for x in range(0, len(matrix1)):
#     for y in range(0, len(matrix1[0])):
#         print(matrix1[x][y], end=' '),
#     print('')
# print('')


# for x in range(0, len(matrix2)):
#     for y in range(0, len(matrix2[0])):
#         print(matrix2[x][y], end=' '),
#     print('')
# print('')


# matrix1 = [[7, 1], [4, 5]]
# matrix2 = [[2, 3], [2, 2]]
# for x in range(0, len(matrix1)):
#     for y in range(0, len(matrix1[0])):
#         print(matrix1[x][y] + matrix2[x][y], end=' '),
#     print('')
# print('')

# matrix1 = [[7, 1], [4, 5], [3, 6]]
# for x in range(0, len(matrix1)):
#     for y in range(0, len(matrix1[0])):
#         print(matrix1[x][y], end=' ')
#     print('')
# print('')

# for x in range(0, 2):
#     for y in range(0, 3):
#         print(matrix1[y][x], end=' ')
#     print('')
# print('')

# deklarasi matrik 4x4
matriks = ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0])
# isi matriks 4x4
for i in range(4):
    for j in range(4):
        if i <= j:
            matriks[i][j] = 1
        if i < j:
            matriks[i][j] = 4 - i
        if i > j:
            matriks[i][j] = 4 - i


# cetak bentuk matriks
for i in range(4):
    print(matriks[i])
