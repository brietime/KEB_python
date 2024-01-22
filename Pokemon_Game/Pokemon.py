from Field_Setting import *

class Pokemon:
    def __init__(self, name, type, life):
        self.__name = name
        self.type = type
        self.life = life
        
    def attack(self):
        return life -3
    
    def HP(name, combat_field, type):
        life = 10
        if combat_field(stage) == given_field(type):
            life += 2



class Pikachu(Pokemon):
    pass

class Pengdori(Pokemon):
    pass

class Paiery(Pokemon):
    pass

class Charizard(Pokemon): # 다중 상속중
    pass

p1 = Pikachu("피카츄", "electric")
p2 = Pengdori("펭도리", "water")
p3 = Paiery("파이리", "fire")# LSP


c1 = Charizard("리자몽", "fire") # LSP



# assosiation: aggergation(부품 분리 가능) & composition(부품 분리 불가)
class FlyingMixin, class SwimmingMixin

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
