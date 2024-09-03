num = int(input())
score = list(map(int, input().split()))
high = max(score)

for i in range(num):
  score[i] = score[i]/high * 100


print(sum(score)/num)