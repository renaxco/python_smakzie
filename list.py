buah = ['jeruk', 'apel', 'anggur', 'kiwi','jeruk']
buah2 = ['melon','kadu','nangka']
buah[0] = 'pepaya'
buah[1:4] = ['mangga','jambu','pisang']
buah.insert(3, 'dukuh')   #menambah list item di tengah-tengah
buah.append('sirsak')   #menambah list item di akhir
buah.extend(buah2) #menggabungkan 2 list
buah.remove("nangka") #menghapus list item  
buah.pop(8) #menghapus list item berdasarkan index
del buah[0] #menghapus langsung dengan perintah
buah.clear() #menghapus semua list
print(buah)
tebakBuah = input('Tulis nama buah : ')
if tebakBuah in buah:
    print('Anda benar!')
else: print('Anda salah!')

