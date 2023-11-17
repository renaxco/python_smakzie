barang1 = float(input('Barang 1\t: '))
barang2 = float(input('Barang 2\t: '))
barang3 = float(input('Barang 3\t: '))
barang4 = float(input('Barang 4\t: '))

totalBeli = barang1 + barang2 + barang3 + barang4
diskon = totalBeli * 7.5/100 if totalBeli >= 200000 else 0
totalBayar = totalBeli - diskon

print('Total beli\t: ', totalBeli)
print('Diskon \t\t: ', diskon)
print('Total Bayar\t: ', totalBayar)