def pangkat(n, p):
    h = 1
    for a in range(1, p+1):
        h = h*n
    return h


# program utama
n = int(input("Masukkan angka : "))
p = int(input("Pangkat berapa : "))
print(n, ' pangkat ', p, '=', pangkat(n, p))
