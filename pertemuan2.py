toko = (" TOKO MAINAN ANAK ")
print(toko.center(100, "*"))

nama = str(input("Masukkan Nama Pembeli : "))
kode = str(input("Masukkan Kode Mainan  : "))
harga = int(input("Masukkan Harga        : "))
jumlah = int(input("Masukkan Jumlah Beli  : "))
total = harga * jumlah

print("\n=============================================\n")

print("Nama Pembeli = ", nama)
print("Kode Mainan  = ", kode)
print("Harga        = ", harga)
print("Jumlah Beli  = ", jumlah)
print("Total        = ", total)
if kode == "TEST-2022":
    print('kode kupon berhasil!, anda mendapatkan diskon 20%')

    diskon = total - (total * 20/100)

    print("Besar uang yang harus dibayar setelah diskon = ", diskon)
else:
    print(total)
