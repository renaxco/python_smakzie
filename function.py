def menu():
  print('==========================')
  print('     MENU GEOMETRI')
  print('--------------------------')
  print('1. Hitung Luas Lingkaran')

def calcSalary(salary):
  tunjangan = 10/100 * salary
  pajak = (salary + tunjangan) * 10/100
  return salary+tunjangan-pajak

add2 = lambda x,y: x+y
print(add2(1000,234324))

# buat function dari kasus berikut:
# 1. Luas Lingkaran
# 2. Keliling Lingkaran
# 3. Luas Permukaan Bola
# 4. Volume Bola
# 5. Luas Kubus
# 6. Volume Kubus

# PHI = 3.14 

# def CalcCircleArea(r):
#   return PHI * r * r

# function
def luasPersegi(s):
  return s * s

# lambda
luasPersegi = lambda s: s * s
kelilingPersegi = lambda s: 4 * s
luasPersegiPanjang = lambda p,l: p * l

print(luasPersegi(5))
print(luas(7))
print(luasPersegiPanjang(3,5))




