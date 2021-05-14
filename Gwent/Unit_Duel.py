'''
Created on May 9, 2021

@author: alienware
'''
from copy import copy
class Units():
    def __init__(self,Name,Hp,Armor,Shield = False):
        self.Name = Name
        self.Hp = Hp
        self.Armor = Armor
        self.Shielded = Shield
        
    def __repr__(self):
        if self.Shielded:
            return f"({self.Name}<Hp:{self.Hp},{self.Armor}>)"
        else:
            return f"{self.Name}<Hp:{self.Hp},{self.Armor}>"
        
    def duel(self,target):
        def attack(hp,armor,dmg):
            armor_left = armor - dmg
            hp_left = hp + min(0,armor_left)
            return max(hp_left,0), max(0,armor_left)
            
        print(f"**{self} __V.S__  {target}**")
        while True:
            #Self_Attack Target
            target_temp = copy(target)
            if target.Shielded:
                target.Shielded = False
            else:
                target.Hp,target.Armor = attack(target.Hp, target.Armor, self.Hp) 
            print(f"{self} ATTACK {target.Name}:{target_temp.__repr__()}--->{target.__repr__()}")
            if target.Hp <= 0 :
                break
            #Target Attack Back:
            self_temp = copy(self)
            if self.Shielded:
                self.Shielded = False
            else:
                self.Hp,self.Armor = attack(self.Hp, self.Armor, target.Hp) 
            print(f"{target} ATTACK {self.Name}:{self_temp.__repr__()}--->{self.__repr__()}")
            if self.Hp <= 0:
                break
        print(f"**RESULT:{self.__repr__()}{target.__repr__()}**\n")
            
        
    def Sim_Duel(self,target):
        SELF1 = copy(self)
        SELF2 = copy(self)
        TARGET1 = copy(target)
        TARGET2 = copy(target)
        SELF1.duel(TARGET1)
        TARGET2.duel(SELF2)

        
if __name__ == '__main__':
    A = Units('a',10,4,1)
    B = Units('b',15,0,0)
    A.Sim_Duel(B)