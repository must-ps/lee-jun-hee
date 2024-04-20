# https://www.acmicpc.net/problem/14503

# 2024/04/17

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def clean(r,c):
    global ans
    if (map[r][c]==0):
        map[r][c] = 2
        ans+=1
    return

def no_where_to_clean(r,c):
    for i in range(4):
        if map[r+dx[i]][c+dy[i]]==0:
            return False
    return True

ans = 0
N, M = map(int, input().split())
r, c, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)] # 청소 안한곳 0, 벽 1, 청소 한곳 2

while True:
    clean(r,c)
    # [case1] 사방면 다 벽 or cleaned
    if no_where_to_clean(r,c):
        d_to_move = (d + 2) % 4
        x = r + dx[d_to_move] # 후진
        y = c + dy[d_to_move] # 후진
        if (0 <= x < N and 0 <= y < M and map[x][y]!=1): # 후진가능
            r,c = x,y
        else: # 청소불가능
            break # while 루프에서 빠져나오기
    # [case2] 사방면 중 청소할 곳 있음
    else: 
        d = (d + 3) % 4 # 반시계 방향으로 90도 회전
        x = r + dx[d] # 전진
        y = c + dy[d] # 전진
        if (0 <= x < N and 0 <= y < M and map[x][y]==0): # 청소가능
            r,c = x,y

print(ans)
