import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        food_1, food_2 = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, food_1 + 2 * food_2)
        answer += 1
    return answer if scoville[0] >= K  else -1
