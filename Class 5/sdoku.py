import sys
input = sys.stdin.readline

def row_check(row, num):
  for col in range(9):
    if arr[row][col] == num:
      return False
  return True

def col_check(col, num):
  for row in range(9):
    if arr[row][col] == num:
      return False
  return True

def square_check(row, col, num):
  r = row // 3 * 3
  c = col // 3 * 3

  for a in range(3):
    for b in range(3):
      if arr[r + a][c + b] == num:
        return False
  return True

def dfs(idx):
  if idx == len(zero_idx):
    for i in range(9):
      for j in range(9):
        print(arr[i][j], end = "")
      print()
    exit()
  
  x, y = zero_idx[idx]

  for n in range(1, 10):
    if row_check(x, n) and col_check(y, n) and square_check(x, y, n):
      arr[x][y] = n
      dfs(idx + 1)
      arr[x][y] = 0

arr = [list(map(int, input().rstrip())) for _ in range(9)]
zero_idx = []
for i in range(9):
  for j in range(9):
    if not arr[i][j]:
      zero_idx.append((i, j))

dfs(0)