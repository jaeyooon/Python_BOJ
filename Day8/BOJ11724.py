# 연결요소의 개수 구하기
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())  # n 정점의 개수(노드 개수), m 간선의 개수(에지 개수)
graph = [[] for _ in range(n+1)]  # 그래프 데이터 저장 인접 리스트 초기화
visited = [False] * (n+1)   # 방문 기록 리스트 초기화

def DFS(v):
  visited[v] = True   # visited 리스트에 현재 노드 방문 기록
  for i in graph[v]:  # 현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행(재귀 함수 형태)
    if not visited[i]:
      DFS(i)

# graph 인접 리스트에 데이터 저장
for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

count = 0

for i in range(1, n+1):
  if not visited[i]:
    DFS(i)
    count += 1

print(count)