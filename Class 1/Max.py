MAX = []
check = 0
location = 0

for i in range(9):
  MAX.append(input())

for j in range(len(MAX)):
  if check <= int(MAX[j]):
    check = int(MAX[j])
    location = j + 1

print(check)
print(location)