n = int(input())
m = int(input())
s = input()
p = 'IO' * n + 'I'

answer = 0

for i in range(m - len(p) + 1):
  if s[i] == 'I':
    if s[i:i + len(p)] ==  p:
      answer += 1

print(answer)