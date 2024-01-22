# class mothid 는 공유
# self 로 생성된 객체 인스턴스 
# 덕 타이핑 - 꼭 상속 관계에 있는 클래스의 함수만 이용할 수 있는 것은 아님. 10.7 확인
# 덕타이핑을 하기 위해 객체가 갗춰야 할 것은?

# class FlyingBehavior:
#     def fly(self):
#         return f"하늘을 훨훨 날아갑니다~"

# class NoFly(FlyingBehavior):
#     def fly(self):
#         return f"하늘을 날 수 없습니다."

# class FlyWithiWings(FlyingBehavior):
#     def fly(self):
#         return f"하늘을 훨훨 날아갑니다~"

# class JetPack(FlyingBehavior):
#     def fly(self):
#         return f"로켓추진기로 하늘을 날아갑니다!"

# class Pokemon:
#     def __init__(self, name, hp, fly):
#         self.__name = name
#         self.hp = hp
#         self.FlyingBehavior = fly

#     def set_fly_behavior(self,fly):
#         self.FlyingBehavior = fly
        
#     def attack(self):
#         print("공격~")

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name

#     # magic method
#     def __str__(self):
#         return self.__name + " 입니다"

#     def __add__(self, target):
#         #return self.__name + " + " + target.__name
#         return f"두 포켓몬스터 체력의 합은 {self.hp + target.hp}입니다."


# class Charizard(Pokemon): # 다중 상속중
#     pass

# class Pikachu(Pokemon):
#     pass

# nofly = NoFly()
# p1 = Pikachu("피카츄", 100, nofly) # LSP
# wings = FlyWithiWings()
# c1 = Charizard("리자몽", 120, wings) # LSP

# print(c1.FlyingBehavior.fly())
# print(p1.FlyingBehavior.fly())
# print(p1)
# print(c1)
# print(p1+c1)
# #print(p1+200)
# p1.set_fly_behavior(JetPack())
# print(p1.FlyingBehavior.fly())

# assosiation: aggergation(부품 분리 가능) & composition(부품 분리 불가)
# class FlyingMixin, class SwimmingMixin

# 해당 부분을 상속에서 연관관계로 변경하고자 함


class FlyingBehavior:
    def fly(self):
        return f"하늘을 훨훨 날아갑니다~"

class NoFly(FlyingBehavior):
    def fly(self):
        return f"하늘을 날 수 없습니다."
    
class JetPack(FlyingBehavior):
    def fly(self):
        return f"로켓추진기로 하늘을 날아갑니다!"
    
    
# class Pikachu:
#     def __init__(self, name, hp, fly):
#         self. name = name
#         self.hp = hp
#         self.FlyingBehavior = fly # aggregation 
# nofly = NoFly() # 객체가 밖에서 생성
class Pikachu:
    def __init__(self, name, hp):
        self. name = name
        self.hp = hp
        self.FlyingBehavior = NoFly() # composition, Nofly 객체가 안에서 생성
# 피카츄 객체가 Nofly를 가지고 있음

p1 = Pikachu("피카츄", 100) # LSP
print(p1.FlyingBehavior.fly())
print(p1)

# has-a : self.~ 가지고 있음
# use-a: 셀프 없음


import mymath

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
            if mymath.isprime(number):
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
            if mymath.isprime(number):
                print(number, end = ' ')
        print()
    
    elif menu == '5':
        print('Terminate Program.')
        break
    
    else: 
        print('Invaild Syntax!')
        