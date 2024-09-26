msg=input('Enter message:')
pas='divy'
msg_ac=[]
pas_ac=[]
for i in msg:
    msg_ac.append(ord(i))
for i in pas:
    pas_ac.append(ord(i))
en_msg=[]
for i in msg_ac:
    en_msg.append(i^pas_ac[(len(pas)-1)-msg_ac.index(i)])
for i in msg_ac:
    print(chr(i),end='')
print()
print('Encrypted:',end='')
for i in en_msg:
    print(chr(i),end='')
msg=[]
for i in en_msg:
    msg.append(i^pas_ac[(len(pas)-1)-en_msg.index(i)])
print()
print('Message:',end='')
for i in msg:
    print(chr(i),end='')