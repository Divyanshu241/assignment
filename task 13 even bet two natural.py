try:
    n1=int(input('Enter the first natural number:'))
    n2=int(input('Enter the second natural number:'))
except:
    print('Enter number correctly.')
    exit()
if n1<n2:
    while n1<n2:
        n1+=1
        if n1%2==0:
            if n1!=n2:
                print(n1)     
if n1>n2:
    while n1>n2:
        n1-=1
        if n1%2==0:
            if n1!=n2:
                print(n1)