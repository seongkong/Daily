data = []

for i in range(int(input())):
  x, y = map(int, input().split())
  data.append((x, y))

data.sort(key = lambda x : (x[1], x[0]))

for j in data:
  print(j[0], j[1])