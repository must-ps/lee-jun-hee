# 다소 괴상망측하게 푼 첫번쨰 풀이 ... 테스트케이스는 통과했으나 로직이 한눈에 들어오지 않음 ㅠ --------------------

import math

def solution(progresses, speeds):
    answer = []
    required_days = []
    for i in range(len(progresses)):
        required_days.append(math.ceil((100-progresses[i])/speeds[i])) # 올림처리
    print(required_days)
    
    tmp_biggest = required_days[0]
    release_amount = 0
    for i in range(len(required_days)):
        if required_days[i] <= tmp_biggest:
            release_amount+=1
            if i==(len(required_days)-1):
                answer.append(release_amount)
        else:
            answer.append(release_amount)
            release_amount = 1
            if i==(len(required_days)-1):
                answer.append(release_amount)
            else:
                tmp_biggest = required_days[i]
          
    return answer



# 재시도 ... --------------------------------------------------------------------------------------