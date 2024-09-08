import sys
input = sys.stdin.readline

x = int(input())

arr = []

for i in range(x):
  [a, b] = map(int, input().split())
  arr.append([a, b])

a_arr = sorted(arr)

for j in range(x):
  print(a_arr[j][0], a_arr[j][1])