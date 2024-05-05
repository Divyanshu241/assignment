try:
    n=int(input("Enter a number to get it's multiplication table:"))
except:
    print('Enter number correctly.')
    exit()
x=0
while x<10:
    x+=1
    print(str(n)+'X'+str(x)+'='+str(x*n))
