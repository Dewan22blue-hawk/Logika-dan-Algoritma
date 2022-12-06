# program sengaja saya beri while agar bisa mengembalikan inputan saat inputan salah
no = ''
wk = ''
try:
    while no != 'quit':
        no = int(input('Masukkan angka kartu [1-6]   : '))
        wk = input('Masukkan kode warna kartu [H/h, M/m] : ')
        if no in range(1, 7):
            if wk == "h" or wk == "H":
                if no == 1:
                    print('PETIK')
                elif no == 2:
                    print('PLOMPONG')
                elif no == 3:
                    print('GUNUNG')
                elif no == 4:
                    print('CAWANG')
                elif no == 5:
                    print('KANTONG')
                elif no == 6:
                    print('KEROK')
# kondisi bersarang kompleks
            elif wk == "m" or wk == "M":
                if no == 1:
                    print('RATU')
                elif no == 2:
                    print('DIMPIL')
                elif no == 3:
                    print('CIWIR')
                elif no == 4:
                    print('GUNDUL')
                elif no == 5:
                    print('BABI')
                elif no == 6:
                    print('TENGKRANG')

            else:
                print('Warna kartu yang anda inputkan salah!')

        else:
            print('Angka kartu yang anda Inputkan salah!')

except ValueError:
    print('program exit')
