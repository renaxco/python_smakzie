A = int(input('Masukkan Angka A : '))
B = float(input('Masukkan Angka B : '))


# cari terbaik ke-3
C = A
A = B
B = C

#car terbaik ke-2
A = A + B   
B = A - B   
A = A - B   

print('A = '+ str(A))
print('B = '+ str(B))