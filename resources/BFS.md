### BFS
- BFS는 기본적인 그래프 탐색 방법 중 하나입니다.
- 그래프는 값을 저장하는 node, node를 잇는 edge들로 이루어진 자료구조입니다.
- BFS로 그래프의 모든 node를 탐색할 수 있습니다. 하지만 주로 문제풀이에서 쓰이는 방법은, 내가 타겟으로 삼은 node에 시작 node로 부터 최단거리로 도착하는 경로를 찾는 방식으로 많이 쓰입니다.

### BFS 예시 코드

```python
edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [6, 7]]
```

- 각 값은 node 번호이고, edges에 있는 숫자 쌍은 해당 두 node가 이어져있음을 뜻합니다. 예를들어 1번 node는 2, 3번 node와 이어져있습니다.
- 먼저 bfs를 원활하게 구현하기 위해서는, 각 node 별로 어떤 node와 연결되어있는지를 정리할 필요가 있습니다. 위의 edges는 어떤 node들이 서로 연결되어있는지의 정보만 제공할 뿐, 1번 node는 어떤 node들과 이어져있는지 정보는 직접 찾아야하므로 이를 변환하겠습니다.
- 우리의 목표는 1번 node는 어떤 node와 이어져있어? 라고했을 때 바로 [2, 3] 이라는 답이 나올 수 있는 자료구조를 만드는 것입니다. 이를 adjs(adjacent) 라고 이름짓고, 딕셔너리(해시테이블)을 만들겠습니다.

```python
adjs = {1:[2, 3], 2:[1, 4], 3:[1, 5], 4:[2, 6], 6:[4, 7], 7:[6]}
```

- 이렇게 작성하면, `adjs[1]` 을 호출했을 때 1번 node와 연결된 node들의 list인 `[2, 3]`을 반환받습니다.
- 매번 문제를 볼 때마다 해당 `adjs` 딕셔너리를 직접 작성할 수는 없기때문에, 문제에서 주어진 그래프의 정보로부터 `adjs`를 뽑아올 수 있는 로직을 직접 작성해야합니다.
- 위 예시의 경우 이런식으로 작성해보겠습니다.

```python
from collections import defaultdict
adjs = defaultdict(list)
for node_1, node_2 in edges:
    adjs[node_1].append(node_2)
    adjs[node_2].append(node_1)
```

- 이렇게 `adjs`를 만들었습니다. 이번엔  BFS를 실행하기 위한 node들의 큐를 만들어줍니다. 파이썬의 `deque` 자료구조를 이용하겠습니다. 큐의 최초 상태에는 내가 탐색을 시작하고자 하는 node를 넣어줍니다.

```python
start_node = 1
nodes = deque([start_node])
```

- 마지막으로,`visited`라는 딕셔너리를 만들건데요. 해당 딕셔너리는 node에 이미 방문했는지 여부를 저장합니다. 최초 탐색 전에는 아무 node도 방문하지 않았으므로 기본값이 `False`인 `defaultdict`를 만들겠습니다.

```python
visited = defaultdict(lambda: False)
```

- 이제 모든 준비가 끝났습니다. BFS의 기본 원리는, _**"node를 방문하고, 방문한 node와 인접한 node들을 큐에 넣어 다음에 방문하도록 한다."**_ 입니다. `while`문을 이용해서 `nodes` 내부에 값이 없어질 때까지 반복문을 실행합니다.

```python
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
    # 큐에서 하나의 node를 빼오면서, 방문완료 처리
    visited[now] = True
    # 현재 방문중인 node를 출력
    print(now, end="  ")
    # adjs[now] 는 현재 방문중인 now node와 인접한 node들의 리스트를 반환한다.
    for adj in adjs[now]:
        # 만약 인접한 node를 넣으려했는데, 이미 visited 라면 무시한다.
        if visited[adj]:
            continue
        nodes.append(adj)
print()
print("BFS ended")
```

- 알고리즘의 이해가 가지않는다면, 샘플 코드 중간중간에 `nodes`의 상태라던가, `adjs[now]`를 직접 출력해보면서 이해하시는게 빠를 수 있습니다.

### 응용
- `start_node`로 부터 `target_node`까지의 최소거리를 BFS를 활용해서 어떻게 구할 수 있을까요?
- BFS는 기본적인 그래프 탐색 방법이지만, `nodes` 큐에 어떤 정보를 넣느냐에 따라서 다양한 응용이 가능합니다. 대표적인 예시인 최소거리를 구해보겠습니다.
- 기본 골조는 동일합니다. 다만, `nodes`큐에 node의 번호뿐만 아니라, 시작 node로부터의 거리까지 같이 append합니다.

```python
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
```
- 이렇게 실행해보면, 1과 6번 node 사이의 거리인 3이 출력됩니다.
