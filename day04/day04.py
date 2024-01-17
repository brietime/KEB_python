# 2개의 수 사이 소수 판정
numbers = input("first number Second number: ").split()
n1 = int(numbers[0]) # 임시 튜플
n2 = int(numbers[1]) # "

if n1 > n2: # 튜플 아님
    n1,n2 = n2,n1
        
for i in range(n1,n2+1,1):
    is_prime = True
        
    if i < 2:
        pass
    
    else: 
        k = 2
        while k*k <= i: # performance issue
            if i % k ==  0:
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

# ' '먼저 함수로 인식하기 때문에 ()로 감싸주지 않으면 , 인식을 함수 인식 후에
print(type('ksdf',)) # ????????
print(type('ksdf',))
print(type(('ksdf',)))

# 튜플로 변환
dffs_list = ['dsjf','sjhdnf','qiwedj']
dffs_tuple = tuple(dffs_list)

# 비교연산 - 개수비교x, 순서대로 숫자 비교
t9 = 1,4,3
t10 = 1,2,3,1 
print(t9 == t10)
print(t9 <= t10)
print(t9 < t10)

words = ('fresh', 'milk', 'juice')
for word in words:
    print(word)
    
t11 = 4.43, 
t12 = 3.98, 4.1, 3.27
print(id(t11))
t11 = t11 + t12 # 할당 & 업데이트 
print(id(t11))
print(t11) 

# List
a_tuple = ('ready','or','not')
list(a_tuple) # ['ready', 'or', 'not']
list('cat') # ['c', 'a', 't']

subjects = ["c++", "java", " python"]
print(subjects[::-1])
subjects = subjects[::-1]
print(subjects)
subjects[4:]
subjects[-6:]
subjects[-6:-2]
subjects[-6:-4]

# 항목 추가
subjects.append("database")
subjects.insert(2,"data structure")

others = ["data structure", "database"]
subjects.extend(others)
subjects += others
    
subjects[:]

#항목 바꾸기
subjects[2] = 'AI'

# 슬라이싱  추가
numbers = [1,2,3,4]
numbers[1:3] = [8,9]
numbers

numbers[1:3] = [7,8,9]
numbers[1:3] = (12,32,56)
numbers[1:3] = 'wat?'
numbers

# 삭제
del numbers[-1]
numbers.remove('t')
numbers.pop() # 맨 뒤 pop
numbers.pop(2) # 해당 위치 pop
numbers

numbers.clear()
numbers

# 인덱스
numbers = [1,2,3,4]
numbers.index(3) #예외처리 value error, 다른건 -1 반환
4 in numbers #boolean

numbers.count(2)
# join, seperate
'/ '.join(subjects)

seperator = '*'
joined = seperator.join(subjects)
joined
seperated = joined.split(seperator)
seperated
seperated == subjects

# sort() 정렬
subjects.sort()
subjects

subjects = ['c++', '5', 'data structure', '하늘','database', '구연산', 'java', '9']
subjects.sort(reverse = True)
subjects

copy_subjects = sorted(subjects)
print(copy_subjects,subjects)

# len() 길이
subjects = ['c++', '5', 'data structure', '하늘','database', '구연산', 'java', '9']
print(len(subjects))
