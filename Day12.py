def IsValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        # If it's an opening bracket, push to stack
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False
    return not stack


# Test Cases 1
print(IsValid("()"))
#Test Case 2
print(IsValid("([)]"))
#Test Case 3
print(IsValid("[{()}]"))
#Test Case 4
print(IsValid(""))
#Test Case 5
print(IsValid("{[}"))