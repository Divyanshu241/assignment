n=int(input('Enter Number:'))
for x in range(2,n+1):
    for i in range(2,(x//2)+1):
        if (x%i)==0:
            break
    else:
        print(x)