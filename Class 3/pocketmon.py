import sys

x, y = map(int, input().split())

pokedic_int_key = {}
pokedic_name_key = {}

for i in range(x):
  name = sys.stdin.readline().strip()
  pokedic_int_key[i] = name
  pokedic_name_key[name] = i

for j in range(y):
  item = sys.stdin.readline().strip()
  if item.isdigit() == True:
    print(pokedic_int_key[int(item) - 1])
  else:
    print(pokedic_name_key[item] + 1)