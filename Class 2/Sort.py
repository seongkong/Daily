import sys 

x = int(sys.stdin.readline())
num = [0] * 10001

for i in range(x):
  num[int(sys.stdin.readline())] += 1

for j in range(10001):
  if num != 0:
    for k in range(num[j]):
      print(j)