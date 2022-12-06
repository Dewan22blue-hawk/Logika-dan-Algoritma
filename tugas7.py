wkh = [" ", "PETIK", "PLOMPONG", "GUNUNG", "CAWANG", "KANTONG", "KEROK"]
wkm = [" ", "RATU", "DIMPIL", "CIWIR", "GUNDUL", "BABI", "TENGKRANG"]
no = int(input('Masukkan angka kartu [1-6]   : '))
wrn = input("Masukkan warna kartu [H/M] : ")
if wrn == "h" or wrn == "H":
    print(wkh[no])
elif wrn == "m" or wrn == "M":
    print(wkm[no])
else:
    print(
        'kode warna yang anda inputkan salah, kode warna yang terdaftar ialah [H/h, M/m]')
