x = []

for i in range(10):
  a = int(input())
  b = a % 42
  x.append(b)

y = set(x)
print(len(y))