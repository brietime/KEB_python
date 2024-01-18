# 9.1
def good():
    print(['Harry','Ron','Hermione'])

good()

# 9.2
def get_odds():
    odds_list = []
    for i in range(10):
        if i % 2 != 0:
            odds_list.append(i)
    print(odds_list[2])
    
get_odds()

# 9.3 
def test(func):
    def new_func(*args,**kwargs):     
        print('start')  
        result = func(*args,**kwargs)
        print('end')
    return new_func

@test
def get_odds():
    odds_list = []
    for i in range(10):
        if i % 2 != 0:
            odds_list.append(i)
    print(odds_list[2])
    
get_odds()
        
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
        except IndexError as err:
            print('Caught an Oops', menu) 
            
            
    
    
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
    


