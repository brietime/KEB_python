# class mothid 는 공유
# self 로 생성된 객체 인스턴스 
# 덕 타이핑 - 꼭 상속 관계에 있는 클래스의 함수만 이용할 수 있는 것은 아님. 10.7 확인
# 덕타이핑을 하기 위해 객체가 갗춰야 할 것은?


class FlyingMixin:
    def fly(self):
        return f"{self.__name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name, hp):
        self.__name = name
        self.hp = hp

    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    # magic method
    def __str__(self):
        return self.__name + " 입니다"

    def __add__(self, target):
        #return self.__name + " + " + target.__name
        return f"두 포켓몬스터 체력의 합은 {self.hp + target.hp}입니다."


class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스", 100)
c1 = Charizard("리자몽", 120)
print(g1)
print(c1)
print(g1+c1)
#print(g1+200)