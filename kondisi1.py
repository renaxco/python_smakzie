nilai = int(input("Inputkan nilai\t\t: "))
nilai_sikap = input('Inputkan nilai sikap\t: ')
nilai_ulangan = int(input('Inputkan nilai ulangan\t: '))

if nilai >= 75 and nilai_sikap == 'A' or 'B' and nilai_ulangan >= 60:
  print('Lulus')
else:
  print('Tidak Lulus')

# Standar Lulus:
# 1. Nilai > =  75
# 2. Nilai sikap harus A atau B
# 3. Nilai ulangan > = 60

# SHORTHAND IF (ternary operator) DAN MOD
bilangan = 9
if bilangan % 2 == 1:
  print('Bilangan ganjil')
else:
  print('Bilangan genap')

hasil = 'Bilangan ganjil' if bilangan % 2 == 1 else 'Bilangan genap'
print(hasil)

OPERATOR ARITMATIKA
+ - * /  %
10 % 3 = 1
4 % 2 = 0
12 % 10 = 2
1000 % 3 = 1
100 % 4 = 0
100 % 30 = 10
27 % 20 = 7
30 % 9 = 3
33 % 6 = 3
37 % 8 = 5
40 % 4 = 0
45 % 4 = 1

# buat variable username diisi "admin" password diisi "nimda123"
# buatlah kondisi apabila user dan password benar atau salah

# gerbang logika AND
# gerbang logika OR

# true and true  = true
# true and false = false
# false and true = false
# false and false = false

# true or true  = true
# true or false = true
# false or true = true
# false or false = false