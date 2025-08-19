def Find_Leader(arr):
    Leaders=[]
    max_in_arr=arr[-1]
    Leaders.append(max_in_arr)
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>max_in_arr:
            max_in_arr=arr[i]
            Leaders.append(arr[i])
    return Leaders[::-1]

#Test Case 1   
print(Find_Leader([16, 17, 4, 3, 5, 2]))
#Test Case 2
print(Find_Leader([1, 2, 3, 4, 0]))
#Test Case 3
print(Find_Leader([7, 10, 4, 10, 6, 5, 2]))
#Test Case 4
print(Find_Leader([5]))
#Test Case
print(Find_Leader([100, 50, 20, 10]))