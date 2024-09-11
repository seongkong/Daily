import sys

x, y = map(int, input().split())
line = [int(sys.stdin.readline()) for _ in range(x)]
start, end = 1, max(line)

while start <= end:
  mid = (start + end) // 2
  lines = 0
  for i in line:
    lines += i // mid

  if lines >= y:
    start = mid + 1
  else:
    end = mid - 1

print(end)