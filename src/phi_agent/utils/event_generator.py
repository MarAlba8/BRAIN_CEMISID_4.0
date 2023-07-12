import random

from michael_agent.bce import BCE


class Generator():

    def __init__(self):
        self.generic_pattern_arr=["pattern_zero","pattern_a","pattern_b","pattern_c","pattern_d","pattern_e","pattern_f","pattern_g","pattern_zero2"]
        self.arr_senses=["sight","hearing","smell","taste","touch","body","time"]
        self.generic_event_arr=["event_a","event_b","event_c","event_d","event_e","event_f","event_g","event_h","event_i"]
        self.arr_patternes_bce=[]

    def gen_patterns(self):
        arr_patternes_bce=[]
        for sense in self.arr_senses:
            arr_senses = []
            for pattenr in self.generic_pattern_arr:
                if pattenr == "pattern_zero" or pattenr == "pattern_zero2" and sense != "time":
                    arr_senses.append([f"{pattenr}_{sense}",BCE().zero()])
                elif sense == "time":
                    arr_senses.append([f"{pattenr}_{sense}",BCE().time_sample()])
                else:
                    arr_senses.append([f"{pattenr}_{sense}",BCE().sample()])
            arr_patternes_bce.append(arr_senses)
        self.arr_patternes_bce=arr_patternes_bce
        return self.arr_patternes_bce

    def gen_event(self):
        #self.gen_patterns()
        sensory_event=[]
        for index, sense in enumerate(self.arr_senses):
            pattenr = random.choice(self.arr_patternes_bce[index])[0]
            event = random.choice(self.generic_event_arr)
            sensory_event.append(f"{pattenr}:{event}")
        return sensory_event

    #gen_event(arr_senses,arr_events,patternes_init)


#patternes_init