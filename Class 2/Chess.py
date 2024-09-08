x, y = map(int, input().split())

mtr = []
cnt = []

for i in range(x):
  mtr.append(input())

for j in range(x - 7):
  for k in range(y - 7):
    a_index = 0
    b_index = 0
    for h in range(j, j+8):
      for g in range(k, k+8):
        if (h+g)%2 == 0:
          if mtr[h][j] != 'W':
            a_index += 1
          else:
            b_index += 1
        else:
          if mtr[h][g] != 'W':
            b_index += 1
          else:
            a_index += 1


    cnt.append(a_index)
    cnt.append(b_index)
print(min(cnt))