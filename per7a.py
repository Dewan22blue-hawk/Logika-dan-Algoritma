"""print(ord('a'))
print(ord('Z'))
print(chr(88))
"""
kk = str(input('input kata/kalimat : '))
jk = len(kk)
for a in range(1, jk+1):
    c = ord(kk[a-1]) - 32
    if c < 97 and c < 122:
        print(chr(c), end='')
    else:
        print('salah input harus kecil semua')
print('')
