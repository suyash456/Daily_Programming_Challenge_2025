def Sort_0s_1s_2s(arr):
    l, m, h = 0, 0, len(arr) - 1

    while m <= h:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            l=l+1 
            m =m+ 1
        elif arr[m] == 1:
            m =m+ 1
        else: 
            arr[m], arr[h] = arr[h], arr[m]
            h =h-1

    return arr

# Test cases
print(Sort_0s_1s_2s([0, 1, 2, 1, 0, 2, 1, 0]))
print(Sort_0s_1s_2s([2, 2, 2, 2]))
print(Sort_0s_1s_2s([0, 0, 0, 0]))
print(Sort_0s_1s_2s([1, 1, 1, 1]))
print(Sort_0s_1s_2s([2, 0, 1]))
print(Sort_0s_1s_2s([]))
