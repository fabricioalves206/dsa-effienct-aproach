# problem : determine the preceding smaller value for every number on the list
def smaller_number(numbers: list) -> list:
    result = [-1]
    stack = []
    for num in numbers:
        while stack and stack[-1] >= num:
            stack.pop()
        if not stack:
            result.append(-1)
            stack.append(num)
        else:
            result.append(stack[-1])
    return result[1:]

# problem : determine the closest smaller value for every number on the list
def smaller_closest_number(numbers: list) -> list:
    result = [-1]
    stack = []
    for num in numbers:
        while stack and stack[-1] >= num:
            stack.pop()
        result.append(stack[-1] if stack else -1)
        stack.append(num)
    return result[1:]

numbers = [5,6,7,3,6,8,10,2,6,12]
print(numbers)
print(smaller_number(numbers))
print(smaller_closest_number(numbers))

