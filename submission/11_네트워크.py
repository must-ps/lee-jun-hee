from collections import deque
from collections import defaultdict

def solution(n, computers):
    # (1) 인접 딕셔너리 만들기
    adjs = defaultdict(list)
    for node_idx in range(n):
        for i, val in enumerate(computers[node_idx]):
            if i!=node_idx and val==1:
                adjs[node_idx].append(i)
                
    # (2) 각각 이어진 애들에 대하여 BFS 실행 - BFS로 노드 하나씩 소거하며 count            

    visited = defaultdict(lambda: False)
    network_num = 0

    while True:
        left_over_idx = -1
        # left_over_idx 추출
        for idx in range(n):
            if visited[idx]==False:
                left_over_idx = idx
                break
        # 모든 visited value가 True일 경우 그대로 값 반환        
        if (left_over_idx==-1): 
            return network_num
        # visited가 false인 노드가 있을 경우 - 해당 노드를 시작으로 BFS 시전
        else:
            nodes = deque([left_over_idx])
            while(nodes):
                now = nodes.popleft()
                visited[now] = True
                for adj in adjs[now]:
                    if visited[adj]:
                        continue
                    nodes.append(adj)
            # BFS가 한번씩 끝날때마다 네트워크 수는 +1 되어야함
            network_num+=1