import random

from michael_agent.bce import BCE


class Generator():

    def __init__(self):
        n_items=10
        self.generic_pattern_arr=["pattern_zero","pattern_zero2"]+["pattern_{:03d}".format(i) for i in range(n_items)]
        self.arr_senses=["sight","hearing","smell","taste","touch","body","time"]
        self.generic_event_arr=["event_{:03d}".format(i) for i in range(n_items)]
        self.arr_patternes_bce=[]

    def gen_patterns(self):
        arr_patternes_bce=[]
        for sense in self.arr_senses:
            arr_senses = []
            for pattenr in self.generic_pattern_arr:
                if pattenr == "pattern_zero" or pattenr == "pattern_zero2" and sense != "time":
                    arr_senses.append([f"{pattenr}",BCE().zero()])
                elif sense == "time":
                    arr_senses.append([f"{pattenr}",BCE().time_sample()])
                else:
                    arr_senses.append([f"{pattenr}",BCE().sample()])
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
