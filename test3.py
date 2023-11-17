Buatlah function untuk menghitung volume tabung 
  (phi * r * r * t)
Buatlah lambda untuk menghitung luas permukaan tabung
  (2 x (phi * r * r)) + ((phi * 2 * r) * t) 

Inputkan dari user dan tampilkan hasil volume dan luas

PHI = 3.14
def volumeTabung(r, t):
  return PHI * r * r * t

luasTabung = lambda r,t : (2 * (PHI * r * r)) + ((PHI * 2 * r) * t)

r = float(input('Jari - jari : '))
t = float(input('Tinggi : '))

print(volumeTabung(r,t))
print(luasTabung(r,t))

input('')

Buat function mencari bilangan terbesar dan terkecil dari 3 variable

