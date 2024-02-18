# 질의의 개수가 100000이므로 질의마다 합을 구하면 안 되고, 구간 합 배열을 이용해야 함을 알 수 있음.
# 구간 합 배열이 1차원에서 2차원으로 확장된 것으로 생각하여 구간 합 배열을 어떻게 구성할지 고민하는 것이 이 문제의 핵심!

import sys
input = sys.stdin.readline

# n(리스트 크기), m(질의 수)
# A(원본 리스트), D(합 배열)
n, m = map(int, input().split())
A = [[0] * (n+1)]   # 크기가 n+1인 1차원 배열, 인덱스는 0부터 시작하므로 n+1 까지 선언
D = [[0] * (n+1) for _ in range(n+1)]   # 크기가 (n+1) * (n+1)인 2차원 배열

# 원본 배열 받기
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n+1):     # 합 배열 저장
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j] 

for _ in range(m):     # 질의에 대한 결과 계산 및 출력
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
