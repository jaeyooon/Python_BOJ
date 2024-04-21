# 최소 공배수 구하기  
# 📌최소 공배수는 A와 B가 주어졌을 때 A * B / 최대공약수로 계산해 구할 수 있음  
# 유클리드 호제법을 이용해 최대공약수를 구한 후, 두 수의 곱에서 최대공약수를 나눠주는 방법으로 문제를 풀 수 있음!  

# 최대공약수 구하는 함수
def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

t = int(input())

for i in range(t):
  a, b = map(int, input().split())
  result = a * b // gcd(a, b)
  print(result)