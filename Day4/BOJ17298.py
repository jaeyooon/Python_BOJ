# N의 최대 크기가 1000000이므로 반복문으로 오큰수를 찾으면 제한 시간을 초과함! 
# 스택에 다음 아이디어를 추가하여 문제 풀어보기
# - 스택에 새로 들어오는 수가 top에 존재하는 수보다 크면 그 수는 오큰수가 됨.
# - 오큰수를 구한 후 수열에서 오큰수가 존재하지 않는 숫자에 -1을 출력해야 함.

n = int(input())    # 수열 개수
ans = [0] * n   # 정답 리스트
A = list(map(int, input().split()))     # 수열 리스트 채우기
myStack = []    # 스택 선언

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]: # 오큰수 조건(현재 들어가려는 값이 스택의 top 위치에 있는 값보다 클 경우 반복)
        ans[myStack.pop()] = A[i]   # 스택에서 pop한 값을 인덱스로 하는 ans 리스트에 현재 값 저장
    myStack.append(i)   # 현재 들어가려고 한 인덱스를 스택에 저장

while myStack:  # 스택이 빌 때 까지
    ans[myStack.pop()] = -1

result = ""
for i in range(n):
    result += str(ans[i]) + " "

print(result)