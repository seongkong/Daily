import sys

input = sys.stdin.readline

N, M = map(int, input().split())
add = {}

for i in range(N):
  site, ps = input().split()
  add[site] = ps

for j in range(M):
  print(add[input().rstrip()])