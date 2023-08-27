from michael_agent.intelligent_agent import Intelligent_agent
from michael_agent.sensory_system import Sensory_system
from michael_agent.bce import BCE
class Agent_A():
    
    def __init__(self):
        self.ai_bce = Intelligent_agent()
        self.rn_senses = Sensory_system()
        

    def set_event(self,arr_event):
        return self.rn_senses.set_event(arr_event)

    #Entradas de modulo de maria     
    def update_neuron(self,arr_bce):
        return self.rn_senses.update_neuron(arr_bce)
    
    def status_rn(self):
        return self.rn_senses.status()
    
    def status_ai_bce(self):
        return  self.ai_bce.status()

    #La entrada es el evaluador general BCE de maria
    def add_bce(self,bce_in):
        return self.ai_bce.add_bce(bce_in)

    def init_patterns(self,arr_patternes):
        return self.rn_senses.init_patterns(arr_patternes)
 
    def to_memory(self):
        return self.rn_senses.to_memory()
    
    def get_bce_from_mind(self,bce:BCE):
        return self.rn_senses.get_bce_from_mind(bce)

    def reset(self):
        self.ai_bce.reset()
        self.rn_senses.reset()