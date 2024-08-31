x = int(input())

for i in range(x):
  y, z = input().split()
  for i in range(len(z)):
    print(int(y) * z[i], end='')
  print()