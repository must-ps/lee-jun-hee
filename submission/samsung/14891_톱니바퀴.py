def getRotatedTarget(target, direction):
    if (direction>0):
        return (target-1)%8
    else:
        (target+1)%8

def rotateA(direction):
    global a,b
    a = getRotatedTarget(a,direction)
    if gears[0][a]==gears[1][b]:
        return
    else:
        rotateB(direction*-1)

def rotateB(direction):
    global b,c,d
    b = getRotatedTarget(b,direction)
    c = getRotatedTarget(c,direction)
    # check b
    if gears[1][b]==gears[0][a]:
        return
    else:
        rotateA(direction*-1)
    # check c
    if gears[1][c]==gears[2][d]:
        return
    else:
        rotateC(direction*-1)    

def rotateC(direction):
    global d,e,f
    d = getRotatedTarget(d,direction)
    e = getRotatedTarget(e,direction)
    # check d
    if gears[2][d]==gears[1][c]:
        return
    else:
        rotateB(direction*-1)
    # check e
    if gears[2][e]==gears[3][f]:
        return
    else:
        rotateD(direction*-1)   

def rotateD(direction):
    global e,f
    f = getRotatedTarget(f,direction)
    if gears[3][f]==gears[2][e]:
        return
    else:
        rotateC(direction*-1)

gears = [list(map(int, input().split())) for _ in range(4)]
K = int(input())
methods = [list(map(int, input().split())) for _ in range(K)]
a, b, c, d, e, f = 2, 6, 2, 6, 2, 6

for gear_num, direction in methods:
    if (gear_num==1):
        rotateA(direction)
    elif (gear_num==2):
        rotateB(direction)
    elif (gear_num==3):
        rotateC(direction)
    elif (gear_num==4):
        rotateD(direction)

ans_1 = gears[0][(a+6)%8]
ans_2 = gears[1][(c+6)%8]*2
ans_3 = gears[2][(e+6)%8]*4
ans_4 = gears[3][(f+2)%8]*8

print(ans_1 + ans_2 + ans_3 + ans_4)