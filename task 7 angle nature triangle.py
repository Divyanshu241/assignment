try:
    a=int(input('Enter the first angle:'))
    b=int(input('Enter the second angle:'))
    c=int(input('Enter the third angle:'))
except:
    print('Enter the angles correctly.')
    exit()
if a+b+c==180:
    if a==90 or b==90 or c==90:
        print("It's a right angled triangle.")
    elif a==b and b==c:
        print("It's a equilateral triangle.")
    if a>90 or b>90 or c>90:
        print("It's a obtuse angled triangle.")
    if a<90 and b<90 and c<90:
        print("It's a right angled triangle.")
    if a!=b and a!=c and b!=c:
        print("It's a scalane triangle.") 
    if a==b or a==c or b==c:
        print("It's a isosceles triangle.")
else:
    print("It's not a valid triangle." )