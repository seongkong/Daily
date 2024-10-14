import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**9)

arr = []
while True:
  try:
    x = int(input())
    arr.append(x)
  except:
    break

def post(start, end):
  if start > end:
    return
  mid = end + 1
  for i in range(start + 1, end + 1):
    if arr[i] > arr[start]:
      mid = i
      break
  
  post(start + 1, mid - 1)
  post(mid, end)
  print(arr[start])

post(0, len(arr) - 1)