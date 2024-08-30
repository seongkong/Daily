x = int(input())
y = int(input())
z = int(input())

sum = list(str(x * y * z))

for i in range(0, 10):
  count = 0
  for num in sum:
    if i == int(num):
      count += 1
    
  print(count)