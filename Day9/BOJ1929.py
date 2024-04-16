# 소수 구하기  

import math
M, N = map(int, input().split())  # M 시작수 N 종료수
A = [0] * (N + 1)  # 소수 리스트 초기화

for i in range(2, N + 1):
  A[i] = i

for i in range(2, int(math.sqrt(N)) + 1):   # 제곱근까지만 수행
  if A[i] == 0:
    continue
  for i in range(i + i, N + 1, i):    # 배수 지우기
    A[i] = 0

for i in range(M, N + 1):
  if A[i] != 0:
    print(A[i])
