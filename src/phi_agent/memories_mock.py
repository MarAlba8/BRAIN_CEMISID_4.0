import random

from phi_agent.settings import SENSES
from phi_agent.settings import STATES

MEMORIES = {
    "Movie": {
        'hearing': {
            'biological': f"childhood_movie::song",
            'cultural': f"childhood_movie:song",
            'emotional': f"childhood_movie:song"
        },
        'touch': {
            'biological': "childhood_movie:sense_chair",
            'cultural': "childhood_movie:sense_chair",
            'emotional': "childhood_movie:sense_chair"
        },
        'sight': {
            'biological': f"childhood_movie:images",
            'cultural': f"childhood_movie:images",
            'emotional': f"childhood_movie:images"
        },
        'smell': {
            'biological': f"childhood_movie:pop_corns_smell",
            'cultural': f"childhood_movie:pop_corns_smell",
            'emotional': f"childhood_movie:pop_corns_smell"
        },
        'taste': {
            'biological': f"childhood_movie:pop_corn_taste",
            'cultural': f"childhood_movie:pop_corn_taste",
            'emotional': f"childhood_movie:pop_corn_taste"
        },
        'body': {
            'biological': f"childhood_movie:sense_mouth_location",
            'cultural': f"childhood_movie:sense_mouth_location",
            'emotional': f"bchildhood_movie:sense_mouth_location"
        },
        'time': {
            'biological': "childhood_movie:time_slow",
            'cultural': "childhood_movie:time_slow",
            'emotional': "childhood_movie:time_slow"
        }
    },
    "Song": {
        'hearing': {
            'biological': f"childhood_song:agua fria",
            'cultural': f"childhood_song:tesis",
            'emotional': f"childhood_song:nostalgia"
        },
        'touch': {
            'biological': "childhood_song",
            'cultural': "childhood_song",
            'emotional': "childhood_song"
        },
        'sight': {
            'biological': f"childhood_song:tesis",
            'cultural': f"childhood_song:tesis",
            'emotional': f"childhood_song:good"
        },
        'smell': {
            'biological': f"childhood_song",
            'cultural': f"childhood_song",
            'emotional': f"childhood_song"
        },
        'taste': {
            'biological': f"childhood_song",
            'cultural': f"childhood_song",
            'emotional': f"childhood_song"
        },
        'body': {
            'biological': f"childhood_song",
            'cultural': f"childhood_song",
            'emotional': f"childhood_song"
        },
        'time': {
            'biological': "childhood_song",
            'cultural': "childhood_song",
            'emotional': "childhood_song"
        }
    },
    "Study": {
        'hearing': {
            'biological': f"last_semester",
            'cultural': f"last_semester",
            'emotional': f"last_semester"
        },
        'touch': {
            'biological': "last_semester",
            'cultural': "last_semester",
            'emotional': "last_semester"
        },
        'sight': {
            'biological': f"last_semester",
            'cultural': f"last_semester",
            'emotional': f"last_semester"
        },
        'smell': {
            'biological': f"last_semester",
            'cultural': f"last_semester",
            'emotional': f"last_semester"
        },
        'taste': {
            'biological': f"last_semester",
            'cultural': f"last_semester",
            'emotional': f"last_semester"
        },
        'body': {
            'biological': f"last_semester",
            'cultural': f"last_semester",
            'emotional': f"last_semester"
        },
        'time': {
            'biological': "last_semester",
            'cultural': "last_semester",
            'emotional': "last_semester"
        }
    }
}

CURRENT_EVENTS = {
    'hearing': {
        'biological': "hearing:event_receivedl",
        'cultural': "hearing:event_received",
        'emotional': "hearing:event_received"
    },
    'touch': {
        'biological': "touch:event_received",
        'cultural': "touch:event_received",
        'emotional': "touch:event_received"
    },
    'sight': {
        'biological': f"sight:event_received",
        'cultural': f"sight:event_received",
        'emotional': f"sight:event_received"
    },
    'smell': {
        'biological': f"smell:event_received",
        'cultural': f"smell:event_received",
        'emotional': f"smell:event_received"
    },
    'taste': {
        'biological': f"taste:event_received",
        'cultural': f"taste:event_received",
        'emotional': f"taste:event_received"
    },
    'body': {
        'biological': f"body:event_received",
        'cultural': f"body:event_received",
        'emotional': f"body:event_received"
    },
    'time': {
        'biological': "body:event_received",
        'cultural': "body:event_received",
        'emotional': "body:event_received"
    }
}


class Memory:
    def __init__(self):
        self.temporal_memory = {}

    def set_event(self, event):
        self.event = event

    def get_memories(self, bce_modified_by_senses: dict):

        memories = {}

        for sense in SENSES:
            bce_by_sense = bce_modified_by_senses[sense]
            memories[sense] = {}
            for state in STATES:
                memories[sense][state] = 0
                bce_modified = bce_by_sense[state]
                if bce_modified:
                    memories[sense][state] = self.temporal_memory[sense][state] + " -> " + MEMORIES[self.event][sense][state]

        return memories

    def get_current_temporal_memory(self):
        for sense in SENSES:
            self.temporal_memory[sense] = {}
            for state in STATES:
                self.temporal_memory[sense][state] = self.event
        return self.temporal_memory

    def get_details(self):
        details = {}
        for sense in CURRENT_EVENTS:
            details[sense] = {}
            for state in STATES:
                num_registers = 1000
                details[sense][state] = {
                    "number_registers": num_registers,
                    "number_occurrences": round(random.randint(0,num_registers)),
                }
        return details
