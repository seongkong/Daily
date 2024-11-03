N = int(input())
liquids = list(map(int, input().split()))

min_val = float('inf')
answer = [float('inf'), float('inf')]
left, right = 0, N - 1
while left < right:
    if abs(liquids[left] + liquids[right]) < min_val:
        min_val = abs(liquids[left] + liquids[right])
        answer = [liquids[left], liquids[right]]

    if liquids[left] + liquids[right] < 0:
        left += 1
    else:
        right -= 1
print(*answer)