try:
    n=int(input("Enter a number to get it's factors:"))
except:
    print('Enter number correctly.')
    exit()
for i in range(1,n):
    if n%i==0:
        print(i)