# 2개의 수 사이 소수 판정
numbers = input("first number Second number: ").split()
    n1 = int(numbers[0])
    n2 = int(numbers[1])

    if n1 > n2:
        n1,n2 = n2,n1
            
    for i in range(n1,n2+1,1):
        is_prime = True
            
        if i < 2:
            pass
        
        else: 
            k = 2
            while k*k <= i: # performance issue
                i % k ==  0:
                is_prime = False
                break
            k += 1
            # print(i, end = ' ') #loop count
        if is_prime:
            pass

