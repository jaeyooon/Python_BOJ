# 숫자의 개수만큼 입력받은 값을 리스트 형태로 저장 => list(input())
# numbers 리스트를 탐색하여 각 값을 정수형으로 변환하고 결과값에 더하여 누적함.
# 📌파이썬에서 리스트는 배열의 특징을 모두 가지고 있기 때문에 index로 접근할 수 있음.

N = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum = sum + int(i)

print(sum)