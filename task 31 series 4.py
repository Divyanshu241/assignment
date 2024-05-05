n=int(input('Enter Value for n:'))
x=int(input('Enter Value for x:'))
v1=1
v2=1
f=1
c=0
for i in range(1,n+1):
    c+=1
    f=1
    i=2*i+1
    for a in range(1,i+1):
        f*=a
    m1=float((x**i)/f)
    print(m1)
    m2=float((x**i)/f)
    if c%2==0:
        m2=-((x**i)/f)
    v1+=m1
    v2-=m2
print("Value for series sign,+:",v1)
print("Value for series sign,-:",v2)