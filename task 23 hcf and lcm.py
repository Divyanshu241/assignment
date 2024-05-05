n=int(input('Enter first number:'))
n1=int(input('Enter second number:'))
m=n*n1
if n1>n:
    n2=n1
    while n1%n!=0:
        if n1%n!=0:
            n1=n
            n=n2%n
            n2=n1
    print('HCF:'+str(n))
    print('LCM:'+str(int(m/n)))
else:
    n2=n
    while n%n1!=0:
        if n%n1!=0:
            n=n1
            n1=n2%n1
            n2=n
    print('HCF:'+str(n1))
    print('LCM:'+str(int(m/n1)))