def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1 
            lst.append(word)
    print("list of wrd with 1st and last same\n", lst)
    return ctr

count = match_words(['abc', 'cfc','xyz','aba','1826'])
print("num of word having 1st and last chracter same are:",count)