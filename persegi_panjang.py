# p = 3
# l = 7
# L = p * l
# print(L)

# r = 14
# PHI = 3.14
# L = PHI * r ** 2
# print(L)

# Volume tabung = PHI * r * r * t
# Luas Permukaan tabung = 2 x (2 x PHI x r) + (2 x PHI x r x t)

PHI = 3.14
r = float(input('Masukkan jari-jari : '))
t = float(input('Masukkan tinggi    : '))
volume_tabung = PHI * r ** 2 * t
luas_permukaan = 2 * (2 * PHI * r) + (2 * PHI * r * t)
print('Volume \t\t: ', volume_tabung)
print('Luas permukaan \t: ', luas_permukaan)

# volume bola = 4/3 x PHI x r x r x r