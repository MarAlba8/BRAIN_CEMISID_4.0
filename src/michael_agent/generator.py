import random

from michael_agent.bce import BCE
from michael_agent.need import Need

class Generator():

    def __init__(self):
        self.n_items = 15
        pattern_arr = ["pattern_{:03d}".format(i) for i in range(self.n_items)]
        self.generic_pattern_arr = [self.add_random_suffix(s) for s in pattern_arr]
        self.arr_senses = ["sight", "hearing", "smell", "taste", "touch", "body", "time"]
        self.generic_event_arr = ["event_{:03d}".format(i) for i in range(self.n_items)]
        self.arr_patternes_bce = []

    def add_random_suffix(self, input_string):
        suffixes = ["_b", "_c", "_e"]
        random_suffix = random.choice(suffixes)
        string_with_suffix = input_string + random_suffix
        return string_with_suffix

    def gen_patterns(self):
        arr_patternes_bce = []
        for sense in self.arr_senses:
            arr_senses = []
            for pattenr in self.generic_pattern_arr:
                if sense != "time":
                    arr_senses.append([f"{sense}_{pattenr}", BCE().sample()])
                else:
                    arr_senses.append([f"{sense}_{pattenr}", BCE().time_sample()])

                    
            arr_patternes_bce.append(arr_senses)
        self.arr_patternes_bce = arr_patternes_bce
        return self.arr_patternes_bce

    def gen_event(self):
        # self.gen_patterns()
        sensory_event = []
        for index, sense in enumerate(self.arr_senses):
            pattenr = random.choice(self.arr_patternes_bce[index])[0]
            event = random.choice(self.generic_event_arr)
            sensory_event.append(f"{pattenr}:{sense}_{event}")
        return sensory_event

    def gen_init_events(self):
        sensory_init_events = {}
        for sense_index, sense in enumerate(self.arr_senses):
            init_events = []
            for i in range(self.n_items):
                if i == 0:
                    pattern = random.choice(self.arr_patternes_bce[sense_index])[0]
                else:
                    prev_pattern = init_events[i - 1].split(':')[1].split('_')
                    pattern = '_'.join(prev_pattern)

                event = random.choice(self.generic_event_arr)
                while event == pattern:
                    event = random.choice(self.generic_event_arr)

                init_events.append(f"{pattern}:{sense}_{event}")
            sensory_init_events[sense] = init_events

        return sensory_init_events

    def manual_events(self):
        Events_BCE0 = [ "sight_educación_c:tesis",
                        "hearing_musica_e:canción_memorable",
                        "smell_cafe:olor_cafe",
                        "taste_dulce:sabor_dulce",
                        "touch_confortante:frio_confortante",
                        "body_saludable:saludable",
                        "time_neutro:tiempo_neutro"
                    ]
        Events_BCE1 = [ "sight_educación_c:tesis",
                        "hearing_musica_e:canción_memorable",
                        "smell_cafe:olor_cafe",
                        "taste_dulce:sabor_dulce",
                        "touch_confortante:frio_confortante",
                        "body_saludable:saludable",
                        "time_neutro:tiempo_neutro"
                    ]
        Events_BCE2 = [ "sight_educación_c:tesis",
                        "hearing_musica_e:canción_memorable",
                        "smell_cafe:olor_cafe",
                        "taste_dulce:sabor_dulce",
                        "touch_confortante:frio_confortante",
                        "body_saludable:saludable",
                        "time_neutro:tiempo_neutro"
                    ]
        


        return [Events_BCE0, Events_BCE1, Events_BCE2]

    def manual_patterns(self):
        patterns_BCE = [ [["sight_educación_c",BCE(Need(0,0),Need(0,2),Need(0,0))]],
                        [["hearing_musica_e",BCE(Need(0,0),Need(0,0),Need(1,2))]],
                        [["smell_cafe",BCE(Need(0,0),Need(0,0),Need(0,0))]],
                        [["taste_dulce",BCE(Need(0,0),Need(0,0),Need(0,0))]],
                        [["touch_confortante",BCE(Need(0,0),Need(0,0),Need(0,0))]],
                        [["body_saludable",BCE(Need(0,0),Need(0,0),Need(0,0))]],
                        [["time_neutro",BCE(Need(0,0),Need(0,0),Need(0,0))]]]
        return patterns_BCE
        

# patternes_init
