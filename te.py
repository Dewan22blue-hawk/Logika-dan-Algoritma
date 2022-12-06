thn = 2020
js = 15000000
jj = 12000000
print('Tahun            solo                jogja')
while js > jj:
    print(thn, '  ', js, '  ', jj)
    js = js+0.1*js
    jj = jj+0.12*jj
    thn += 1
else:
    print(thn, '  ', js, '  ', jj)
