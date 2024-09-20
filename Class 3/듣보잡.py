x,y = map(int, input().split())

a = set()
for i in range(x):
  a.add(input())

b = set()
for j in range(y):
  b.add(input())

result = sorted(list(a&b))

print(len(result))

for k in result:
  print(k)