l=[['.','.','.'],['.','.','.'],['.','.','.']]
l1=[['.','.','.'],['.','.','.'],['.','.','.']]
l2=[[l[0][2],l[1][1],l[2][0]],[l[0][0],l[1][1],l[2][2]],]

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
        X1=l1[cox]

        if c%2==0:
            X[cox]='O'
            X1[coy]='O'
        else:
            X[cox]='X'
            X1[coy]='X'
    except:
        break
    print(l)
    print(l[2][0])
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
            quit()
        elif o==3:
            print('**O** ***WON***')
            quit()

    for w in l1:
        x=0
        o=0
        for b in w:
            if b=='X':
                x+=1
            elif b=='O':
                o+=1

        if x==3:
            print('**X** ***WON***')
            quit()
        elif o==3:
            print('**O** ***WON***')
            quit()
    
    for w in l2:
        x=0
        o=0
        for b in w:
            if b=='X':
                x+=1
            elif b=='O':
                o+=1

        if x==3:
            print('**X** ***WON***')
            quit()
        elif o==3:
            print('**O** ***WON***')
            quit()
