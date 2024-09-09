x = int(input())

stack = []

for i in range(x):
  a = int(input())
  if a == 0:
    stack.pop()
  else:
    stack.append(a)

print(sum(stack))