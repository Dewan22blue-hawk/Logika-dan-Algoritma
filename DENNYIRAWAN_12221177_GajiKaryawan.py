# Program menentukan gaji karyawan
# Tugas Pemrograman Dasar Pertemuan 4
# DENNY IRAWAN
# SISTEM INFORMASI
# 12.1A.18

nama = str(input("Nama Karyawan : "))
# Gaji pokok
gp = 300000

# Tunjangan golongan jabatan
gol = int(input("Golongan Jabatan[1/2/3] : "))
if gol == 1:
    bj = gp * (5/100)
elif gol == 2:
    bj = gp*(10/100)
elif gol == 3:
    bj = gp*(15/100)
else:
    print("Golongan Yang Anda Masukkan Salah")
    exit()
# Tunjangan pendidikan
pendidikan = input("Pendidikan [SMA/D1/D3/S1] : ")
if pendidikan == "SMA":
    bp = gp*(2.5/100)

elif pendidikan == "D1":
    bp = gp*(5/100)

elif pendidikan == "D3":
    bp = gp*(20/100)

elif pendidikan == "S1":
    bp = gp*(30/100)
else:
    print("Golongan Pendidikan Yang Anda Masukkan Salah")
    exit()
# Bonus/honor lembur
jam = int(input("Jumlah Jam Kerja : "))
if jam > 8:
    bl = (jam - 8) * 3500
else:
    bl = 0

# Hitung Total gaji yang diterima
total = gp + bj + bp + bl

# Cetak Outputnya

print("\n-----------------------------------------")
print("---------PT. DINGIN ABADI----------------")
print("\nKaryawan yang bernama", nama.upper())
print("Honor yang diterima :")
print("\tTunjangan Jabatan    Rp.", bj)
print("\tTunjangan Pendidikan Rp.", bp)
print("\tHonor Lembur         Rp.", bl)
print("Gaji Pokok                   Rp.", gp)
print("\t\t\t\t---------+")
print("Total Gaji            \t====>Rp.", total)
print("------------ TERIMA KASIH ---------------")
print("-----------------------------------------\n")
