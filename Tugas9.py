# Denny Irawan
# 12221177
# 12.1A.18
# Sistem Informasi
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
