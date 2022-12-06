
kode_baju = ''
ukuran = ''
try:
    while kode_baju != 'hop':

        kode_baju = input("Masukkan Kode Baju [SP/AD] : ")
        ukuran = input("Masukkan Ukuran Baju [X/XL] : ")
        if kode_baju == "SP" or kode_baju == "sp":
            merk = "SuperDry"
            if ukuran == "X" or ukuran == "x":
                harga = 50000
            elif ukuran == "XL" or ukuran == "xl":
                harga = 60000
            else:
                harga = 0
        elif kode_baju == "AD" or kode_baju == "ad":
            if ukuran == "X" or ukuran == "x":
                harga = 65000
            elif ukuran == "XL" or ukuran == "xl":
                harga = 70000
            else:
                harga = 0
        else:
            merk = "Anda Salah Input Kode Merk"
            harga = "harga tidak tahu karena ukuran salah"
            print(merk + harga)
        print("____________________")
        print("Merk Baju : "+(merk))
        print("Harga baju : Rp.", harga)

except ValueError:
    print('program exit')
