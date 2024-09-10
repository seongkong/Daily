import sys

def my_round(val):
  if val - int(val) >= 0.5:
    return int(val) + 1
  else:
    return int(val)
  
x = int(sys.stdin.readline().strip())
if x:
  level = []
  for i in range(x):
    level.append(int(sys.stdin.readline().strip()))

  xx = my_round(x * 0.15)
  level.sort()
  if xx > 0:
    print(my_round(sum(level[xx:-xx])/len(level[xx:-xx])))
  else:
    print(my_round(sum(level)/len(level)))
else:
  print(0)