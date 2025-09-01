def Count_Divisors(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count
print(Count_Divisors(12))
#Test Case 1
print(Count_Divisors(18))
#Test Case 2
print(Count_Divisors(29))
#Test Case 3
print(Count_Divisors(100))
#Test Case 4
print(Count_Divisors(1))
#Test Case 5
print(Count_Divisors(997))