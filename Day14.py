def Substring_With_K_Distinct_Element(s, k):
    substr = []
    n = len(s)
    for i in range(n):
        substs = ""
        for j in range(i, n):
            substs += s[j]
            if len(set(substs)) == k:
                substr.append(substs)
    return len(substr)
#Test Case 1
print(Substring_With_K_Distinct_Element(s = "pqpqs", k = 2))
#Test Case 2
print(Substring_With_K_Distinct_Element(s = "aabacbebebe", k = 3))
#Test Case 3
print(Substring_With_K_Distinct_Element(s = "a", k = 1))
#Test Case 4
print(Substring_With_K_Distinct_Element(s = "abc", k = 3))
#Test Case 5
print(Substring_With_K_Distinct_Element(s = "abc", k = 2))
