def Longest_Comman_prefix(str):
    if not str:
        return ""

    prefix = str[0]
    
    for s in str[1:]:
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1] 
            if not prefix:
                return ""
    return prefix
#Test Case 1
print(Longest_Comman_prefix( ["flower", "flow", "flight"]))
#Test Case 2
print(Longest_Comman_prefix( ["dog", "racecar", "car"]))
#Test Case 3
print(Longest_Comman_prefix(["apple", "ape", "april"]))
#Test Case 4
print(Longest_Comman_prefix([""]))
#Test Case 5
print(Longest_Comman_prefix( ["alone"]))