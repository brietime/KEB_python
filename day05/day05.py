# Key = immutable(tuple o, list x)
# dict comprehenshion

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts

univ = 'inha university'
counts_alphabet = dict()
for letter in univ:
    counts_alphabet[letter] = univ.count(letter)
print(counts_alphabet)

# SET 
reindeer = set(['1','2','3'])
reindeer.add('4')
print(reindeer)

#immutable set - frozen set : 읽기전용

drinks = {
'martini' : {'vodka','vermouth'},
'black rassian': {'vodka','kaluah'},
'white rassian': {'vodka','kaluah'},
'manhattan': {'rye','vermouth','bitters'},
'screwdriver':{'orange juice','vodka'}
}

print(not drinks['screwdriver'] & {'vermouth','vodka'})

# Def

# 단일책임원칙 -하나의 클래스가 만들어지면 하나의 일을 잘 해야 함! (한가지 기능에 충실하자)
# prime number with function

def isprime(n) -> bool:
    """
    매개변수로 넘겨받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """
    if n < 2:
        return False
    else:
        i=2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1   
        return True      
    
      
numbers = input("first number Second number: ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1,n2 = n2,n1
    
for number in range(n1, n2 +1):
    if isprime(number):
        print(number, end = ' ')
        
        
# menu with func
def isprime(n) -> bool:
    """
    매개변수로 넘겨받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """
    if n < 2:
        return False
    else:
        i=2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1   
        return True      
    
while True:
    menu = input("1) fahrenheit -> celsius  2) Celsius -> fahrenheit  3) Prime number  4) Prime numbers(two input)  5) Quit Program : ")
    
    if menu  == '1':
        fahrenheit = float(input('Input fahrenheit: '))
        print(f'Fahrenheit: {fahrenheit}F, Celsius: {((fahrenheit-32.0)*5.0/9.0):.4f}C')
    
    elif menu == '2':
        celsius = float(input('Input Celcius: '))
        print(f'Celsius: {celsius}C, fahrenheit: {((celsius *9.0/5.0)+32.0):.4f}F')
    
    elif menu == '3':
        number = int(input("Input number: "))
        for i in range(2, number): 
            if isprime(number):
                print(f'{number} is prime number.')
            else: 
                print(f'{number} is NOT prime number')
        
    elif menu == '4':
        numbers = input("first number Second number: ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1,n2 = n2,n1
            
        for number in range(n1,n2+1,1):
            if isprime(number):
                print(number, end = ' ')
        print()
    
    elif menu == '5':
        print('Terminate Program.')
        break
    
    else: 
        print('Invaild Syntax!')
        
        
# def2
thing = None
if thing:
    print("it's some thing")
else: 
    print("It's nothing")

thing = None
if thing is None:
    print("it's nothing")
else: 
    print("Its some thing")
    
# 기본이 비어있는 값, != None

def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing is not None:
        print(thing, "is True") # 비어있는 값임
    else: 
        print(thing, "is False")
        

whatis(None)
whatis(True)
whatis(False)
whatis(0)
whatis(0.0)
whatis('')
whatis(())

def menu(wine, entree, dessert):
    return{'wine':wine, 'entree': entree, 'dessert':dessert}

menu('chardonnay','chicken','cake')
menu('beef','bagel','bordeaux')
menu(entree = 'beef', dessert = 'bagel', wine= 'bordeaux')
menu('frontenac', dessert = 'flan', entree= 'fish')

def menu_fixed(wine, entree, dessert = 'pudding'): #if you dont insert dessert, its ouput is pudding
    return{'wine': wine, 'entree' : entree, 'dessert': dessert}

menu_fixed('chardoney','chicken')
menu_fixed('dunkelfelder','duck','doughnut') # output has been changed as doughnut 

def buggy(arg, result = []):
    result.append(arg)
    print(result)
    
buggy('a')
buggy('b')

def nonbuggy(arg, result = None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
    
nonbuggy('a')
nonbuggy('b')
## 중요!!!

# * asterisk 가변 매개변수 처리, 튜플에 담음. 변수 담을 때 positional args 뒤에 작성할것.
def print_args(*args):
    print('Positional tuple', args)
    
print_args()
print_args(3,2,1,'wait!','uh...')

def print_more(required1, required2, *args):
    print('Need this one: ', required1)
    print('Need this one too: ', required2)
    print('Need these: ', args)
    
print_more('cap','gloves','glasses','muffler','shoes')

# * 는 tuple 반환 **는 dict 반환
def print_args(**args):
    print('Positional tuple', args)
    
print_args()
print_args(3,2,1,'wait!','uh...')

# 추가 질문 
# 오버로딩-객체지향 언어에서, 같은 함수이름을 가져도 변수 개수가 다르면 다르게 적용되는것/ 파이썬에서 적용 x
def a(n1,n2):
    print(n1,n2)
    
def a(n):
    print(n)
    
a(7)
a(7,11)

#  none 과 false 구분
def a(n):
    if n is None:
        print(f'{n} is None') #none
    elif n:
        print(f'{n} is True')#값 있음
    else:
        print(f'{n} is False')#비어있음
        
a(None)
a('')
a(-9)
a([])


# mutable, immutable
outside = ['one','fine','day']
def mangle(arg):
    arg[1] = 'terrible!'
    
mangle(outside)

print(isprime.__doc__) #double underscore __ : magic method

# function: everything is object -> func는 object로 다뤄짐

def squares(n):
    return n*n

def run_function(f, *number):
    return f(*number)

print(squares(7))
print(run_function(squares, number:9))

def squares(*n):
    """
    넘벼받은 수치 데이터들의 거듭제곱 값을 리ㅣ스트에 담아서 리턴 
    :param : tuple
    :
    """
    return [pow(i,2) for i in n]

print(run_function(squares(7,5,2)))
print(run_function(squares,9,10))

#closure
def out_func(nout):
    # new*
    def inner_func():
        return nout * nout
    reutrn inner_func()

x = out_func(9)
print(type(x))
print(x)
print(x())

# Inner function
def out_func(nout):
    new*
    def inner_func(nin):
        return nin *nin
    reutrn inner_func(nout)

print(out_func(5))

#lambda func
numbers = ["7","-11","3"]
print(sum(map(int,numbers)))
          
          
# numbers = ["7","-11","3"]
# hap = 0
# for number in numbers:
#     hap += int(number)
# print(hap)

# menu with func version2
def isprime(n) -> bool:
    """
    매개변수로 넘겨받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """
    if n < 2:
        return False
    else:
        i=2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1   
        return True      
    
while True:
    menu = input("1) fahrenheit -> celsius  2) Celsius -> fahrenheit  3) Prime number  4) Prime numbers(two input)  5) Quit Program : ")
    
    if menu  == '1':
        fahrenheit = float(input('Input fahrenheit: '))
        print(f'Fahrenheit: {fahrenheit}F, Celsius: {((fahrenheit-32.0)*5.0/9.0):.4f}C')
    
    elif menu == '2':
        celsius = float(input('Input Celcius: '))
        print(f'Celsius: {celsius}C, fahrenheit: {((celsius *9.0/5.0)+32.0):.4f}F')
    
    elif menu == '3':
        number = int(input("Input number: "))
        for i in range(2, number): 
            if isprime(number):
                print(f'{number} is prime number.')
            else: 
                print(f'{number} is NOT prime number')
        
    elif menu == '4':
        n1,n2 = map(int,input("first number Second number: ").split()) #map, int?에 함수의 이름을 넣음
        n1,n2 = min(n1,n2), max(n1,n2) #unpack
        # n1 = int(numbers[0])
        # n2 = int(numbers[1])

        if n1 > n2:
            n1,n2 = n2,n1
            
        for number in range(n1,n2+1,1):
            if isprime(number):
                print(number, end = ' ')
        print()
    
    elif menu == '5':
        print('Terminate Program.')
        break
    
    else: 
        print('Invaild Syntax!')
        