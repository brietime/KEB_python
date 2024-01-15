univ = "Inha university"

print(univ)
print(univ[5])

# univ[5] = 'U' //immutable
# print(univ) #변경안됨

subjects = ['python','c++', 'linux', 'data structure', 'database']
print(subjects)
print(subjects[3])

subjects[3] = 'data structure & algorithm' #mutable
print(subjects[3])

# frozenset is not mutable 

# print(0.1)
# print(1e-1)
# print(21000)

abc = 7
Abc = 8
ABC = 6 # case sensitive in lower & upper case letters

test9 = 77
# 9test = 77 #no num can start as var
_9test =71 #okay in underline

# False = 123 #no keywords 

x = 2
y = x + 5
print(y)

print(type(3.14))
print(isinstance(3.14, float))
print(isinstance("Inha", float))

artists = ['bts','뉴진스', '핑클','ses', 'hot','블랙핑크']
groups = artists
print(artists, groups)
artists[2] = '세븐틴'
print(artists, groups)

money = 5,000,000
print(money)
print(type(money)) #tuple

cash = 5_000_000
print(cash)
print(type(cash)) #int

base_number = int(input('Input base number: '))
exponent_number = int(input('Input exponent number: '))
print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number ** exponent_number}')