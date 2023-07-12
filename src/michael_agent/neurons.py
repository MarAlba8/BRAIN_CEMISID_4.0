from michael_agent.bce import BCE

class Neurons():
    def __init__(self):
        self.learned_neurons = {}
        self.neuron_to_learn = {}

        self.tmp = None

    def set_event(self, string):
        pattenr, event = string.split(":")
        
        if event not in self.learned_neurons:
            self.neuron_to_learn[event]=[len(self.learned_neurons),self.learned_neurons[pattenr][1]]
            return self.neuron_to_learn[event]
        else:
            self.tmp = self.learned_neurons[event]
            return self.learned_neurons[event]
        
    def set_event_bce(self, event, bce):
        if event not in self.learned_neurons:
            self.neuron_to_learn[event]=[len(self.learned_neurons),BCE().none()]
            self.update_neuron_to_learn(bce)

        return self.learned_neurons[event]

    def update_neuron_to_learn(self, bce):
        if bool(self.neuron_to_learn):
            event, value = self.neuron_to_learn.popitem()
            id_neurona = len(self.learned_neurons)
            self.learned_neurons[event]=[id_neurona,(bce+value[1])//2]
            return self.learned_neurons[event]
        else:
            return self.tmp 

    def init_patterns(self,arr_patternes_bce):
        for pattern_bce in arr_patternes_bce:
            self.learned_neurons[pattern_bce[0]]=[len(self.learned_neurons),pattern_bce[1]]

    def get_neurons(self):
        return self.learned_neurons

