n=int(input('Enter Number:'))
x=n*15
c=0
for y in range(2,x):
    for i in range(2,(y//2)+1):
        if (y%i)==0:
            break
    else:
        if n>0:
            c+=1
            n-=1
            print(y)