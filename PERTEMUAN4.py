pembeli = input('Input Nama Pembeli : ')
no_hp = input('Masukkan No.Handphone : ')
jurusan = input('Input Jurusan [SBY/BL/LMP] : ')
if jurusan == "SBY":
    namajurusan = "Surabaya"
    harga = 300000
elif jurusan == "BL" or jurusan == "bl":
    namajurusan = "Bali"
    harga = 350000
else:
    namajurusan = "Lampung"
    harga = 500000

jumlah = int(input('Masukkan Jumlah Beli : '))

if jumlah >= 3:
    potongan = (jumlah*harga) * 0.1
else:
    potongan = 0
total = (jumlah*harga)-potongan

print("___________________________________________")
print("            PENJUALAN TIKET BUS            ")
print("___________________________________________")
print("Nama Pembeli             : "+str(pembeli))
print("Kode Jurusan yang dipilih: "+str(jurusan))
print("Nama Kota Tujuan         : "+str(namajurusan))
print("Harga                    : ", +(harga))
print("Jumlah Beli              : ", +(jumlah))
print("___________________________________________")
print("potongan yang didapat    : ", +(potongan))
print("Total Bayar              : ", +(total))
ubay = int(input("Masukkan Uang Bayar      : "))
uangkembali = ubay-total
print("Uang Kembali             : ", +uangkembali)
