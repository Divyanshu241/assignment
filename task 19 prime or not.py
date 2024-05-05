n=int(input('Enter Number:'))
for i in range(2,(n//2)+1):
    if (n%i)==0:
        print('It is composite.')
        break
else:
   print('It is prime.')
