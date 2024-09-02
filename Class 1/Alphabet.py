x = list(input())
y = 'abcdefghijklmnopqrstuvwxyz'

for i in y:
  if i in x:
    print(x.index(i), end = ' ')
  else:
    print(-1, end= ' ')
