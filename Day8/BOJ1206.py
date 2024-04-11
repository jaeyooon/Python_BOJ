# DFS와 BFS 프로그램
import sys
from collections import deque
input = sys.stdin.readline

N, M, Start = map(int, input().split())   # N 노드개수 M 에지 개수 Start 시작점
graph = [[] for _ in range(N+1)]    # 그래프 데이터 저장 인접 리스트, 2차원 배열

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(N+1):
  graph[i].sort()   # 번호가 작은 노드부터 방문하기 위해 오름차순 정렬

def DFS(v):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      DFS(i)

visited = [False] * (N+1)
DFS(Start)

def BFS(v):
  queue = deque()
  queue.append(v)   # 큐 자료구조에 시작 노드 삽입
  visited[v] = True
  while queue:
    node = queue.popleft()  # 큐애서 노드 데이터 가져오기
    print(node, end=' ')
    for i in graph[node]: # 현재 노드의 연결 노드 중 미방문 노드를 큐에 삽입하고(append) 방문 리스트에 기록
      if not visited[i]:
        visited[i] = True
        queue.append(i)

print()
visited = [False] * (N+1)
BFS(Start)