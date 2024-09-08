x = int(input())
y = list(map(int, input().split()))
z = int(input())

arr = list(map(int, input().split()))

y.sort()

for i in arr:
  lt, rt = 0, x - 1
  isExist = False

  while lt <= rt:
    mid = (lt + rt) // 2
    if i == y[mid]:
      isExist = True
      print(1)
      break
    elif i > y[mid]:
      lt = mid + 1
    else:
      rt = mid - 1

  if not isExist:
    print(0)