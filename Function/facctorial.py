def cal_fact(n):    
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)

# call function 
cal_fact(5)
