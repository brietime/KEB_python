# 9.1
def good():
    '''
    chapter 9.01 
    return: list
    '''
    name = input('Type your name: ').split()
    return name

print(good())

# 9.2
def get_odds(n) -> int:
    """
    1부터 n까지의 홀수를 발생시키는 제네레이터
    :param n: int
    :return: int
    """
    for i in range(1, n+1, 2):
        yield i

cnt = 0
odds = get_odds(9)
for odd in odds:
    cnt = cnt + 1
    if cnt == 3:
        print(f'Third number is {odd}')
        break   

# 9.3 
# def test(func):
#     '''
#     데코레이터 함수, 함수 시작하면 start 출력, 함수 끝나면 end 출력
#     :param f: function
#     :return: closure function
#     '''
#     def new_func(*args,**kwargs):     
#         print('start')  
#         result = func(*args,**kwargs)
#         print('end')
#         return result
#     return new_func

def test(f):
    '''
    데코레이터 함수, 함수 시작하면 start 출력, 함수 끝나면 end 출력
    :param f: function
    :return: closure function
    '''
    def test_in(*args,**kwargs):     
        print('start')  
        # result = func(*args,**kwargs)
        f()
        print('end')
        # return result
    return test_in

@test
def greeting():
    print('안녕하세요~')
    
greeting()
        
# 9.4
import random

class OopsException(Exception):
    drinks_foods= {'고량주':'양꼬치','위스키':'초콜릿','와인':'치즈','소주':'삼겹살'}
    japan_drinks_foods = {'사케':'광어회','위스키':'낙곱새'}
    drinks_foods.update(japan_drinks_foods)

    drinks_foods_keys = list(drinks_foods)

    while True:
        menu = input(f'다음 술 중에 고르세요.\n1){drinks_foods_keys[0]}, 2){drinks_foods_keys[1]}, 3){drinks_foods_keys[2]}, 4){drinks_foods_keys[3]}, 5){drinks_foods_keys[4]}, 6)오늘의 추천 7)종료 : ')

        if menu == '1':
            print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]}입니다.')
        elif menu == '2':
            print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]}입니다.')
        elif menu == '3':
            print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]}입니다.')
        elif menu == '4':
            print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]}입니다.')
        elif menu == '5':
            print(f'{drinks_foods_keys[4]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[4]]}입니다.')
        elif menu == '6':
            random_drink = random.choice(drinks_foods_keys)
            print(f'오늘의 추천 메뉴는 {random_drink}와 {drinks_foods[random_drink]}입니다.')
        elif menu == '7':
            print('다음에 또 오세요')
            break
        
        try: 
            menu != int(1,2,3,4,5,6,7)
            print('다음에 또 오세요')
        # except IndexError:
        #     print('Caught an Oops- index error index', menu) 
        # except ValueError:
        #     print('Caught an Oops-value error index', menu) 
        # except Exception: 
        #     print('Caught an oops')
        except IndexError as err:
            print('Caught an Oops\n{err}') 
        except ValueError as err:
            print('Caught an Oops\n{err}') 
        except Exception as err: 
            print('Caught an oops\n{err}')
            
            
            
    
    
# 피보나치 수열에서 소수인 수 출력
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fib_list = []
for i in range(10):
    fib_list.append(fib(i))
    


