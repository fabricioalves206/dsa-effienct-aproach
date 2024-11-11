def check_anagram(list1, list2):
    sorted_tuple1 = set(tuple(sorted(word)) for word in list1)
    sorted_tuple2 = set(tuple(sorted(word)) for word in list2)
    common_tuples = sorted_tuple1 & sorted_tuple2
    list1_output = [word for word in list1 if tuple(sorted(word)) in common_tuples]
    list2_output = [word for word in list2 if tuple(sorted(word)) in common_tuples]
    output = []
    for word1 in list1_output:
        for word2 in list2_output:
            if tuple(sorted(word2)) == tuple(sorted(word1)):
                output.append((word1, word2))
    return output

list1 = ['amor', 'amostrei']
list2 = ['roma', 'mora', 'atiremos', 'porta', 'iteramos']

print(check_anagram(list1, list2))