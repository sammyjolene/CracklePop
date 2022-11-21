for number in range(101):
   if number % 3 == 0 and number % 5 ==0:
    print('CracklePop')
   elif number % 3 == 0:
    print('Crackle')
   elif number % 5 == 0:
    print('Pop')
   else:
    print(number)