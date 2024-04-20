# https://www.acmicpc.net/problem/14501

# 스스로 다시 풀어봐야댐

# [참고] 2024/04/12
# https://www.youtube.com/watch?v=9GLuPXiIC3s
# 뒤부터 앞으로 도는 DP 풀이 -------------------------------------------- 

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0]*(N+1)
for n in range(N-1,-1,-1): # 뒤에서 앞으로 (완료기준)
    if n+T[n]<=N: # 기간내 상담완료 가능
        dp[n]=max(dp[n+1], dp[n+T[n]]+P[n]) # 상담 안할때 / 할때 -> 둘중 더 큰것으로
    else: # 기간내 상담완료 불가능
        dp[n]= dp[n+1]

print(dp[0])

# [내가 다시 풀이] 2024/04/** -------------------------------------------

