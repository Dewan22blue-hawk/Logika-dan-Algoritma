'''
from tabulate import tabulate
data = [['kolom-1', 'kolom-2', 'kolom-3'],
        [1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
print(tabulate(data, headers='firstrow'))

datasatu = data[1]
datadua = data[2]
datatiga = data[3]
dataempat = data[4]
print('baris pertama, kolom pertama ialah {}'.format(datasatu[0]))
print('baris pertama, kolom kedua ialah {}'.format(datasatu[1]))
print('baris pertama, kolom ketiga ialah {}'.format(datasatu[2]))
print('baris ketiga, kolom ketiga ialah {}'.format(datatiga[2]))
print('baris pertama, kolom pertama ialah {}'.format(dataempat[0]))

list = [['kolom 1', 'kolom 2', 'kolom 3'],
        [1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
list1 = list[1]
list2 = list[2]
list3 = list[3]
list4 = list[4]
print('baris pertama, kolom pertama ialah \n{}'.format(list1[0]))
print('baris pertama, kolom kedua ialah \n{}'.format(list1[1]))
print('baris pertama, kolom ketiga ialah \n{}'.format(list1[2]))
print('baris pertama, kolom ketiga ialah \n{}'.format(list3[2]))
print('baris pertama, kolom pertama ialah \n{}'.format(list4[0]))
'''


list_nim = []
list_uts = []
list_uas = []
list_total = []
ulang = 2
for i in range(ulang):
    print("data Ke - " + str(i+1))
    list_nim.append(input("Masukkan Nim anda : "))
    list_uts.append(int(input("Masukkan Nilai UTS anda :")))
    list_uas.append(int(input("Masukkan Nilai UAS : ")))
    # proses`
for i in range(ulang):
    list_total.append((list_uas[i] + list_uts[i]) / 2)
# Cetak
print("=============================================================")
print("Nim      Nilai Uts            Nilai UAS                 Total")
print("=============================================================")
for i in range(ulang):
    print("%s \t %i \t\t %i \t\t\t %i" %
          (list_nim[i], list_uts[i], list_uas[i], list_total[i]))
    print("=============================================================")
