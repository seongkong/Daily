x = int(input())
y = input()
z = 0

for i in range(x):
  z += (ord(y[i]) - 96) * (31 ** i)
print(z % 1234567891)