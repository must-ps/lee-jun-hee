# [풀이1] 정확성 테스트는 통과했는데 효율성 테스트 다 실패함 (시간초과로)

from collections import deque
from collections import defaultdict

def solution(maps):
    row_nums = len(maps)
    column_nums = len(maps[0])
    
    start_node = (0,0)
    target_node = (row_nums-1, column_nums-1) # index니까 -1씩으로
    # 최초 start_node 자기 자신부터 칸 수 count (따라서 초기값 1)
    nodes = deque([(start_node, 1)])
    visited = defaultdict(lambda: False)
    
    while(nodes):
        now, dist = nodes.popleft()
        visited[now] = True
        
        # 타겟노드 도달했으면 바로 값 return
        if now == target_node:
            return dist
            break
            
        # 즉석에서 adjacent_node 체크
        adjs =[]
        row_idx, column_idx = now
        if (row_idx>0 and maps[row_idx-1][column_idx]==1):
            adjs.append((row_idx-1, column_idx))
        if (row_idx<row_nums-1 and maps[row_idx+1][column_idx]==1):
            adjs.append((row_idx+1,column_idx))
        if (column_idx>0 and maps[row_idx][column_idx-1]==1):
            adjs.append((row_idx, column_idx-1))
        if (column_idx<column_nums-1 and maps[row_idx][column_idx+1]==1):
            adjs.append((row_idx,column_idx+1))
            
        # 위에서 바로 만든 adjs 배열로 BFS 고고   
        for adj in adjs:
            if visited[adj]:
                continue
            nodes.append((adj, dist+1))
    
    return -1