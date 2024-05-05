n1=int(input('Enter first no.:'))
n2=int(input('Enter second no.:'))
l1=[]
l2=[]
for i in range(2,n1):
    if n1%i==0:
        l1.append(i)
for i in range(2,n2):
    if n2%i==0:
        l2.append(i)
for x in l1:
    for y in l2:
        if x==y:
            print("It's not a co-prime.")
            quit()
print("It's a co-prime.")
print(l1,l2)