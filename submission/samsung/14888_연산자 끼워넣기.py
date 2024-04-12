# https://www.acmicpc.net/problem/14888

# 스스로 다시 풀어봐야댐

# [참고] 2024/04/12 -------------------------------------------- 
# https://www.youtube.com/watch?v=6mbVfrwb3Qc
# --- 백트래킹 --------------------------------------------------

def dfs(n, sm, add, sub, mul, div):
    global mn, mx
    # [0] 결과값/중간 값의 범위: int(-1e9)~int(1e9)
    if sm < int(-1e9) or int(1e9)<sm:
        return

    # [1] 종료조건(정답처리)
    if n==N: # 실제 n 인덱스는 0~N-1니까 N은 없는놈 -> 여기서 리턴을 해줘야함
        mn = min(mn, sm)
        mx = max(mx, sm)
        return

    # [2] 하부호출: 연산자 개수 남았을 경우만 호출 가능
    if add>0:
        dfs(n+1, sm+lst[n], add-1, sub, mul, div)
    if sub>0:
        dfs(n+1, sm-lst[n], add, sub-1, mul, div)
    if mul>0:
        dfs(n+1, sm*lst[n], add, sub, mul-1, div)
    if div>0:
        dfs(n+1, int(sm/lst[n]), add, sub, mul, div-1)

N = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

mn, mx = int(1e9), int(-1e9)
dfs(1, lst[0], add, sub, mul, div) # 자신과, 자기 바로 앞에 붙은 연산자를 처리하기 때문에 n=1부터 시작한다
print(mx, mn, sep='\n')

# [내가 다시 풀이] 2024/04/** -------------------------------------------