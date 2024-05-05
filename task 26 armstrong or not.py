n=int(input('Enter Number:'))
s=0
for i in str(n):
    i=int(i)
    s+=i**3
if n==s:
    print("It's a Armstrong Number.")
else:
    print("It's not a Armstrong Number.")