totalBelanja = int(input('Total Belanja : '))
diskon = totalBelanja >= 100000
# if hasil:
#   print('lulus')
# else:
#   print('Belum lulus')




# Ternary Operator / Shorthand if
""""
Soal 1
Inputkan total belanja, apabila total belanja 100k ke atas maka tuliskan 'Anda mendapatkan diskon' dan sebaliknya
"""

""""
Soal 2, dapat diskon kalau belanja minimal 200k 7.5%
Barang 1 : 20000
Barang 2 : 50000
Barang 3 : 40000
Barang 4 : 120000
Total Belanja : 230000
Diskon        :  17250
Total Bayar   : 212750
"""

diskon =(totalBelanja * 7.5/100) if totalBelanja >= 200000 else  0