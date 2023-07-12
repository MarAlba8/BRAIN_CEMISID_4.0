from michael_agent.need import Need
import numpy as np

class BCE():
    
    def __init__(self,need_bio=Need().sample(),need_cul=Need().sample(),need_emo=Need().sample()):
        #action  6*3+1 =>19
        
        self.biological = need_bio
        self.culture = need_cul
        self.emotional = need_emo

    def state(self):
        return np.array([ self.biological.state, self.culture.state, self.emotional.state ], dtype=np.int_)  
        
        #self.sign_str={0:"+",1:"-"}
    def __str__(self):
        return f"Biological:{str(self.biological)} Culture:{str(self.culture)} Emotional:{str(self.emotional)}"

    def __repr__(self):
        return f"Biological:{str(self.biological)} Culture:{str(self.culture)} Emotional:{str(self.emotional)}"
    
    def __add__(self, other):
        return BCE(self.biological+other.biological,self.culture+other.culture,self.emotional+other.emotional)
    
    def __sub__(self, other):
        return BCE(self.biological-other.biological,self.culture-other.culture,self.emotional-other.emotional)
    
    def __mul__(self, escalar):
        return BCE(self.biological*escalar,self.culture*escalar,self.emotional*escalar)
    
    def __floordiv__(self, escalar):
        return BCE(self.biological//escalar,self.culture//escalar,self.emotional//escalar)
    
    def __truediv__(self, escalar):
        return BCE(self.biological/escalar,self.culture/escalar,self.emotional/escalar)
    
    def reset(self):
        self.biological.reset()
        self.culture.reset()
        self.emotional.reset()

    def sample(self):
        return BCE(self.biological.sample(),self.culture.sample(),self.emotional.sample())
    
    def time_sample(self):
        return BCE(self.biological.time_sample(),self.culture.time_sample(),self.emotional.time_sample())
    
    def zero(self):
        return BCE(Need().zero(), Need().zero(), Need().zero())
    
    def none(self):
        return BCE(Need().none(), Need().none(), Need().none())

