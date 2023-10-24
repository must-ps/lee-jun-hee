# 알고리즘 정리

## 해시

- Hashmap(딕셔너리)
    - key - value로 이어진 쌍들의 집합. key값을 이용해서 value에 바로 접근이 가능
- Hashset(세트)
    - 중복 원소를 허용하지 않는 key들의 집합
- [Lv1. 폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845)
- [Lv2. 위장](https://school.programmers.co.kr/learn/courses/30/lessons/42578)
- [Lv2. 뉴스 클러스터링](https://programmers.co.kr/learn/courses/30/lessons/17677)
- [Lv3. 베스트앨범](https://school.programmers.co.kr/learn/courses/30/lessons/42579)

## 스택 / 큐

- 스택 - LIFO, 큐 - FIFO 구조
- [Lv.2 다리를 지나는 트럭](https://programmers.co.kr/learn/courses/30/lessons/42583)

## 힙

- 특정 작업마다 반복적으로 최대/최소값을 찾아야할 때, O(n)이 아니라 O(logn)으로 찾을 수 있음
- [Lv.3 이중우선순위큐](https://programmers.co.kr/learn/courses/30/lessons/42628)
- [Lv.3 디스크 컨트롤러](https://programmers.co.kr/learn/courses/30/lessons/42627)

## 정렬

## 완전탐색

## 탐욕법(Greedy)

- 작은 단계에서부터 최선의 선택을 한 결과가 최종적으로 최선의 값이 된다는 원리
- [Lv2. 큰 수 만들기](https://programmers.co.kr/learn/courses/30/lessons/42883)
- [Lv2. 조이스틱](https://programmers.co.kr/learn/courses/30/lessons/42860)

## 동적계획법 (DP)

- 문제를 간소화하여 n값이 작은 결과부터 구해서 귀납적으로 결과 도출
- dp 리스트를 만들어 점화식을 구현하거나, 재귀함수를 만들어 구현 가능
- [Lv.3 N으로 표현](https://programmers.co.kr/learn/courses/30/lessons/42895)
- [Lv3. 정수 삼각형](https://programmers.co.kr/learn/courses/30/lessons/43105)
- [Lv3. 하노이의 탑](https://programmers.co.kr/learn/courses/30/lessons/12946)
- [Lv4. 매출 하락 최소화](https://programmers.co.kr/learn/courses/30/lessons/72416) (+DFS)

## DFS / BFS

- DFS 재귀, BFS 큐로 구현
- [Lv.3 네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)
- [Lv3. 여행경로](https://programmers.co.kr/learn/courses/30/lessons/43164)
- [Lv3. 단어 변환](https://programmers.co.kr/learn/courses/30/lessons/43163)

## 이분 탐색(Binary Search)

- 큰 범위의 숫자 중에 조건에 만족하는 특정 값을 찾아야하는 경우, O(n)으로 전체 탐색하지 않고 반으로 쪼개어가면서 O(logn)으로 구함
- [Lv3. 입국심사](https://programmers.co.kr/learn/courses/30/lessons/43238)
- [Lv3. 징검다리 건너기](https://programmers.co.kr/learn/courses/30/lessons/64062)
- [Lv4. 징검다리](https://programmers.co.kr/learn/courses/30/lessons/43236)

## 그래프

- node, vertex로 이루어진 자료구조. UnionFind(같이 연결된 집합에 속해있는지), 다익스트라, 플로이드-와샬 등 유형 존재. DFS/BFS 등으로 탐색해서 최소 경로를 찾는 경우도 있음
- [Lv3. 가장 먼 노드](https://programmers.co.kr/learn/courses/30/lessons/49189)

## 플로이드-와샬

- 주어진 모든 node에 대해 다른 node로 가는 최소 거리를 계산
- 3중 for문으로 구성되며, 시간복잡도는 O(n^3)
- [Lv3. 합승 택시 요금](https://programmers.co.kr/learn/courses/30/lessons/72413)

## 문자열 문제

- [Lv3. 가장 긴 팰린드롬](https://programmers.co.kr/learn/courses/30/lessons/12904)
- [Lv2. 숫자 문자열과 영단어](https://programmers.co.kr/learn/courses/30/lessons/81301)

## 백트래킹

- DFS의 원리를 이용하여 조건에 맞게 원소를 하나씩 채워나가다가, 맞지 않으면 다시 직전 상태로 돌아와서 다른 원소를 채워 넣는 식으로 정답을 구함
- [Lv3. N-Queen](https://programmers.co.kr/learn/courses/30/lessons/12952)

## 일반 구현 문제

- [Lv2. 신규 아이디 추천](https://programmers.co.kr/learn/courses/30/lessons/72410)
- [Lv3. 추석 트래픽](https://programmers.co.kr/learn/courses/30/lessons/17676)
- [Lv3. 자물쇠와 열쇠](https://programmers.co.kr/learn/courses/30/lessons/60059)

## 기타 일반 유형

- [Lv3. 기지국 설치](https://programmers.co.kr/learn/courses/30/lessons/12979)
- [Lv2. 124 나라의 숫자](https://programmers.co.kr/learn/courses/30/lessons/12899)
- [Lv3. 표 편집](https://programmers.co.kr/learn/courses/30/lessons/81303) (링크드 리스트, 혹은 해시)
- [Lv3. 야근 지수](https://programmers.co.kr/learn/courses/30/lessons/12927)
- [Lv2. 수식 최대화](https://programmers.co.kr/learn/courses/30/lessons/67257)
- [Lv2. n진수 게임](https://programmers.co.kr/learn/courses/30/lessons/17687)

## 투포인터

- 투포인터는 start, end값을 조절해가며 조건에 부합하는지 체크
- 투포인터의 간단한 형태 (start, end가 같이 1씩 증가하는)가 슬라이딩 윈도우라고 볼 수 있음
- [Lv3. 보석 쇼핑](https://programmers.co.kr/learn/courses/30/lessons/67258) (투포인터)