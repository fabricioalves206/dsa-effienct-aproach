# problem : given 2 lists, find the elements that exist in just one of them

def unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    unique_list1 = sorted(list(set1 - set2))
    unique_list2 = sorted(list(set2 - set1))
    return (unique_list1, unique_list2)


list1 = [1,2,3,5]
list2 = [6,7,1,2]

print(unique_elements(list1, list2))