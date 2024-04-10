import heapq

def solution(scoville, K):
    my_heap = scoville.copy()
    heapq.heapify(my_heap)
    answer = 0
    
    while(my_heap[0]<K and len(my_heap)>=2):
        first = heapq.heappop(my_heap)
        second = heapq.heappop(my_heap)
        heapq.heappush(my_heap, first+second*2)
        answer+=1
        
    if (my_heap[0]<K): 
        return -1
    
    return answer