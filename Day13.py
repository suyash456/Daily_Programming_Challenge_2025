def Longest_Palindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    start=0
    max_len =1
    def expand(l: int, r: int) -> None:
        nonlocal start, max_len
        while l >= 0 and r < n and s[l] == s[r]:
            curr_len = r - l + 1
            if curr_len > max_len or (curr_len == max_len and l < start):
                start, max_len = l, curr_len
            l -= 1
            r += 1
    for i in range(n):
        expand(i, i)
        expand(i, i + 1)  

    return s[start:start + max_len]

#Test case 1
print(Longest_Palindrome("babad"))
#Test case 2
print(Longest_Palindrome("cbbd"))
#Test case 3
print(Longest_Palindrome("a"))  
#Test case 4
print(Longest_Palindrome("aaaa")) 
#Test case 5
print(Longest_Palindrome("abc"))  
