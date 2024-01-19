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
    print(5/0)
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
    
except Exception as err:
    print(f'Error ocurs'{err})
    


