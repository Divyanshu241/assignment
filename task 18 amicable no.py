try:
    n1=int(input("Enter First number:"))
    n2=int(input("Enter Second number:"))
except:
    print('Enter numbers correctly.')
    exit()
sum1=0
sum2=0
for i in range(1,n1):
    if n1%i==0:
        sum1+=i
for i in range(1,n2):
    if n2%i==0:
        sum2+=i
if sum1==n2 and sum2==n1:
    print("They are amicalbe numbers.")
else:
    print("They are not amicalbe numbers.")