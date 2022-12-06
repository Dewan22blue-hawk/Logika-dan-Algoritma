import tkinter as tk
a = int(input("suku pertama ="))
b = int(input("Beda ="))
rangesu = int(input('range ='))


index = 1
jumlhsu = 0

while index <= rangesu:
    print(str(a), end=' ')
    jumlhsu += a
    a += b
    index += 1
print("\n jumlah deret " + str(jumlhsu))
