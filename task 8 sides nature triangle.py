print('Enter the lenghts of sides without units.')
try:
    a=int(input('Enter the length of first side:'))
    b=int(input('Enter the length of second side:'))
    c=int(input('Enter the length of third side:'))
    exit()
except:
    print('Enter the sides correctly.')
if a!=b and a!=c and b!=c:
    print("It's a scalane triangle.")
elif a==b and b==c:
    print("It's a equilateral triangle.") 
elif a==b or a==c or b==c:
    print("It's a isosceles triangle.")