# def Find_LCM(n,m):
#     i=max(n,m)
#     while True:
#         if i%n==0 and i%m==0:
#             return i
#         i+=1
# #Test Case 1
# print(Find_LCM(4,6))
# #Test Case 2
# print(Find_LCM(5,10))
# #Test Case 3
# print(Find_LCM(7,3))
# #Test Case 4
# print(Find_LCM(1,987654321))
# #Test Case 5
# print(Find_LCM(123456,789012))


def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

def Find_LCM(n, m):
    return (n * m) // gcd(n, m)
#Test Case 1
print(Find_LCM(4,6))
#Test Case 2
print(Find_LCM(5,10))
#Test Case 3
print(Find_LCM(7,3))
#Test Case 4
print(Find_LCM(1,987654321))
#Test Case 5
print(Find_LCM(123456,789012))