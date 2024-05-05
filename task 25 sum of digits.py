n=input('Enter Number:')
s=0
for i in n:
    try:
        i=int(i)
        s+=i
    except:
        continue
print("The sum of it's digits is",str(s)+'.')