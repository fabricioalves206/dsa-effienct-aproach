# problem : find the elements that don't have duplicates

def non_repeating_elements(nums):
    seen, repeated = set(), set()
    for num in nums:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)
    return list(seen - repeated)

nums = [1,2,1,4,2,7]

print(non_repeating_elements(nums))