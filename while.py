soal1 = 'Apa nama ibukota Mesir?'
jawaban1 = 'kairo'

soal2 = 'Apa nama ibukota Mesir?'
jawaban2 = 'kairo'

soal3 = 'Apa nama ibukota Mesir?'
jawaban3 = 'kairo'

soal4 = 'Apa nama ibukota Mesir?'
jawaban4 = 'kairo'

soal5 = 'Apa nama ibukota Mesir?'
jawaban5 = 'kairo'

diulang = 'ya'
while diulang.lower() == 'ya':
  skor = 0
  print(soal1)
  jawab1 = input('Jawaban : ')

  print(soal2)
  jawab2 = input('Jawaban : ')

  print(soal3)
  jawab3 = input('Jawaban : ')

  print(soal4)
  jawab4 = input('Jawaban : ')

  print(soal5)
  jawab5 = input('Jawaban : ')

  if jawab1 == jawaban1: skor +=1
  if jawab2 == jawaban2: skor +=1
  if jawab3 == jawaban3: skor +=1
  if jawab4 == jawaban4: skor +=1
  if jawab5 == jawaban5: skor +=1
   
  print('Skor anda adalah ' + str(skor))

  diulang = input('Apakah mau diulang menjawab soal (ya/tidak) ? ')
