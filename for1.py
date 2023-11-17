# for x in range(1, 6):
#   print(f'{x} x {x+1} = {x * (x+1)}')
#   print(x, ' x ', x+1, ' = ', x * (x+1))

# 1. Tuliskan bilangan genap dari 0 - 100
# 2. Tuliskan 10, 20, 30 .. 100
# 3. Tuliskan 1x, 2x, 3x, .. 10x
# 4. Tuliskan Hello 1, Hello 2, Hello 3, .. Hello 10
# 5. Tuliskan 
#     1 x 2 = 2
#     2 x 3 = 6
#     3 x 4 = 12
#     4 x 5 = 20
#     5 x 6 = 30
# nested for pengulangan bersarang
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# for x in range(1500, 2701):
#   if x % 5 == 0 and x % 7 == 0:
#     print(x, end = '')

# for x in range(1,6):
#   for y in range(x):
#     print('*', end = ' ')
#   print()

# 10, 9, 8, 7, 6 ,5, 4, 3, 2, 1
# for x in range(10, 0, -1)
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# print(' ')
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

for x in range(1,6):
  for y in range(5,x,-1):
    print(end =' ')
  for z in range(x):
    print('*', end = ' ')
  print()
