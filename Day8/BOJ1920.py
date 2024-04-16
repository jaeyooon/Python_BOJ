# 원하는 정수 찾기  
N = int(input())  # 주어진 수 개수  
A = list(map(int, input().split()))   # 수 데이터 리스트  
A.sort()  # 이진탐색이므로 오름차순 정렬
M = int(input())  # 탐색할 숫자 개수  
targetList = list(map(int, input().split()))  # 탐색할 수 데이터 리스트  

for i in range(M):
  find = False
  target = targetList[i]
  # 이진 탐색 시작  
  startIndex = 0
  endIndex = len(A) - 1  
  while startIndex <= endIndex:
    midIndex = (startIndex + endIndex) // 2
    midValue = A[midIndex]
    if midValue < target:
      startIndex = midIndex + 1
    elif midValue > target:
      endIndex = midIndex - 1  
    else:
      find = True
      break 
  if find:
    print(1)
  else:
    print(0)


