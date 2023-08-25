import random
import numpy as np

LEN_DEGREE=4

class Need():

    sign_str={0:"+",1:"-"}

    def __init__(self, sign=0, degree=0, len_degree=LEN_DEGREE):

        self.len_sign=2
        self.len_degree=len_degree
        
        if sign==None and degree==None:
            self.state = np.array([sign,degree]) 
        else:
            self.state = np.array([sign,degree], dtype=np.int_) 
        
         

    def set(self, num:int, len_degree=LEN_DEGREE):

        self.len_sign=2
        self.len_degree=len_degree
        sign= 0 if num >=0 else 1
        degree=abs(num) if abs(num)<=self.len_degree else self.len_degree

        self.state = np.array([sign,degree], dtype=np.int_) 
        return self

    def __str__(self):
        if self.state[0]!=None and self.state[1]!=None:
            return f"{self.sign_str[self.state[0]]}{self.state[1]/self.len_degree}"
        else:
            return "None"
    
    def __repr__(self):
        if self.state[0]!=None and self.state[1]!=None:
            return f"{self.sign_str[self.state[0]]}{self.state[1]/self.len_degree}"
        else:
            return "None"
        
    def __add__(self, other):
        if other.state[0]==None or other.state[1]==None:
            return Need(self.state[0],self.state[1])
        elif self.state[0]==None or self.state[1]==None:
            return Need(other.state[0],other.state[1])

        if self.state[1] == 0 and other.state[1] == 0:
            return Need(self.state[0],self.state[1])
        
        # sign1= [1,-1]
        # degree1= self.state[1]*sign1[self.state[0]]
        # degree2= other.state[1]*sign1[other.state[0]]

        # ret_val=degree1+degree2
        # if ret_val ==0:
        #     ret_sign=self.state[0]
        # elif ret_val >0:
        #     ret_sign=0
        #     ret_val=min(ret_val,self.len_degree)
        # else:
        #     ret_sign=1
        #     ret_val=min(abs(ret_val),self.len_degree)
        # return Need(ret_sign,ret_val)

        #self.state[1]+other.state[1]
        elif self.state[0]==0:
           if other.state[0] == 0:
               sign = 0
               degree = self.state[1]+other.state[1]
           else:
               if self.state[1] >= other.state[1]:
                   sign = 0
                   degree = self.state[1]-other.state[1]
               else:
                   sign = 1
                   degree = abs(self.state[1]-other.state[1])
        else:
           if other.state[0] == 1:
               sign = 1
               degree = self.state[1]+other.state[1]
           else:
               if self.state[1] >= other.state[1]:
                   sign = 1
                   degree = self.state[1]-other.state[1]
               else:
                   sign = 0
                   degree = abs(self.state[1]-other.state[1])
                    
        return Need(sign,min(degree,self.len_degree))
    
    def __sub__(self, other):	#To get called on subtraction operation using - operator.  
        if other.state[0] == None and other.state[1] == None:
            return self
        elif other.state[0] == 0:
            sign=1
        elif other.state[0] == 1:
            sign=0
        return self+Need(sign,other.state[1])

    def __mul__(self, escalar):	#To get called on multiplication operation using * operator.
        if self.state[1]==0 or escalar ==0:
            sign=self.state[0]
        elif self.state[0] == 0 and escalar > 0:
            sign=0
        elif self.state[0] == 1 and escalar < 0:
            sign=0
        else:
            sign=1
        return Need(sign,self.state[1]*abs(escalar))+Need(0,0)

    def __truediv__(self, escalar):	#To get called on division operation using / operator.
        if self.state[1]==0:
            sign=self.state[0]
        elif self.state[0] == 0 and escalar > 0:
            sign=0
        elif self.state[0] == 1 and escalar < 0:
            sign=0
        else:
            sign=1
        return Need(sign,self.state[1]/abs(escalar))+Need(0,0)

    def __floordiv__(self, escalar):	#To get called on division operation using // operator.
        if self.state[1]==0:
            sign=self.state[0]
        elif self.state[0] == 0 and escalar > 0:
            sign=0
        elif self.state[0] == 1 and escalar < 0:
            sign=0
        else:
            sign=1
        return Need(sign,self.state[1]//abs(escalar))+Need(0,0)

    def __lt__(self, other):    #To get called on comparison using < operator.
        if (self.state[0]==None and self.state[1]==None) and (other.state[0]!=None and other.state[1]!=None):
            return True
        elif (other.state[0]==None and other.state[1]==None) and (self.state[0]!=None and self.state[1]!=None):
            return False
        elif self.state[0]==0 and other.state[0]==0:
            return self.state[1] < other.state[1]
        elif self.state[0]==1 and other.state[0]==1:
            return self.state[1] > other.state[1]
        elif self.state[0]==0 and other.state[0]==1:
            return False
        elif self.state[0]==1 and other.state[0]==0:
            return True
        
    def __eq__(self, other):    #To get called on comparison using == operator.
        if self.state[0]==other.state[0] and self.state[1]==other.state[1]:
            return True
        else:
            return False

    def __ne__(self, other):    #To get called on comparison using != operator.
        if self == other:
            return False
        else:
            return True

    def __le__(self, other):    #To get called on comparison using <= operator.
        if self == other:
            return True
        elif self < other:
            return True
        else:
            return False

    def __gt__(self, other):    #To get called on comparison using > operator.
        if self == other:
            return False
        elif self < other:
            return False
        else:
            return True

    def __ge__(self, other):    #To get called on comparison using >= operator.
        if self == other:
            return True
        elif self > other:
            return True
        else:
            return False

    def reset(self):
        sign=random.randint(0,self.len_sign-1)
        degree=random.randint(0,self.len_degree-1)
        self.state=np.array([sign,degree], dtype=np.int_)
        return self

    def sample(self):
        sign=random.randint(0,self.len_sign-1)
        degree=random.randint(0,self.len_degree-1)
        return Need(sign,degree)

    def time_sample(self):
        sign=1
        degree=random.randint(0,self.len_degree-1)
        return Need(sign,degree)

    def zero(self):
        sign=0
        degree=0
        self.state=np.array([sign,degree], dtype=np.int_)
        return self

    def none(self):
        sign=None
        degree=None
        self.state=[sign,degree]
        return self

    @staticmethod
    def average(*args):
        if not args:
            return None  # Si no se proporcionan valores, retorna None o algún otro valor apropiado

        items=[]
        for item in args :
            if item.state[0]==0:
                items.append(item.state[1])
            else:
                items.append(item.state[1]*(-1))

        total = sum(items)
        avg = total // len(args)

        if avg==0:
            return Need(args[0].state[0],avg)
        elif avg<0:
            return Need(1,abs(avg))+Need(0,0)
        else:
            return Need(0,abs(avg))+Need(1,0)


        
