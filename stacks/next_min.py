def days_until_cooler(temps):
    result = [-1] * len(temps)
    stack = []

    for i in range(len(temps) - 1, -1, -1):
        while stack and temps[i] <= temps[stack[-1]]:
            stack.pop()
        if not stack:
            result[i] = -1
        else:
            result[i] = stack[-1] - i
        stack.append(i)
    return result

print(days_until_cooler([30, 60, 90, 120, 60, 30]))  # Expected: [-1, 4, 2, 1, 1, -1]
print(days_until_cooler([100, 95, 90, 85, 80, 75]))  # Expected: [1, 1, 1, 1, 1, -1]
print(days_until_cooler([1]))  # Expected: [-1]