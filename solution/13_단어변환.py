from collections import deque
from collections import defaultdict

from itertools import combinations

def solution(begin, target, words):
    # 각 단어 = 하나의 노드
    # 각 단어의 길이 (일괄) = n 개
    # 단어 A와 단어 B가 서로 이어져있으려면, 각 단어를 이루고 있는 알파벳들 중 (n-1)개가 동일해야함 (단, 순서도 동일)
    # 이 상태에서 adjs 딕셔너리를 만들고 BFS를 진행해보자.

    adjs = defaultdict(list)

    words.insert(0,begin)

    for node_1, node_2 in combinations(words, 2):
        for i in range(len(begin)):
            if (node_1[:i]+node_1[i+1:] == node_2[:i]+node_2[i+1:]):
                adjs[node_1].append(node_2)
                adjs[node_2].append(node_1)
                break

    # adjs 생성
    for j in range(len(words)-1):
        for k in range(j+1,len(words)):
            for i in range(len(begin)): # i = 동일하지 않은 알파벳이 위치한 인덱스
                node_1 = words[j]
                node_2 = words[k]
                if (node_1[:i]+node_1[i+1:] == node_2[:i]+node_2[i+1:]):
                    adjs[node_1].append(node_2)
                    adjs[node_2].append(node_1)
                    break

    # BFS 세팅
    nodes = deque([(begin,0)])
    visited = defaultdict(lambda: False)
    while(nodes):
        now, dist = nodes.popleft()
        visited[now] = True
        if now == target:
            return dist
            break
        for adj in adjs[now]:
            if visited[adj]:
                continue
            nodes.append((adj, dist+1))

    return 0