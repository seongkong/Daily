from sys import stdin

N, K = map(int, stdin.readline().split())
index = 0
arr = list(range(1, N + 1))
result = []

while len(arr) != 0:
  index += (K - 1)
  index = index % len(arr)
  result.append(arr.pop(index))

print("<", end="")
for i in range(N - 1):
  print(result[i], end=", ")
print(result[N - 1], end = "")
print(">", end = "")