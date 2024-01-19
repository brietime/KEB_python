# 9.10 namespace와 name scope
# 전역변수는 프로그램 종료시까지 메모리를 소모
animal = 'fruitbat'
def print_global():
    print('inside print_global: ', animal)
    '''
    global 안쓰면 local처리 되어서 함수 나오면 wombat 찍힘
    '''
print('at the top level: ', animal)
print_global()

# def change_and_print_global():
#     print('inside change_and_print_global: ', animal)
#     animal = 'wombat'
#     print('after change: ' , animal)
    
# change_and_print_global()

def change_local():
    animal = 'wombat'
    print('inside change_local: ' , animal)

# 9.11 _, __    
    
# 9.12 재귀
def factorial_repretition(n) -> int:
    '''
    반복문을 이용한 팩토리얼 함수
    :param n: 정수, int
    :return: 팩토리얼 값 
    '''
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

def factorial_recursion(n):
    '''
    재귀함수를 사용한 팩토리얼 함수
    :param n: 정수, int
    :return: function, int
    '''
    if n == 1:
        return n 
    else: 
        return n * factorial_recursion(n-1)
 
number = int(input("number: "))  

print(factorial_repretition(number))
print(factorial_recursion(number))

# 9.13 Async(비동기) Func
# 동기화 하면 시간이 오래걸려용용

# 9.14 예외처리
import random 
# numbers = list()
# for i in range(10):
#     numbers.append(random.randint(1, 100))
    
numbers = [random.randint(1,100) for i in range(5)]
print(numbers)

try:
    pick = int(input(f"Input index (0 ~ {len(numbers)-1}): ")) 
    print(numbers(pick))
    print(5/2)
    raise OopsException("Oops~") # exception!
# except IndexError:
#     print(f'Out of range: shold got index number 0 ~ {len(numbers)-1} but got {pick}!')
except IndexError as err:
    print(f'shold got index number \n{err}')
    
# except ValueError:
#     print(f'Input Only NUMBER: shold got index number 0 ~ {len(numbers)-1} but got {pick}!')
except ValueError:
    print(f'Input Only NUMBER \n{err}')
        
except ZeroDivisionError as err:
    print(f'Denominator cannot be 0.\n{err}')
except OopsException as  err:
    print(f"Oops Oops {err}")
except Exception as err:
    print(f'Error ocurr {err}')
else:
    print(f"Program terminate")
    
# def desc():
#     def wrapper():
#         print('w')
#     print('a')
#     return wrapper 

# def something():
#     print("do something")
# desc() #'a' not 'w' if 'w', its becuz of return wrapper
    
 # 개방폐쇄 good
def desc(f):
    def wrapper():
        print("study")
        f()
    return wrapper 


def something():
    print("do something")

s = desc(something) 
s()

# something()


# 10 object and classes
# 10.1 
class Pokemon:
    def __init__(self,name):
        self.name = name
        print(f"{name} 포켓몬스터 생성")
    def attack(self, target):
        print(f'{self.name}이(가) {target.name}을(를) 공격!')
        
    
charizard = Pokemon("리자몽")   
pikachu = Pokemon('피카츄') # self 피카츄
sqrirtle = Pokemon("꼬부기") # self 꼬부기
charizard.attack(sqrirtle)
# print(pikachu.name)
# print(sqrirtle.name)

# pikachu = Pokemon()
# squirtle = Pokemon()
# pikachu.name = "피카츄"
# pikachu.nemesis = squirtle
# print(pikachu.name)
# # print(pikachu.nemesis.name)
# pikachu.nemesis.name = "꼬부기" #squirtle.name = "꼬부기"
# print(pikachu.nemesis.name)
# print(squirtle.nemesis.name)

# print(pikachu)
# print(squirtle)

# 10.03 METHOD

# 10.04 Initialization
# __init__ 초기화 해주는 특수함수
# self는 예약어 x, 다른 단어 사용 가능하지만 관용적으로 사용.
# 실행시점의 객체의 정보를 담고 있음(피카츄 만들때는 피카츄, 꼬부기 만들고 나면 꼬부기)
# 

#  calss 간의 관계 -상속

# 부모클래스의 객체가 들어갈 수 있는 자리에 자식 클래스 호환 가능(lstm)
# 