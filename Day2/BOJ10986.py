# 나머지 합 문제
# 나머지 합 문제 풀이의 핵심 아이디어
# => (A+B)%C 는 ((A%C)+(B%C))%C 와 같음!
# 구간 합 배열의 원소를 M으로 나눈 나머지로 업데이트하고
# S[i]와 S[j]가 같은 (i, j)쌍을 찾으면 원본 리스트에서
# j+1 부터 i까지의 구간 합이 M으로 나누어떨어진다는 것을 알 수 있음.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())    # n: 수열의 개수, m: 나누어떨어져야 하는 수
A = list(map(int, input().split()))     # A: 원본 수열 저장 리스트
S = [0] * n     # S: 합 배열 선언
C = [0] * m     # C: 같은 나머지의 인덱스를 카운트하는 리스트, m으로 나누었을 때의 나머지 중에 카운트하는 것이므로 m보다 리스트 항목 수가 많을 수 없음!
answer = 0

S[0] = A[0]     # 합 배열의 첫 번째 값은 원본 배열의 첫 번째 값으로 넣어줘야 함!
for i in range(1, n):   # 1 ~ n-1
    S[i] = S[i-1] + A[i]    # 합 배열 구하기

for i in range(n):      # 0 ~ n-1
    remainder = S[i] % m    # 합 배열을 M으로 나눈 나머지 값
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(m):
    if C[i] > 1:     # 적어도 같은 나머지 값을 갖는 애들이 2개 이상있으면 
        answer += (C[i]*(C[i]-1) // 2)      # 이들 중 2가지를 뽑는 경우의 수를 정답에 더함

print(answer)