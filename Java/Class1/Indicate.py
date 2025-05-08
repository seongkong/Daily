number = list(map(int, input().split()))

result = 0

for num in number:
  result += num**2

print(result%10)