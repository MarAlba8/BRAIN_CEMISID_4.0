from michael_agent.neurons import Neurons


class Sensory_NN():
    
    def __init__(self,sense="sight"):
        self.neurons = Neurons()
        self.id = sense

    def status(self):
        return self.neurons.get_neurons()

    def set_event_bce(self,event,bce):
        #if not event.endswith("_"+self.id):
        #    event += "_"+self.id

        return self.neurons.set_event_bce(event,bce)+[self.id]

    def set_event(self,event):
        pattern = event.split(':')[0]
        #if not pattern.endswith("_"+self.id):
        #    pattern += "_"+self.id
        
        event_split = event.split(':')[1]
        #if not event_split.endswith("_"+self.id):
        #    event_split += "_"+self.id      
        
        pattern_event = pattern + ":" + event_split
        return self.neurons.set_event(pattern_event)+[self.id]

    def update_neuron(self, bce):
        return self.neurons.update_neuron_to_learn(bce)+[self.id]
    
    def init_patterns(self, arr_patterns_bce):
        #result_list=[]
        #result_list = [(pattern,bce) if pattern.endswith("_"+self.id) else (pattern+ "_"+self.id, bce) for pattern, bce in arr_patterns_bce]
        result_list = [(pattern,bce) for pattern, bce in arr_patterns_bce]
        #result_list = []
        #for pattern, bce in arr_patterns_bce:
        #    if pattern.endswith("_" + self.id):
        #        result_list.append((pattern, bce))
        #    else:
        #        result_list.append((pattern + "_" + self.id, bce))
        
        return self.neurons.init_patterns(result_list)
        
    def reset(self):
        self.neurons.reset()

    def to_memory(self):
        data=[]
        for key, value in self.status().items():
            data.append((key,self.id,value[0]))    
        return data
