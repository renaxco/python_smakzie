Buatlah function untuk menentukan bilangan ganjil dan genap

Buatlah lambda untuk menentukan apakah bilangan termasukan kelipatan 15 atau bukan

bilangan diinput oleh user, 
tampilkan hasilnya


8
7
"saya"
def ganjilGenap(bilangan):
    if int(bilangan) % 2 == 0:
        return 2
    else:
        return 3

kelipatan15 = lambda bilangan : print('Kelipatan 15') if int(bilangan) % 15 == 0 else print("Bukan kelipatan 15")

bilangan = input('Inputkan bilangan : ')

kalimat =  ganjilGenap(bilangan) * 10 - 230
teks = kelipatan15(bilangan)


def kecepatan(v,t):
    return v*t

v = float('V : ')
t = float('t : ')

print(kecepatan(v,t))