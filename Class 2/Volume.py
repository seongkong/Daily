num = int(input())
lst = []

for i in range(num):
  weight, height = map(int, input().split())
  lst.append((weight, height))

for j in lst:
  rank = 1
  for k in lst:
    if j[0] < k[0] and j[1] < k[1]:
      rank += 1
  print(rank, end = " ")