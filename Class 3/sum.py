n, m = map(int, input().split())

num = list(map(int, input().split()))
sum = [0]
tmp = 0

for i in num:
  tmp = tmp + i
  sum.append(tmp)

for _ in range(m):
  i, j = map(int, input().split())
  print(sum[j] - sum[i - 1])