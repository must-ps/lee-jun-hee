from collections import deque
from collections import defaultdict

edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [6, 7]]

adjs = defaultdict(list)
for node_1, node_2 in edges:
    adjs[node_1].append(node_2)
    adjs[node_2].append(node_1)

start_node = 1
nodes = deque([start_node])
visited = defaultdict(lambda: False)

while(nodes):
    now = nodes.popleft()
    visited[now] = True
    print(now, end="  ")
    for adj in adjs[now]:
        if visited[adj]:
            continue
        nodes.append(adj)
print()
print("BFS ended")

start_node = 1
target_node = 6
# 최초 start_node는 자기 자신으로부터의 거리가 0
nodes = deque([(start_node, 0)])
visited = defaultdict(lambda: False)

while(nodes):
    now, dist = nodes.popleft()
    visited[now] = True
    if now == target_node:
        print(f"dist between {start_node} and {target_node} is {dist}" )
        break
    for adj in adjs[now]:
        if visited[adj]:
            continue
        # adj는 now와 인접한 node. 
        # 그러므로 now와 start_node 사이 거리인
        # dist보다 1만큼 더 멀기 때문에 dist+1 을 넣어준다.
        nodes.append((adj, dist+1))