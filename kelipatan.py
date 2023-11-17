def kelipatan3(bilangan):
    if int(bilangan) % 3 == 0: print('Bilangan ', bilangan, ' adalah kelipatan 3')
    else : print('Bilangan ', bilangan, ' adalah bukan kelipatan 3')

def kelipatan10(bilangan):
    if int(bilangan) % 10 == 0: print('Bilangan ', bilangan, ' adalah kelipatan 10')
    else : print('Bilangan ', bilangan, ' adalah bukan kelipatan 10')

def kelipatan20(bilangan):
    if int(bilangan) % 20 == 0: print('Bilangan ', bilangan, ' adalah kelipatan 20')
    else : print('Bilangan ', bilangan, ' adalah bukan kelipatan 20')

kelipatan7 = lambda bilangan : print('Bilangan ', bilangan, ' adalah kelipatan 7') if int(bilangan) % 7 == 0 else print('Bilangan ', bilangan, ' adalah bukan kelipatan 7')

bilangan = input('Masukkan bilangan : ')

kelipatan3(bilangan)
kelipatan7(bilangan)

Buatlah 5 function, 5 lambda untuk menentukan apakah bilangan termasuk bilangan kelipatan 
3, 7, 10, 11, 20, 2, 100, 1000, 5, 12