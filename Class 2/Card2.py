from collections import deque

def find_last_card(x):
  queue = deque(range(1, x+1))

  while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
  return queue[0]

x = int(input())
print(find_last_card(x))