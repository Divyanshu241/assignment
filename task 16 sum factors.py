try:
    n=int(input("Enter a number to get sum of it's factors:"))
except:
    print('Enter number correctly.')
    exit()
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
print(sum)