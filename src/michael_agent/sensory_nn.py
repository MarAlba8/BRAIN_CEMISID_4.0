from michael_agent.neurons import Neurons


class Sensory_NN():
    
    def __init__(self,sense="sight"):
        self.neurons = Neurons()
        self.id = sense

    def status(self):
        return self.neurons.get_neurons()

    def set_event_bce(self,event,bce):
        return self.neurons.set_event_bce(event,bce)+[self.id]

    def set_event(self,event):
        return self.neurons.set_event(event)+[self.id]

    def update_neuron(self, bce):
        return self.neurons.update_neuron_to_learn(bce)+[self.id]
    

    def init_event(self, arr_events):
        return self.neurons.init_event(arr_events)

    def init_patterns(self, arr_patterns_bce):
        result_list = [(pattern,bce) for pattern, bce in arr_patterns_bce]
        return self.neurons.init_patterns(result_list)
        
    def reset(self):
        self.neurons.reset()

    def to_memory(self):
        data=[]
        for key, value in self.status().items():
            data.append((key,self.id,value[0]))    
        return data
