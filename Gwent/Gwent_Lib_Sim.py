'''
Created on May 14, 2021

@author: alienware
'''
import matplotlib.pyplot as plt
import random 

class Card:
    def __init__(self,Rarity,ID):
        self.ID = ID
        self.Rarity = Rarity
        
    def __repr__(self):
        return f"<{self.Rarity}>|{self.ID}"
    
    def __eq__(self,right):
        assert isinstance(right, Card)
        return self.ID == right.ID and self.Rarity == right.Rarity

class Gwent_Cards:
    def __init__(self,rarity = {'C':0.72,'R':0.224,'E':0.0448,'L':0.0112},
                 Pool_info = {'C': 66,'R':67,'E':103,'L':66} ):
        self.rarity = rarity 
        self.Pool_info = Pool_info
        self.Pool = self.Fill_Pool()
        self.Library = {'C':[],'R':[],'E':[],'L':[]}
        self.Value_Cost = {'C': 30,'R':80,'E':200,'L':800}
        self.millRate = {'C': 1/6,'R':1/8,'E':1/4,'L':1/4}
        
    @staticmethod
    def SET(List_of_Cards):
        OUT = []
        for card in List_of_Cards:
            add_it = True
            if len(OUT) == 0:
                OUT.append(card)
            else:
                for card_ex in OUT:
                    if card_ex == card:
                        add_it = False
                if add_it:
                    OUT.append(card)
        return OUT
    
                
    def SET_lib(self):
        OUT =  {'C':[],'R':[],'E':[],'L':[]}
        for rarity in self.Library:
            OUT[rarity] = self.SET(self.Library[rarity])
        return OUT
        
    def Fill_Pool(self):
        Pool = {'C':[],'R':[],'E':[],'L':[]}
        for Rarity in self.Pool_info:
            N_cards = self.Pool_info[Rarity]
            for repeat in range(N_cards):
                Pool[Rarity].append(Card(Rarity,f'CardID_{len(Pool[Rarity])}'))
        return Pool
        
    def Draw(self,k=1):
        OUT = []
        for i in range(k):
            Rarity =  random.choices(population = list(self.rarity.keys()), weights = list(self.rarity.values()))
            OUT.append( random.choices(self.Pool[Rarity[0]]) [0])
        return OUT
    
    def EPK(self):
        OUT = 0
        LIB = self.SET_lib()
        def P_own(rarity,Libary):
            return len(Libary[rarity])/len(self.Pool[rarity])
        
        for rarity in self.rarity:
            pr_own = P_own(rarity,LIB)
            OUT += pr_own*self.rarity[rarity]*self.Value_Cost[rarity]*self.millRate[rarity] + (1-pr_own)*self.rarity[rarity]*self.Value_Cost[rarity]
        return OUT
       
    def _add_toLib(self,n):
        def add(card):
            assert isinstance(card, Card)
            self.Library[card.Rarity].append(card)
            
        for i in range(int(5*n)):
            add(self.Draw()[0])
             
if __name__ == '__main__':
    T = Gwent_Cards()
    EPKs = []
    n = 200
    for i in range(n):
        T._add_toLib(1)
        EPKs.append(T.EPK())
    plt.plot(range(n),EPKs)
    plt.show()