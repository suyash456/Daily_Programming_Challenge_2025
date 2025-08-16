def Find_Missing_Number(arr):
    if arr[0]!=1:
        return 1
    else:
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]!=1:
                return arr[i-1]+1

        else:
            return arr[len(arr)-1]+1
    
print(Find_Missing_Number([1, 2, 4, 5]))
print(Find_Missing_Number([2, 3, 4, 5]))
print(Find_Missing_Number([1, 2, 3, 4]))
print(Find_Missing_Number([1]))