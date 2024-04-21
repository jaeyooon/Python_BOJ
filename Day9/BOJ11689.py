# ⭐오일러 피 함수 구현하기  
# 문제에서 요구하는 GCD(n, k) = 1 을 만족하는 자연수의 개수 👉 오일러 피 함수의 정의  

import math
n = int(input())  # n 소인수 표현  
result = n  # 결괏값 

for p in range(2, int(math.sqrt(n) + 1)):   # 제곱근까지만 진행
  if n % p == 0:
    result -= result // p    # 결괏값 업데이트 
    while n % p == 0:
      n //= p    # n에서 현재 소인수 내역 제거

if n > 1:   # n이 마지막 소인수일 때
  result -= result // n

print(result)