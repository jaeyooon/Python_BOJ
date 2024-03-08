# N의 최대 범위가 500000이므로 버블정렬을 사용하면 버블정렬의 시간복잡도는 N²이므로 제한 시간을 초과함!
# => 이 문제는 버블정렬이 아닌 O(nlogn)의 시간 복잡도를 가진 병합정렬을 사용해야 함!
# 병합정렬은 두 그룹을 병합하는 과정에 버블정렬의 swap이 포함되어 있음

import sys
input = sys.stdin.readline
result = 0

def merge_sort(s, e):   # s 시작점 e 종료점 m 중간점
    global result
    # 재귀 함수 형태로 구현
    if e-s < 1: return      # 더 이상 반으로 자를 수 없을 경우
    m = int(s+(e-s) / 2)    #반으로 자름
    merge_sort(s, m)
    merge_sort(m+1, e)

    for i in range(s, e+1):
        tmp[i] = A[i]   # tmp에 A배열 값을 그대로 넣음
    
    k = s   # k변수는 A배열에서 어느 위치에 데이터가 들어가야되는지 나타내주는 인덱스
    # 투 포인터
    index1 = s
    index2 = m+1
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k    # ✨swap 값 카운트, index2 - k는 현재 앞의 데이터셋에 남아있는 데이터의 개수를 의미
            k += 1
            index2 += 1 # swap 되었으므로 포인터 이동
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())    # 정렬할 수 개수
A = list(map(int, input().split()))     # 정렬할 리스트 선언
A.insert(0,0)   # 첫번째 인덱스에 0 값 넣어줌
tmp = [0] * int(N+1)    # 정렬할 때 잠시 사용할 임시 리스트 선언

merge_sort(1, N)     # 첫번째 인덱스부터 N번째 인덱스까지 병합 정렬
print(result)
