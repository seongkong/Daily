import sys

input = sys.stdin.readline

string = [input().strip() for i in range(3)]

for j in range(2, -1, -1):
  if string[j].isdigit():
    answer = int(string[j]) + (3 - j)
    break

if answer % 15 == 0:
  print('FizzBuzz')
elif answer % 3 == 0:
  print('Fizz')
elif answer % 5 == 0:
  print('Buzz')
else:
  print(answer)