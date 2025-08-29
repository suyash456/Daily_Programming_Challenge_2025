def Longest_Substr_Without_Repeated_Char(s):
    char_index = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1 
        char_index[s[end]] = end 
        max_length = max(max_length, end - start + 1)
    return max_length
# Test case 1
print(Longest_Substr_Without_Repeated_Char("abcabcbb"))
# Test case 2
print(Longest_Substr_Without_Repeated_Char("bbbbb")) 
# Test case 3
print(Longest_Substr_Without_Repeated_Char("pwwkew"))  
# Test case 4
print(Longest_Substr_Without_Repeated_Char("abcdefgh"))  
# Test case 5
print(Longest_Substr_Without_Repeated_Char("a")) 

