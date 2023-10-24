import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    job_deque = deque(progresses)
    speed_deque = deque(speeds)
    
    while(job_deque):
        for idx in range(len(job_deque)):
            job_deque[idx] = min(job_deque[idx] + speed_deque[idx], 100)
        cnt = 0
        while(job_deque and job_deque[0] == 100):
            job_deque.popleft()
            speed_deque.popleft()
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
    # answer = []
    # finish_dates = deque([math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)])
    # date = 0
    # while finish_dates:
    #     count = 0
    #     if finish_dates[0] == date:
    #         while finish_dates and finish_dates[0] <= date:
    #             finish_dates.popleft()
    #             count += 1
    #         answer.append(count)
    #     date += 1 
    
    return answer