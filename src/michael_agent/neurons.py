from michael_agent.bce import BCE

class Neurons():
    def __init__(self):
        self.learned_neurons = {}
        self.neuron_to_learn = {}

        self.tmp = None

    def set_event(self, string):
        pattern, event = string.split(":")
        if event not in self.learned_neurons:
            self.neuron_to_learn[event]=[len(self.learned_neurons),self.learned_neurons[pattern][1],pattern,event]
            return self.neuron_to_learn[event]
        else:
            self.tmp = self.learned_neurons[event]
            return self.learned_neurons[event]
        
    def set_event_bce(self, event, bce):
        if event not in self.learned_neurons:
            self.learned_neurons[event]=[len(self.learned_neurons),bce,"",event]
            #self.neuron_to_learn[event]=[len(self.learned_neurons),bce]
            #self.update_neuron_to_learn(bce)

        return self.learned_neurons[event]

    def init_event(self, arr_events):
        list_return = []
        for event in arr_events:
            self.set_event(event)
            data_return = self.update_neuron_to_learn( BCE().sample() )
            list_return.append(data_return)

        return data_return

    def update_neuron_to_learn(self, bce):
        if bool(self.neuron_to_learn):
            event, value = self.neuron_to_learn.popitem()
            id_neurona = len(self.learned_neurons)
            self.learned_neurons[event]=[id_neurona,(BCE.average(bce,value[1])),value[2],value[3]]
            return self.learned_neurons[event]
        else:
            return self.tmp 

    def init_patterns(self,arr_patterns_bce):
        #print(arr_patterns_bce)
        list_return = []
        for pattern_bce in arr_patterns_bce:
            data = self.set_event_bce(pattern_bce[0],pattern_bce[1])
            data_return = (data[0],pattern_bce[0],data[1])
            list_return.append(data_return)
            #list_id_neurons.append(id_neurons)
            #self.learned_neurons[pattern_bce[0]]=[id_neurons,pattern_bce[1]]
        return list_return
        

    def get_neurons(self):
        return self.learned_neurons

    def reset(self):
        self.learned_neurons = {}
        self.neuron_to_learn = {}
        