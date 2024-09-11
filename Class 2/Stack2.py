count = 1
temp = True
stack = []
op = []

x = int(input())
for i in range(x):
  num = int(input())
  while count <= num:
    stack.append(count)
    op.append('+')
    count += 1

  if stack[-1] == num:
    stack.pop()
    op.append('-')
  else:
    temp = False
    break

if temp == False:
  print("N0")
else:
  for i in op:
    print(i)