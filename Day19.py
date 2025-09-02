def Evaluate_Postfix(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    
    return stack[0]

# Test Case 1
print(Evaluate_Postfix("5 6 +"))
#Test Case 2
print(Evaluate_Postfix("3 4 2 * 1 5 - 2 3 ^ ^ / +"))
#Test Case 3
print(Evaluate_Postfix("-5 6 -")) 
#Test Case 4
print(Evaluate_Postfix("15 7 1 1 + - / 3 * 2 1 1 + + -")) 
#Test Case 5
print(Evaluate_Postfix("5"))     
