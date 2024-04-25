# ⭐유니온 파인드 문제

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, m = map(int, input().split())    # n 원소 개수, m 질의 개수  
parent = [0] * (n + 1)    # 대표 노드 저장 리스트

def find(a):  # find 연산
  if a == parent[a]:    # a가 대표노드면 리턴
    return a
  else:
    parent[a] = find(parent[a])   # 재귀 형태로 구현 => 경로 압축 부분
    return parent[a]
  
def union(a, b):    # union 연산 대표 노드끼리 합치기
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a

def checkSame(a, b):    # 두 원소가 같은 집합에 속해 있는지 확인하는 함수
  a = find(a)
  b = find(b)
  if a == b:
    return True
  return False

for i in range(0, n + 1):   # 대표노드를 자기 자신으로 초기화
  parent[i] = i

for i in range(m):
  question, a, b = map(int, input().split())
  if question == 0:
    union(a, b)
  else:
    if checkSame(a, b):
      print("YES")
    else:
      print("NO")