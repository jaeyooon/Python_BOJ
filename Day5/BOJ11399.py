# ATM에서 모든 사람이 가장 빠른 시간에 인출하는 방법을 그리디 방식으로 해결!
# ATM 앞에 있는 사람 중 인출 시간이 가장 적게 걸리는 사람이 먼저 인출할 수 있도록 순서를 정하는 것이 곧 그리디 방식
# 이를 위해 인출 시간을 기준으로 값을 정렬해야 함.
# N의 최댓값이 1000 이고, 시간 제한이 1초이므로 시간 복잡도가 O(n²)이하인 정렬 알고리즘 중 아무거나 사용해도 됨.
# 여기서는 삽입정렬 이용

N = int(input())    # 사람 수
A = list(map(int, input().split()))
S = [0] * N     # A 합 배열: 각 사람이 인출을 완료하는데 필요한 시간을 저장하기 위한 것

# 삽입 정렬

for i in range(1, N):   # 1~N만큼 반복
    insert_point = i    # 현재 인덱스
    insert_value = A[i]
    for j in range(i-1, -1, -1):    # i-1 ~ 0까지 뒤에서부터 반복
        if A[j] < A[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0

    for j in range(i, insert_point, -1):  # i ~ insert_point+1 까지 뒤에서부터 반복
        A[j] = A[j-1]   # 삽입을 위해 삽입 위치에서 i까지 데이터를 한칸씩 뒤로 shift
    A[insert_point] = insert_value  # 삽입 위치에 현재 데이터 저장

# 합 배열 만들기
S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i]

sum = 0
for i in range(0, N):   
    sum += S[i]     # S 리스트의 각 데이터 값을 모두 합해 결과 출력

print(sum)

