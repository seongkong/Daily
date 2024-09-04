import sys

x = int(sys.stdin.readline())

lst = []

for i in range(x):
  lst.append(sys.stdin.readline().strip())

set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)

for j in lst:
  print(j)