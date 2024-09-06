import sys
input = sys.stdin.readline

x = int(input())
li = []

for i in range(x):
  li.append(int(input()))

for j in sorted(li):
  print(j)