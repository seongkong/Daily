import sys

sys.setrecursionlimit(1000000000)
n, r, q = map(int, sys.stdin.readline().split(' '))

m = [[] for _ in range(n + 1)]
visit = [-1 for _ in range(n + 1)]

for _ in range(n - 1):
  a, b = map(int, sys.stdin.readline().split(' '))
  m[a].append(b)
  m[b].append(a)

def dfs(now):
  global visit
  visit[now] = 1
  for i in m[now]:
    if visit[i] == -1:
      visit[now] += dfs(i)
  return visit[now]

dfs(r)
for _ in range(q):
  get = int(sys.stdin.readline())
  print(visit[get])