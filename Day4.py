def Merge_arr(arr1,arr2):
    a=len(arr1)
    b=len(arr2)
    
    def Next_gap(gap):
        if gap<=1:
            return 0
        return (gap)//2 + (gap)%2
    gap=a+b
    gap=Next_gap(gap)
    
    while gap > 0:
        i = 0
        j = gap

        while j < (a + b):
            if i < a:
                a_i = arr1[i]
            else:
                a_i = arr2[i - a]

            if j < a:
                a_j = arr1[j]
            else:
                a_j = arr2[j - a]
                
            if a_i > a_j:
                if i < a and j < a:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                elif i < a and j >= a: 
                    arr1[i], arr2[j - a] = arr2[j - a], arr1[i]
                else: 
                    arr2[i - a], arr2[j - a] = arr2[j - a], arr2[i - a]

            i += 1
            j += 1

        gap = Next_gap(gap)

    print(arr1,arr2)

#Test Case1
Merge_arr(arr1 = [1, 3, 5], arr2 = [2, 4, 6])
#Test Case2
Merge_arr(arr1 = [10, 12, 14], arr2 = [1, 3, 5])
#Test Case3
Merge_arr(arr1 = [2, 3, 8], arr2 = [4, 6, 10])
#Test Case4
Merge_arr(arr1 = [1], arr2 = [2])

        
    