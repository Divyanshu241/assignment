n=int(input('Enter Value for n:'))
x=int(input('Enter Value for x:'))
v1=1
v2=1
for i in range(1,n+1):
    m1=(-x)**i
    m2=x**n
    v1+=m1
    v2+=m2
print("Value for series sign,-:",v1)
print("Value for series sign,+:",v2)