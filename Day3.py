# def Find_Duplicate(arr):
#     duplicate=0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]==arr[j]:
#                 duplicate=arr[i]
                
#     return duplicate

# #Test Cases
# print(Find_Duplicate([1, 3, 4, 2, 2]))
# print(Find_Duplicate( [3, 1, 3, 4, 2]))
# print(Find_Duplicate( [1,1]))
# print(Find_Duplicate( [1,4,4,2,3]))

# #Time Complexity: O(n^2)
# #Space Complexity: O(1)


def Find_Duplicate(arr):
    slow = arr[0]
    fast = arr[0]

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
        
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow

#Test Cases
print(Find_Duplicate([1, 3, 4, 2, 2]))
print(Find_Duplicate( [3, 1, 3, 4, 2]))
print(Find_Duplicate( [1,1]))
print(Find_Duplicate( [1,4,4,2,3]))
#Time Complexity: O(n)
#Space Complexity: O(1)