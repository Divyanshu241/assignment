n=int(input('Enter number:'))
c=''
s=''
z=0
while n>0:
    z+=1
    n-=1
    x=z
    c=c+' '+str(z)
    while x>1:
        if x==z:
            s=''
        x-=1
        s=s+' '+str(x)
    print('  '*n+c+s)