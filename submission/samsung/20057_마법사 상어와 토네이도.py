# https://www.acmicpc.net/problem/20057

# 2024/04/10 - 잘모르겠어서 다른분 풀이 보고 정리해봤어요! ---------------------------
# https://www.youtube.com/watch?v=IRCazBiMfnM 

import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 좌, 하, 우, 상
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
ans = dr = cnt = flag = 0 
cnt_max = 1 # 처음엔 한칸씩 이동 (1,1,2,2,3,3,...) -> flag는 0,1,0,1,...
ci = cj = N // 2 # 시작 지점

#위치 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 <- 9는 나머지
mul=[ 2, 10, 7, 1, 5, 10, 7, 1, 2, 0]  # %비율 => 100으로 나눠야 함
ai=[[-2,-1,-1,-1, 0, 1, 1, 1, 2, 0], # 좌
    [ 0, 1, 0,-1, 2, 1, 0,-1, 0, 1], # 하
    [ 2, 1, 1, 1, 0,-1,-1,-1,-2, 0], # 우
    [ 0,-1, 0, 1,-2,-1, 0, 1, 0,-1]] # 상
aj=[[ 0,-1, 0, 1,-2,-1, 0, 1, 0,-1], # 좌
    [-2,-1,-1,-1, 0, 1, 1, 1, 2, 0], # 하
    [ 0, 1, 0,-1, 2, 1, 0,-1, 0, 1], # 우
    [ 2, 1, 1, 1, 0,-1,-1,-1,-2, 0]]  # 상

while (ci,cj)!=(0,0):
    ci, cj = ci + di[dr], cj + dj[dr] # dr 방향으로 한칸 이동

    # [1] ci, cj 기준좌표 중심으로 모래량 계산 추가, 범위밖 => ans에 추가 
    if arr[ci][cj]>0: # 모래가 있을때만 진행
        val = arr[ci][cj] # 기준 좌표 모래양
        t_sum = arr[ci][cj] = 0 # 기준좌표 모래는 날아가서 없어짐

        for i in range(10): # 위치 0~9까지 처리
            ni, nj = ci + ai[dr][i], cj+aj[dr][i] # 좌표 계산
            t = (val * mul[i]) // 100 # 소수점 이하 버림
            if i==9: # 나머지 모래
                t = val - t_sum
            
            if 0 <= ni < N and 0 <= nj < N: # 범위 내 => 누적
                arr[ni][nj]+=t
            else: # 범위 밖 => ans에 추가
                ans += t # 밖으로 나간 모래양에 추가
            t_sum += t
            

    cnt += 1 # 한칸씩 이동하는거
    if cnt == cnt_max: # 즉, 방향을 전환해야한다는 이야기
        cnt = 0
        dr = (dr+1) % 4 # 방향은 매번 바뀜
        if flag == 0:
            flag = 1
        else:
            flag = 0
            cnt_max+=1


print(ans)