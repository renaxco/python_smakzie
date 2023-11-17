# range(initialization, condition, iteration)
#for x in range(1,11,3):
#    print("Hello ",x)

nama = 'tek1'
nama += ' tek2'
# print(nama)

# angka = ''
jumlah = 0
for i in range(10,60, 10):
  angka += str(i)
  angka += " + " if i < 50 else ""
  jumlah += i
print(angka, " = ", str(jumlah))

teks = ''
for x in range(5):
  for a in range(1,6):
      teks += 'a' + ' '
  teks += '\n'

print(teks)

# 1 2 3 4 5

