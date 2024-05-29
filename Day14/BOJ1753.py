# 최단 경로 구하기 (다익스트라 알고리즘 활용)

import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())    # V 노드 개수 E 에지 개수
K = int(input())    # 출발 노드 
distance = [sys.maxsize]*(V+1)    # 거리 저장 리스트, 충분히 큰 수로 초기화
visited = [False]*(V+1)   # 방문 여부 저장 리스트
myList = [[] for _ in range(V+1)]   # 에지 데이터 저장 인접 리스트
q = PriorityQueue()   # 다익스트라를 위한 우선순위 큐 

for _ in range(E):    # 에지의 개수만큼 반복
  u, v, w = map(int, input().split())
  myList[u].append((v, w))    # (노드, 가중치) 인접 리스트에 에지 정보 저장

# 다익스트라 수행
q.put((0, K))    # (거리 리스트의 값, 노드) 출발노드는 우선순위 큐에 넣고 시작 (자동으로 거리가 최소인 노드를 선택)
distance[K] = 0   # 거리 리스트에 출발 노드의 값을 0으로 설정

while q.qsize() > 0:   # 큐가 빌때까지 반복 
  current = q.get()
  c_v = current[1]    # 우선순위 큐에서 노드 가져오기
  if visited[c_v]:
    continue
  visited[c_v] = True   # 현재 노드를 방문노드로 업데이트
  for tmp in myList[c_v]:   # 현재 선택 노드의 에지 개수 만큼 반복
    next = tmp[0]   # 연결 노드
    value = tmp[1]    #  연결 노드 에지 가중치
    if distance[next] > distance[c_v] + value:
      distance[next] = distance[c_v] + value    # 연결 노드 최단 거리 업데이트
      q.put((distance[next], next))     # 우선순위 큐에 연결노드 추가

for i in range(1, V+1):
  if visited[i]:
    print(distance[i])
  else:     # 방문하지 않은 노드의 경우
    print("INF")


