# 테스트 코드 하나만 맞고 다 틀린 풀이
# 틀린 이유 궁예 : 
# "하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다." <- 이 조건 놓쳐서

import heapq as hq

def solution(jobs):
    element_num = len(jobs)
    
    q = [(x[1],x[0]) for x in jobs] # 소요시간을 첫번째 요소로, 요청시점을 두번째 요소로
    hq.heapify(q) # 소요되는 시간을 기준으로 정렬 (오름차순)
    
    overall_sum = 0
    time_spent_so_far = 0

    while q:
        tmp_smallest = hq.heappop(q)
        time_spent_so_far += tmp_smallest[0] # 현재 요소의 소요시간을 넣어줌
        overall_sum += (time_spent_so_far-tmp_smallest[1])
    
    return overall_sum/element_num

