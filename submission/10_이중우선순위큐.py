# 테스트 케이스 반은 맞고 반은 틀림.. ㅠ
import heapq as hq

def solution(operations):
    max_heap = []
    min_heap = []
    
    for o in operations:
        if o[0]=="I":
            num = int(o[2:])
            hq.heappush(min_heap,num)
            hq.heappush(max_heap,-num)
        elif o[2]=="1":
            if len(max_heap)>0:
                hq.heappop(max_heap)
        else:
            if len(min_heap)>0:
                hq.heappop(min_heap)
    
    if len(max_heap)==len(min_heap):
        return [0,0]
    else:
        max_num = -hq.heappop(max_heap) 
        min_num = hq.heappop(min_heap)
        return [max_num, min_num]

# 테스트 케이스 1개 빼고는 다 맞았는데.. 그 하나떄문에 틀림
# 어떤 케이스를 놓친걸까 ㅇㅅㅇ
import heapq as hq

def solution(operations):
    max_heap = []
    min_heap = []
    
    for o in operations:
        if o[0]=="I":
            num = int(o[2:])
            hq.heappush(min_heap,num)
            hq.heappush(max_heap,-num)
        elif o[2]=="1":
            if len(max_heap)>0:
                hq.heappop(max_heap)
        else:
            if len(min_heap)>0:
                hq.heappop(min_heap)
    
    if len(max_heap)*len(min_heap)<1: # 하나라도 길이가 0이면
        return [0,0]
    elif (-max_heap[0]==min_heap[0]):
        return [0,0]
    else:
        max_num = -hq.heappop(max_heap) 
        min_num = hq.heappop(min_heap)
        return [max_num, min_num]

# 여전히 틀림
import heapq as hq

def solution(operations):
    max_heap = []
    min_heap = []
    
    trash = set()
    
    for o in operations:
        if o[0]=="I":
            num = int(o[2:])
            hq.heappush(min_heap,num)
            hq.heappush(max_heap,-num)
        elif o[2]=="1":
            op_num+=1
            if (op_num+1>num_num):
                min_heap=[]
                max_heap=[]
                continue
            else:
                op_num+=1
            if len(max_heap)>0:
                n = hq.heappop(max_heap)
                trash.add(-n)
        else:
            op_num+=1
            if (op_num+1>num_num):
                min_heap=[]
                max_heap=[]
                continue
            else:
                op_num+=1
            if len(min_heap)>0:
                n = hq.heappop(min_heap)
                trash.add(n)
    
    if len(max_heap)*len(min_heap)<1: # 하나라도 길이가 0이면
        return [0,0]
    
    max_num = -hq.heappop(max_heap) 
    min_num = hq.heappop(min_heap)
        
    if (max_num in trash or min_num in trash):
        return [0,0]
    elif (max_num==min_num):
        return [0,0]
    else:
        return [max_num, min_num]