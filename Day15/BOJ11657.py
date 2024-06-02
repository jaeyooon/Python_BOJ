import sys
input = sys.stdin.readline
N, M = map(int, input().split())    # N 노드 개수, N 에지 개수
edges = []    # 에지 정보 저장 리스트
distance = [sys.maxsize]*(N+1)   # 거리 리스트 => 인덱스가 0부터 시작하고 N번째까지 필요하므로 N+1, 충분히 큰 수로 초기화

# 에지 데이터 저장
for i in range(M):
  start, end, time = map(int, input().split())
  edges.append((start, end, time))    # 에지 리스트에 에지 정보 저장

# 벨만 포드 수행
distance[1] = 0   # 거리 리스트에 출발 노드 0으로 초기화

for _ in range(N-1):    # 노드 개수 - 1 만큼 반복 => 여기서 최단 거리 구해짐!
  for start, end, time in edges:    # 에지 개수만큼 반복하면서 현재 에지 데이터 가져오기
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
      distance[end] = distance[start] + time    # 업데이트 수행

# 음수 사이클 존재 여부 확인
mCycle = False

for start, end, time in edges:    
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
      mCycle = True   # 업데이트 가능하므로 음수 사이클 존재한다는 의미

if not mCycle:
  for i in range(2, N+1):
    if distance[i] != sys.maxsize:
      print(distance[i])
    else:     # 해당 도시로 가능 경로가 없는 경우
      print(-1)
else:     # 음수 사이클 존재하는 경우
  print(-1)