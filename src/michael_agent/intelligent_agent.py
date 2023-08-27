from michael_agent.bce import BCE
from michael_agent.need import Need

class Intelligent_agent():
    
    def __init__(self):
        self.status_bce = BCE().zero()
        self.length = Need().len_degree

    def status(self):
        return self.status_bce

    def add_bce(self,bce):
        self.status_bce += bce
        return self.status_bce
    
    def __str__(self) -> str:
        return str(self.status_bce)
    
    def __repr__(self) -> str:
        return str(self.status_bce)
    
    def reset(self):
        self.status_bce = BCE().zero()
        return self.status