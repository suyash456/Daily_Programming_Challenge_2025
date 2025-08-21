def Trapping_Rain_Water(arr):
    left, right = 0, len(arr) - 1
    max_left=0
    max_right=0
    trapped_water = 0

    while left < right:
        if arr[left] < arr[right]:
            if arr[left] >= max_left:
                max_left = arr[left]
            else:
                trapped_water += max_left - arr[left]
            left += 1
        else:
            if arr[right] >= max_right:
                max_right = arr[right]
            else:
                trapped_water += max_right - arr[right]
            right -= 1

    return trapped_water

# Test Case 1
print(Trapping_Rain_Water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
#Test Case 2
print(Trapping_Rain_Water([4, 2, 0, 3, 2, 5]))
#Test Case 3
print(Trapping_Rain_Water([1,1,1]))
#Test Case 4
print(Trapping_Rain_Water([5]))
print(Trapping_Rain_Water([2,0,2]))
