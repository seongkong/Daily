x = int(input())
cnt = 0

while(x > 1):
  cnt += x // 5
  x = x // 5
  

print(cnt)