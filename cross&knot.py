
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

def move(x,y,turn):
    if l[y][x]==1 or l[y][x]==-1: return 0 ; print('Spot is already taken. Try again .') 
    elif turn%2==1: l[y][x]=1
    elif turn%2==0: l[y][x]=-1

#winh for horizontal rows
#winv for vertical rows
#wind for digonal rows

def checkwin():
    for i in range(3):
        winh=0
        winv=0
        wind1=l[1][1]+l[0][2]+l[2][0]
        wind2=l[1][1]+l[0][0]+l[2][2]
        if winh==3 or winv==3 or wind1==3 or wind2==3: return 1 ; break
        elif winh==-3 or winv==-3 or wind1==-3 or wind2==-3: return -1 ; break
        for j in range (3):
            winh+=l[i][j]
            winv+=l[j][i]

#all the functions only work when list which contains the moves is named l.

l=[[0,0,0],[0,0,0],[0,0,0]]
turn=0

print("Let's play cross and knot.")
print('Enter your move using Coordinate system.')
print('First trun will be of Knot , O .')


while True:
    display()
    x=int(input('Enter X coordinate:'))
    y=int(input('Enter Y coordinate:'))
    move(x,y,turn)
    turn+=1
    win=checkwin()
    if win==1: print('Knot O won.') ; break
    elif win==-1: print('Cross X won.') ; break