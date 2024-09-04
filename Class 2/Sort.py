import sys

x = int(sys.stdin.readline())
num = []

for i in range(x):
  num.append(int(sys.stdin.readline()))

sorted_list = sorted(num)

for j in sorted_list:
  print(j)