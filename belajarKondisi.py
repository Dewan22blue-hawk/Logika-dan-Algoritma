"""x = 5
y = 6
print("nilai x adalah", x)

x += 5
print("nilai setelah ditambah 5 adalah", x)

x *= 5
print("nilai setelah dikali 5 adalah ", x)

print(not (x > y))

x = ["apel", "jeruk"]
# pakai in dan not in
print("jeruk" in x)
print("rambutan" not in x)


x = 6
if (x == 3):
    # pembuatan statment setelah kondisi selain print kita juga bisa untuk membuat keputusan atau variabel
    keputusan = "selamat anda lulus"
elif x == 5:
    keputusan = "nilai sama"

else:
    print('yang kedua')

print(keputusan)

buah = ['jeruk', 'mangga', 'apel']
buah_dicari = input('buah apa yang anda cari : ')
if buah_dicari.lower() in buah:
    print('buah yang anda cari tersedia')
else:
    print('buah yang anda cari tidak ada')

ulang = 2
for i in range(ulang):
    print("data Ke - " + str(i+1))
    nama = input("Masukkan Nim anda : ")
    uts = int(input("Masukkan Nilai UTS anda :"))
    uas = int(input("Masukkan Nilai UAS : "))
    print("NIm anda adalah %s nilai UTS anda %i nilai UTS anda %i" %
          (nama, uts, uas))
    print("-------------------------------------\n")
print("Program Selesai")
"""
i = 1
while i < 6:
    print(i)
    i += 1
