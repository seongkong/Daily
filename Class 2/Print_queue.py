x = int(input())
arr = []

for i in range(x):
  y, z = map(int, input().split())
  arr = list(enumerate(list(map(int, input().split()))))
  v = arr[z]
  result = 0

  while len(arr):
    max_v = max([i[1] for i in arr])
    if arr[0][1] == max_v:
      now = arr.pop(0)
      result += 1
      if now == v:
        print(result)
        break
    else:
      now = arr.pop(0)
      arr.append(now)