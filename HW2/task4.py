def get_most_frequent(words, k):
    words_dic = dict.fromkeys(words, 0)
    for i in words:
        words_dic[i] += 1
    list_of_keys = []
    for key in words_dic:
        list_of_keys.append(key)
    if int(k) > len(set(words)):
        print("please enter k<", len(list_of_keys))
    return list_of_keys[:k]


words = ["hello", "world", "hello", "my", "dear", "world", "hello"]
k = 3
print(get_most_frequent(words, k))


