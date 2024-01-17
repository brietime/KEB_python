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

# deep copy, shallow copy
a = [1,2,3]
a = b
b = [1,2,4]
print(a,b)

#shallow
subjects = ["a","b","c"]
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
print(subjects, a, b, c, d)
subjects[1] = "x"
print(subjects,  a, b, c, d)

subjects = ["a",["b","c"], "d"]
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
print(subjects, a, b, c, d) # shallow copy하면 mutable값 변화함

#deep

import copy
e = copy.deepcopy(a)
subjects[1][1] = "x"
print(subjects, a, b, c, d, e)

# python tutor 에서 확인

# 리스트 비교
cheezes = ['brie','gjetost','havarti']
for cheeze in cheezes:
    if cheeze.startswith('g'):
        print("I wont eat anything that starts with 'g'")
        break
    else:
        print(cheeze)
        
cheezes = ['brie','gjetost','havarti']
fruits = ['banana','apple','mango']
drinks = ['coffee', 'juice','tea']
desserts = ['tiramisu','macaron','pie','icecream']
for cheeze, fruit, drink, dessert in zip(cheezes, fruits, drinks, desserts):
    print(list((cheezes, fruits, drinks, desserts))
    
    dict(zip(cheezes, fruits, drinks, desserts))
        
# List comprehension
numb_list = []
for i in range(1,6):
    numb_list.append(i)
print(numb_list)

numb_list = [number for number in range(1,6)]
print(numb_list)


# list comprehension
squares = list()
for i in range(1,6):
    squares.append(i*i)
    print(squares)
    
squares = [i*i for i in range(1,6)]
print(squares)

a_list = [number for number in range(1,6) if number % 2 == 1]
a_list
b_list = [number for number in range(1,6) if number % 2 == 0]
b_list

even_squares = [i*i for i in range(1,6) if  i % 2  == 0]
print(even_squares)

rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(cols)
cells = [(row,col)for row in rows for col in cols]
for cell in cells:
    print(cell)
#unpack
for row, col in cells:
    print(row,col)
    
small_birds = ['hummingbird', 'finsh']
extinced_birds = ['dodo, 'passengert pigeon', ]
#page 173 이어서

# dict = 표로 사용 가능?
#no tuple comporehension
