a=int(input('Enter A:'))
b=int(input('Enter B:'))
c=int(input('Enter C:'))
d=(b**2-(4*a*c))**0.5
if d>0:
    print('It has real roots.')
    x=((-b)-d)/(2*a)
    x1=((-b)+d)/(2*a)
    print("It's roots are",str(x)+','+str(x1)+'.')
else:
    print('It has no real roots.')

