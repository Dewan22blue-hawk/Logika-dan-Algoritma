# Program menentukan gaji karyawan
# Tugas Pemrograman Dasar Pertemuan 4
# DENNY IRAWAN
# SISTEM INFORMASI
# 12.1A.18


# Membuat layar output pertama
print("    \tGEROBAK FRIED CHICKEN DEWAN ")
print("===========================================")
print("   \tKode Jenis Potong Harga")
print("===========================================")
print("D     Dada         2500")
print("P     Paha         2000")
print("S     Sayap        1500")

# Membuat Variabel input dan list
banyak_jen = int(input("Banyak Jenis : "))
kode_pot = []
banyak_pot = []
jenis_pot = []
harga = []
jumlah = []

# Membuat loop dan kondisi serta menambahkan anggota ke dalam list (append) variabel list
i = 0
while i < banyak_jen:
    print("Jenis Ke - ", i+1)
    kode_pot.append(input("Kode Potong [D/P/S] : "))
    banyak_pot.append(int(input("Banyak Potong : ")))
# Pengkondisian
    if kode_pot[i] == "D" or kode_pot[i] == "d":
        jenis_pot.append("Dada")
        harga.append("2500")
        jumlah.append(banyak_pot[i]*int("2500"))
    elif kode_pot[i] == "P" or kode_pot[i] == "p":
        jenis_pot.append("Paha")
        harga.append("2000")
        jumlah.append(banyak_pot[i]*int("2000"))
    elif kode_pot[i] == "S" or kode_pot[i] == "s":
        jenis_pot.append("Sayap")
        harga.append("1500")
        jumlah.append(banyak_pot[i]*int("1500"))
    else:
        jenis_pot.append("Kode Salah")
        harga.append("0")
        jumlah.append(banyak_pot[i]*int("0"))
    i = i + 1

# Membuat layar output

print("          GEROBAK FRIED CHICKEN DEWAN ")
print("===========================================")
print("No   Jenis     Harga        Banyak    Jumlah")
print("     Potong    Satuan       Beli      Harga ")
print("===========================================")

# Perulangan untuk menampilkan hasil output yang diinputkan menggunakan string method manipulation, squwnce
a = 0
while a < banyak_jen:
    print("%i    %s       %s        %i         %i" %
          (a+1, jenis_pot[a], harga[a], banyak_pot[a], jumlah[a]))
    a = a + 1

jumlah_bayar = int(input("Jumlah Bayar Rp. "))
pajak = jumlah_bayar * 0.1
total_bayar = jumlah_bayar + pajak
print("Pajak 10 % Rp. ", pajak)
print("Total Bayar Rp. ", total_bayar)
