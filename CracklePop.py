for number in range(101):
   if number % 3 == 0 and number % 5 ==0:
    print('CracklePop')
    continue
   if number % 3 == 0:
    print('Crackle')
    continue
   if number % 5 == 0:
    print('Pop')
    continue
   print(number)