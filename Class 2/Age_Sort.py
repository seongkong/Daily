x = int(input())
member = []

for i in range(x):
  age, name = input().split()
  member.append([int(age), name])

for j in sorted(member, key = lambda y : y[0]):
  print(j[0], j[1])