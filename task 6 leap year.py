try:
    yr=int(input('Enter a year:'))
except:
    print('Enter a valid year.')
    exit()
if yr%4==0:
    print("It's leap year.")
elif yr<0:
    print('Enter a valid year.')
else:
   print("It's not a leap year.") 