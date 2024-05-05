n=int(input('Enter Value for n:'))
x=int(input('Enter Value for x:'))
v=1
f=1
for i in range(1,n+1):
    for i in range(1,n+1):
        f*=i
    m=(x**n)/f
    v+=m
print("Value for series sign:",v)