# 가장 빠른 버스 노선 구하기!
# 모든 도시의 쌍과 관련된 최솟값을 찾아야 하는 문제 
# 📌그래프에서 시작점을 지정하지 않고, 모든 노드와 관련된 최소 경로를 구하는 알고리즘인 
# 플로이드-워셜 알고리즘을 활용하여 푸는 문제  

import sys
input = sys.stdin.readline
N = int(input())    # N 도시 개수
M = int(input())    # M 노선 개수
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]  # 노선 데이터를 저장하는 인접 행렬(2치원 리스트)를 충분히 큰 값으로 초기화

for i in range(1, N+1):
  distance[i][i] = 0    # 인접 행렬에 시작 도시와 종료 도시가 같은 자리에 0 저장  

for i in range(M):    # 노선 데이터를 distance 행렬에 저장
  s, e, v = map(int, input().split())
  if distance[s][e] > v:  # 노선이 여러 개 있을 땐, 새로운 v 값이 지금 현재 있는 값보다 작을 때만 받음
    distance[s][e] = v

# 플로이드 워셜 알고리즘 수행
for k in range(1, N+1):   # 3중 for 문의 순서 중요, k가 가장 바깥쪽
  for i in range(1, N+1):
    for j in range(1, N+1):
      if distance[i][j] > distance[i][k] + distance[k][j]:
        distance[i][j] = distance[i][k] + distance[k][j]    # 최단 거리 업데이트

# 정답 리스트 출력
for i in range(1, N+1):
  for j in range(1, N+1):
    if distance[i][j] == sys.maxsize:
      print(0, end=' ')
    else:
      print(distance[i][j], end=' ')
  print()   # 줄바꿈