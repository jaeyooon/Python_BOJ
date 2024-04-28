# ⭐ 게임 개발하기(위상 정렬)
# 어떤 건물을 짓기 위해 먼저 지어야 하는 건물이 있을 수 있다라는 문장에 주목!  
# 👉🏻 각 건물을 노드라고 생각했을 때 그래프 형태에서 노드 순서를 정렬하는 알고리즘인  
# 위상 정렬을 사용하는 문제라는 것을 알 수 있음.  

from collections import deque

N = int(input())    # N 건물 수 
A = [[] for _ in range(N + 1)]    # 건물 데이터 저장 인접 리스트
indegree = [0] * (N + 1)    # 진입 차수 리스트
selfBuild = [0] * (N + 1)   # 자기 자신을 짓는데 걸리는 시간(각 건물당 짓는데 걸리는 시간)  

for i in range(1, N + 1):
  inputList = list(map(int, input().split()))
  selfBuild[i] = inputList[0]
  index = 1
  while True:   # 인접 리스트 만들기
    preTemp = inputList[index]
    index += 1
    if preTemp == -1:
      break
    A[preTemp].append(i)
    indegree[i] += 1    # 진입 차수 데이터 저장


# 위상 정렬 수행
queue = deque()

for i in range(1, N + 1):
  if indegree[i] == 0:    # 진입 차수 리스트의 값이 0인 건물(노드)를 큐에 삽입
    queue.append(i);

result = [0] * (N + 1)

while queue:    # 큐가 빌 때까지 수행
  now = queue.popleft()
  for next in A[now]:
    indegree[next] -= 1
    # 시간 업데이트
    result[next] = max(result[next], result[now] + selfBuild[now])
    if indegree[next] == 0:
      queue.append(next)

for i in range(1, N + 1):
  print(result[i] + selfBuild[i])

