import heapq

def _solution(operations):
    answer = []
    operations = [operation.split(' ') for operation in operations]
    # print(operations)
    min_heap = []
    max_heap = []
    
    for operation in operations:
        if operation[0] == 'I':
            heapq.heappush(min_heap, int(operation[1]))
            heapq.heappush(max_heap, -int(operation[1]))
        elif operation[0] == 'D':
            if len(min_heap) == 0:
                pass
            elif operation[1] == '1':
                maxvalue = -heapq.heappop(max_heap)
                min_heap.remove(maxvalue)
            elif operation[1] == '-1':
                minvalue = heapq.heappop(min_heap)
                max_heap.remove(-minvalue)
    if len(min_heap) == 0:
        answer = [0,0]
    else:
        answer = [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
                
    
    return answer




def solution(operations):

    num = []
    MIN, MAX = -1, 1
    now_heap_status = MIN


    for i in operations:
        j = i.split()
        l = j[0]
        r = j[1]

        if l == 'I':
            heapq.heappush(num, int(r))     
        elif len(num) > 0 and l == 'D' and r == '-1' :
            heapq.heapify(num)
            heapq.heappop(num)
        elif len(num) > 0 and l == 'D' and r == '1' :
            for i in range(len(num)):
                    num[i] *= -1
            heapq.heapify(num)
            heapq.heappop(num)
            #- 복구
            for i in range(len(num)):
                num[i] *= -1

    if len(num) > 0:
        return  [max(num), min(num)]
    else:
        return [0,0]