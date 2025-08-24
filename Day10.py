def Group_Anagrams(strs):
    anagram_map = {} 
    
    for word in strs:
        key = ''.join(sorted(word))
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(word)
    
    return list(anagram_map.values())

#Test Case 1
print(Group_Anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
#Test Case 2
print(Group_Anagrams([""]))
#Test Case 3
print(Group_Anagrams( ["a"]))
#Test Case 4
print(Group_Anagrams(["abc", "bca", "cab", "xyz", "zyx", "yxz"]))
#Test Case 5
print(Group_Anagrams(["abc", "def", "ghi"]))