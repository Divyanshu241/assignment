from random import choice

def display():
    for p in l[::-1]:
        print('| ',end='')
        for p1 in p:
            if p1==0: p1='.'
            elif p1==1: p1='O'
            elif p1==-1: p1='X'
            print(p1+' | ',end='')
        print('')

# 1 for O and -1 for X
#turn even for O turn odd for X

def move(x,y):
    if l[y][x]==1 or l[y][x]==-1: print('Spot is already taken. Try again .') ; return 0  
    l[y][x]=1

#winh for horizontal rows
#winv for vertical rows
#wind for digonal rows
#checkwin() need turn variable to check for draw

def checkwin(list):
    wind1=list[1][1]+list[0][2]+list[2][0]
    wind2=list[1][1]+list[0][0]+list[2][2]
    winh=0
    winv=0
    for i in range(3):
        winh=sum(list[i])
        if winh==3 or winv==3 or wind1==3 or wind2==3: return 1 ; break
        elif winh==-3 or winv==-3 or wind1==-3 or wind2==-3: return -1 ; break
        elif turn==9: return 0
        winv=0 
        for j in range (3):
            winv+=list[j][i]

#all the functions only work when list which contains the moves is named l.
#probmove contain dictionaries one with max and other with min

def checkmoves():
    probmoves=[{},{}]
    wind1=l[1][1]+l[0][2]+l[2][0]
    wind2=l[1][1]+l[0][0]+l[2][2]
    winh=0
    winv=0
    for i in range(9):
        winh=0
        winv=0 
        for j in range (3):
            winh+=l[i//3][j]
            winv+=l[j][i//3]
        if l[i//3][i%3]==0:
            if (i+1)%2==1: probmoves[0][i+1]=max([winh,winv,wind1,wind2]) ; probmoves[1][i+1]=min([winh,winv,wind1,wind2])
            elif (i+1)%2==0: probmoves[0][i+1]=max([winh,winv]) ; probmoves[1][i+1]=min([winh,winv])
    return probmoves

def compmove():
    moves=[0]
    losemoves=[0]
    probmove=checkmoves()
    for i in probmove[0]:
        if probmove[0][max(probmove[0],key=probmove[0].get)]==probmove[0][i]: losemoves.append(i)
    for i in probmove[1]:
        if probmove[1][min(probmove[1],key=probmove[1].get)]==probmove[1][i]: moves.append(i)
    for i in losemoves:
        losemoves.pop(0)
        print(losemoves)
        testl=[row[:] for row in l]
        testl[(i-1)//3][(i-1)%3]=1
        print(checkwin(testl))
        if checkwin(testl)==1: lose=i ; break
        else: lose=0
    for i in moves:
        moves.pop(0)
        testl=[row[:] for row in l]
        testl[(i-1)//3][(i-1)%3]=-1
        if checkwin(testl)==-1: win=i ; break
        else: win=0
    print([win,lose,choice(moves)])
    return [win,lose,choice(moves)] 

#compmove() returns a list [ winning move , losing move , random move ] if winning or losing move is 0 then there isn't amove like that. 

l=[[1,0,0],[0,-1,0],[0,-1,1]]
turn=0

display()
print("Let's play cross and knot.")
print('Enter your move using Coordinate system.')
print('First turn will be yours Knot , O .')

while True:
    turn+=1
    X=int(input('Enter X coordinate:'))
    Y=int(input('Enter Y coordinate:'))
    move(X,Y)
    display()
    cwin=checkwin(l)
    if cwin==0: print('It is a draw.') ; break
    elif cwin==1: print('Knot O won.') ; break
    elif cwin==-1: print('Cross X won.') ; break

    print('My move is this')
    for i in compmove():
        if i!=0: cmove=i ; break
    l[(cmove-1)//3][(cmove-1)%3]=-1
    display()
    cwin=checkwin(l)
    if cwin==0: print('It is a draw.') ; break
    elif cwin==1: print('Knot O won.') ; break
    elif cwin==-1: print('Cross X won.') ; break
