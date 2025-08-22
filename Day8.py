def Reverse_str_word_by_word(s):
    words = []
    word = ""
    i = 0
    while i < len(s):
        if s[i] != " ": 
            word += s[i]
        else:
            if word:
                words.append(word)
                word = ""
        i += 1
    if word:  
        words.append(word)

    reversed_str = ""
    for j in range(len(words)-1, -1, -1):
        reversed_str += words[j]
        if j != 0:
            reversed_str += " "
    return reversed_str
#Test Case 1
print(Reverse_str_word_by_word("the sky is blue"))
#Test Case 2
print(Reverse_str_word_by_word("  hello world  "))
#Test Case 3
print(Reverse_str_word_by_word("a good   example"))
#Test Case 4
print(Reverse_str_word_by_word(""))
#Test Case 5
print(Reverse_str_word_by_word("word"))