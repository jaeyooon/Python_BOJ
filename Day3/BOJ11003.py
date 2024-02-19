import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())    # N: 데이터 개수, L: 최솟값을 구하는 범위
mydeque = deque()  # 데이터를 담을 덱 자료구조
now = list(map(int, input().split()))   # 주어진 숫자 데이터를 가지는 리스트

for i in range(N):
    # 1) 나보다 큰 데이터 삭제하기
    while mydeque and mydeque[-1][0] > now[i]:   # 덱의 마지막 위치[-1]에 있는 값[0]이 현재 리스트에 있는 값보다 크면
        mydeque.pop()
    mydeque.append((now[i], i))     # 덱의 마지막 위치에 현재 값 저장
    # 2) 슬라이딩 윈도우 벗어난 데이터 삭제
    if mydeque[0][1] <= i-L:    # 덱의 제일 앞에 위치한[0] 것의 인덱스[1] 에서부터 L의 범위를 벗어나면
        mydeque.popleft()   # 덱의 앞에서 삭제하는 것이므로 popleft()
    print(mydeque[0][0], end=' ')   # 덱에서 제일 앞에 위치한 인덱스의 값[0]을 출력