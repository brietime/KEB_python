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
            i % k ==  0
            is_prime = False
            break
        k += 1
        # print(i, end = ' ') #loop count
    if is_prime:
        pass
        
# tuple(immutable) /list(mutable) -sequencial
# tuple  
t1 = (5) 
t2 = (5,) # ,
t3 = 5, # () is option
t4 = (5, 7)
t5 = 5, 7 
t6 = "python", "kim" # packing
print(type(t1),type(t2),type(t3),type(t4),type(t5),type(t6)) 
print(type(t6),t6[1])
subject , professor = t6 # unpacking
a, b, c = t6 # ValueError: not enough values to unpack (expected 3, got 2)

print(professor)
print(subject)

t7 = ()
t8 = tuple()
print(type(t7), type(t8), type(9,), type((9,)))

print(type('ksdf',)) # ????????
print(type(('ksdf',)))

dffs_list = ['dsjf','sjhdnf','qiwedj']
dffs_tuple = tuple(dffs_list)

t9 = 1,2,3
t10 = 1,2,3,1
print(t9 == t10)
print(t9 <= t10)
print(t9 < t10)

words = ('fresh', 'milk', 'juice')

t11 = 4.43, 
t12 = 3.98, 4.1, 3.27
print(id(t11))
t11 = t11 + t12 # 할당 & 업데이트 
print(id(t11))
print(t11) 

# List