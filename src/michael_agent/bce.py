from michael_agent.need import Need
import numpy as np

class BCE():
    
    def __init__(self,need_bio=Need().sample(),need_cul=Need().sample(),need_emo=Need().sample()):
        #action  6*3+1 =>19
        
        self.biological = need_bio
        self.culture = need_cul
        self.emotional = need_emo

    def set(self, need_bio, need_cul, need_emo):

        self.need_bio = Need.set(need_bio)
        self.need_cul = Need.set(need_cul)
        self.need_emo = Need.set(need_emo)
        return self
    
    def state(self):
        return np.array([ self.biological.state, self.culture.state, self.emotional.state ], dtype=np.int_)  
        
        #self.sign_str={0:"+",1:"-"}
    def __str__(self):
        return f"Bio:{str(self.biological)} Cul:{str(self.culture)} Emo:{str(self.emotional)}"

    def __repr__(self):
        return f"Bio:{str(self.biological)} Cul:{str(self.culture)} Emo:{str(self.emotional)}"
    
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


    def __lt__(self, other):    #To get called on comparison using < operator.
        if self.biological < other.biological and self.culture < other.culture and self.emotional < other.emotional:
            return True
        else:
            return False
        
    def __eq__(self, other):    #To get called on comparison using == operator.
        if self.biological == other.biological and self.culture == other.culture and self.emotional == other.emotional:
            return True
        else:
            return False

    def __ne__(self, other):    #To get called on comparison using != operator.
        if self.biological != other.biological and self.culture != other.culture and self.emotional != other.emotional:
            return True
        else:
            return False

    def __le__(self, other):    #To get called on comparison using <= operator.
        if self.biological <= other.biological and self.culture <= other.culture and self.emotional <= other.emotional:
            return True
        else:
            return False

    def __gt__(self, other):    #To get called on comparison using > operator.
        if self.biological > other.biological and self.culture > other.culture and self.emotional > other.emotional:
            return True
        else:
            return False

    def __ge__(self, other):    #To get called on comparison using >= operator.
        if self.biological >= other.biological and self.culture >= other.culture and self.emotional >= other.emotional:
            return True
        else:
            return False


    def reset(self):
        
        self.biological.reset()
        self.culture.reset()
        self.emotional.reset()
        return self
    
    @staticmethod
    def average(*args):
        if len(args)==0:
            return None

        bio=[]
        cul=[]
        emo=[]

        for item in args:
            bio.append(item.biological)
            cul.append(item.culture)
            emo.append(item.emotional)
        
        return BCE(Need.average(*bio),Need.average(*cul),Need.average(*emo))


    def sample(self):
        return BCE(self.biological.sample(),self.culture.sample(),self.emotional.sample())
    
    def time_sample(self):
        return BCE(self.biological.time_sample(),self.culture.time_sample(),self.emotional.time_sample())
    
    def zero(self):
        self.biological.zero()
        self.culture.zero()
        self.emotional.zero()
        return self
 
    def none(self):
        self.biological.none()
        self.culture.none()
        self.emotional.none()
        return self

