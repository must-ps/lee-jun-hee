# https://www.acmicpc.net/problem/14889

# 스스로 다시 풀어봐야댐

# [참고] 2024/04/12 -------------------------------------------- 
# 
# --- 요것도 2^20정도의 시간복잡도 예상되니 백트래킹으로 풀리겠다~ ---------------------------

def dfs(n, alst, blst):
    global ans

    # (1) 종료 조건 -> 답 처리
    if n==N:
        if len(alst)==len(blst):    # 같은 인원수로 팀을 구성
            # 차이 계산
            asm = bsm = 0
            for i in range(M):
                for j in range(M):
                    asm += arr[alst[i]][alst[j]]
                    bsm += arr[blst[i]][blst[j]]
            # min값 업데이트        
            ans = min(ans, abs(asm-bsm))
        return

    # (2) 하부호출
    dfs(n+1, alst+[n], blst) # A팀 선택
    dfs(n+1, alst, blst+[n]) # B팀 선택


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

M = N//2
ans = 100*M*M
dfs(0, [], []) # n, a_list, b_list

print(ans)


# [내가 다시 풀이] 2024/04/** -------------------------------------------

N = int(input())
map = [[0]*N]*N

for i in range(N):
    map[i] = list(map(int, input().split()))