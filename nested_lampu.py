# is_on = input('Apakah lampu nyala (Y/N)? ')

# if(is_on.upper() == 'Y' ):
#     warnaLampu = input('Apa warna lampunya (Merah/Kuning/Hijau) ? ')
#     if(warnaLampu.lower() == 'merah'): keterangan = 'Berhenti'
#     elif(warnaLampu.lower() == 'kuning'): keterangan = 'Siap-siap'
#     elif(warnaLampu.lower() == 'hijau'): keterangan = 'Jalan'
#     else: keterangan = 'warna lampu salah!'
# else:
#     keterangan = 'Jalan terus'

# print(keterangan)

bilangan = int(input('Masukkan bilangan : '))

# ternary
keterangan = 'genap' if bilangan % 2 == 0 else 'ganjil'

# konvesional if
if bilangan % 2 == 0: keterangan = 'genap'
else: keterangan = 'ganjil'

print('Termasuk bilangan '+keterangan)



Tugas:
1. Buatlah program untuk menentukan apakah bilangan termasuk kelipatan 11