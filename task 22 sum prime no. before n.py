n=int(input('Enter Number:'))
sum=0
for x in range(2,n+1):
    for i in range(2,(x//2)+1):
        if (x%i)==0:
            break
    else:
        sum+=x
print('The sum of prime numbers:'+str(sum))