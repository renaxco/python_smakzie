# NESTED => BERSARANG

is_passed = input("Apakah lolos fase 1?")
keterangan = ''

if(is_passed.lower() == 'y' ):
    is_passed = input("Apakah lolos  fase 2?")
    if(is_passed.lower() == 'y' ):
        is_passed = input("Apakah lolos  fase 3?")
        if(is_passed.lower() == 'y' ):
            keterangan = 'Selamat anda diterima kerja!'
        else:
            keterangan = 'Tidak lolos di fase 3'
    else:
        keterangan = 'Tidak lolos di fase 2'
else:
    keterangan = 'Tidak lolos di fase 1'

print(keterangan)