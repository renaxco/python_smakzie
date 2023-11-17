suhu = input('Inputkan suhu celcius atau fahrenheit! ')
# mendapatlkan char terakhir
jenis = suhu[-1]
# mendapatkan nilai selain char terakhir
suhu = float(suhu[:-1])

if jenis == 'C':
  # celcius ke fahrenheit
  konversi = (suhu - 32)*5/9

elif jenis == 'F':
  # fahrenheit ke celcius
  konversi = suhu * 9/5 + 32

print(f"Suhu asal {suhu} dikonversi menjadi {konversi}")

Celcius ke Kelvin