from sys import stdin

n = int(input())
arr = list(map(int, stdin.readline().split()))
maxdp = arr
mindp = arr

for _ in range(n - 1):
  arr = list(map(int, stdin.readline().split()))
  maxdp = [arr[0] + max(maxdp[0], maxdp[1]), arr[1] + max(maxdp), arr[2] + max(maxdp[1], maxdp[2])]
  mindp = [arr[0] + min(mindp[0], mindp[1]), arr[1] + min(mindp), arr[2] + min(mindp[1], mindp[2])]

print(max(maxdp), min(mindp))