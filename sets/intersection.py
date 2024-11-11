# problem : find the common elements from 2 differents arrays.
# It's faster if we cast from list to set
# Sets are unordered, so we need to sort it.

def intersection(list1: list, list2: list) -> list:
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    return sorted(list(intersection))

list1 = [1,2,4,5,7]
list2 = [4,12,45,2,1]

print(intersection(list1, list2))