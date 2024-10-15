import sys

s = sys.stdin.readline().rstrip()
explosion_string = sys.stdin.readline().rstrip()

stack = []
ex_len = len(explosion_string)

for i in range(len(s)):
  stack.append(s[i])
  if ''.join(stack[-ex_len:]) == explosion_string:
    for _ in range(ex_len):
      stack.pop()

if stack:
  print(''.join(stack))
else:
  print('FRULA')