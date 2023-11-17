nama = input('Tuliskan nama : ')
toko = input('Tuliskan nama toko: ')
hargaKaos = input('Harga kaos : ')
hargaKemeja = input('Harga kemeja : ')
hargaCelana = input('Harga celana : ')
total = hargaKaos + hargaKemeja + hargaCelana

print("✈ Bapak "+ nama +" membeli beberapa baju di Toko "+ toko +" yaitu baju kaos dengan \nharga Rp. "+ str(hargaKaos) +", \nharga kemeja Rp. "+ str(hargaKemeja) +", dan \nharga celana Rp. "+ str(hargaCelana) +". \nTotal yang harus dibayar adalah Rp. "+ str(total) +".")

buatlah variabel x, y, z dan input dari user
kemudian tampilkan hasil penjumlahan dan perkalian bilangan x, y, z

buku = float(input('Masukkan angka buku : '))
alat_tulis = float(input('Masukkan angka alat tulis : '))
tas = float(input('Masukkan angka tas : '))
jumlah = buku + alat_tulis + tas
diskon = jumlah * 10 /100
print('Harga Beli '+jumlah)
print('Diskon '+diskon)
print('Total Bayar : ', jumlah - diskon)


Andi membeli peralatan sekolah berupa buku dengan harga 25000, alat tulis 20000, dan tas seharga 300000. Berapakah yang harus dibayar oleh Andi dengan mendapatkan diskon 10%