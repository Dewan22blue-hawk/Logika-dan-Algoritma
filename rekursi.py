def ram(batas, i=2):
    print(i)

    if (i < batas):
        ram(batas, i * 2)


isi = int(input("masukkan angka maksimal : "))
ram(isi)
