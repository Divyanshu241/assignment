try:
    age=int(input('Enter your Age:'))
except:
    print('Enter your age correctly.')
    exit()
if age>=18:
    print('You are eligible to give your vote.')
elif age<0:
    print('Enter your age correctly.')
else:
   print('You are not eligible to give your vote.') 