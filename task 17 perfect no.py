try:
    n=int(input("Enter a number to know of it's perfect number:"))
except:
    print('Enter number correctly.')
    exit()
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print("It's a perfect number.")
else:
    print("It's not a perfect number.")