def Prime_Factors_Of_Num(n):
    prime_factors=[]
    i=2
    while i<=n:
        if n%i==0:
            prime_factors.append(i)
            n=n/i
        else:
            i=i+1
    return prime_factors
#Test case 1
print(Prime_Factors_Of_Num(30))
print(Prime_Factors_Of_Num(49))
print(Prime_Factors_Of_Num(19))
print(Prime_Factors_Of_Num(64))
print(Prime_Factors_Of_Num(123456))
