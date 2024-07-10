l=[['.','.','.'],['.','.','.'],['.','.','.']]

c=0

while True:
    c+=1
    if c%2==0:
        print("It's O's turn. ")
    else:
        print("It's X's turn. ")

    try:
        cox=int(input('Enter Coordinate X:'))
        coy=int(input('Enter Coordinate Y:'))

        X=l[coy]

        if c%2==0:
            X[cox]='O'
        else:
            X[cox]='X'
    except:
        break

    for p in l[::-1]:
        for p1 in p:
            print(p1+' ',end='')
        print('')
    
    for w in l:
        x=0
        o=0
        for b in w:
            if b=='X':
                x+=1
            elif b=='O':
                o+=1

        if x==3:
            print('**X** ***WON***')
            break
        elif o==3:
            print('**O** ***WON***')
            break 
