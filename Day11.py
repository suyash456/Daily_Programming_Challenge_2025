def Permutations_of_a_String(s, answer=""):
    permutations = []
    if len(s) == 0:
        permutations.append(answer)
        return permutations
    for i in range(len(s)):
        ch = s[i]
        left = s[:i]
        right = s[i+1:]
        permutations += Permutations_of_a_String(left + right, answer + ch)
    return permutations
print(Permutations_of_a_String("abc"))


    
