import sys

input = sys.stdin.readline

n = int(input())
arrA = list(map(int, input().split()))
m = int(input())
arrB = list(map(int, input().split()))

common_elemnets = set(arrA) & set(arrB)

if not common_elemnets:
  print(0)
  exit()

result = []
while common_elemnets:
  max_val = max(common_elemnets)
  result.append(max_val)

  idx1 = arrA.index(max_val)
  idx2 = arrB.index(max_val)
  arrA = arrA[idx1 + 1:]
  arrB = arrB[idx2 + 1:]

  common_elemnets = set(arrA) & set(arrB)

print(len(result))
print(*result)