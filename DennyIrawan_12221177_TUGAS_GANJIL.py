# DENNY IRAWAN
# NIM 12221177
# KELAS 12.1A.18
# TUGAS PERTEMUAN 10 LOGIKA DAN ALGORITMA
# SISTEM INFORMASI SURAKARTA

data = [1, 3, 9, 11, 15, 22, 29, 31, 48]
key = 3
awal = 1
akhir = len(data) + 1
ketemu = False
while (awal <= akhir) and not ketemu:
    tengah = int((awal + akhir) / 2)
    if key == data[tengah]:
        ketemu = True
        print('data', key, 'ditemukan diposisi', tengah+1)
    elif key < data[tengah]:
        akhir = tengah - 1
    else:
        awal = tengah + 1
if not ketemu:
    print('data tidak ditemukan')
