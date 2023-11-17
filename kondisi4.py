pengetahuan = float(input('Nilai Pengetahuan : '))
keterampilan = float(input('Nilai keterampilan : '))
sikap = input('Nilai sikap : ')

if pengetahuan >= 75 and keterampilan >= 80 and (sikap.lower() == 'a' or 'b'):
    print('Anda Lulus')
else:
    print('Anda Belum Lulus')


Lampu merah : berhenti
lampu kuning: bersiap-siap
lampu hijau : jalan


Cari angka terbesar dan terkecil dari 3 angka
Misal:
Angka 1 : 809
Angka 2 : 740
Angka 3 : 444
Angka terbesar 809
Angka terkecil 444

angka1 = int(input('Angka 1 : '))
angka2 = int(input('Angka 2 : '))
angka3 = int(input('Angka 3 : '))

terkecil = terbesar  = 0

# mencari terbesar 
if(angka1 > angka2 and angka3): terbesar = angka1
elif(angka2 > angka1 and angka3): terbesar = angka2
else: terbesar = angka3

# mencari terkecil 
if(angka1 < angka2 and angka3): terkecil = angka1
elif(angka2 < angka1 and angka3): terkecil = angka2
else: terkecil = angka3

print('Angka terbesar : '+terbesar)
print('Angka terkecil : '+terkecil)