x = int(input())

for i in range(1, x+1):
  num = sum((map(int, str(i))))
  num_sum = i + num

  if num_sum == x:
    print(i)
    break
  if i == x:
    print(0)