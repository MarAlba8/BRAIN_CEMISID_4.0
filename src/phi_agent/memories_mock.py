from phi_agent.settings import SENSES

MEMORIES = {
    'hearing': {
        'biological': f"hearing:biological",
        'cultural': f"hearing:cultural",
        'emotional': f"hearing:emotional"
    },
    'touch': {
        'biological': "touch:biological",
        'cultural': "touch:cultural",
        'emotional': "touch:emotional"
    },
    'sight': {
        'biological': f"sight:biological",
        'cultural': f"sight:cultural",
        'emotional': f"sight:emotional"
    },
    'smell': {
        'biological': f"smell:biological",
        'cultural': f"smell:cultural",
        'emotional': f"smell:emotional"
    },
    'taste': {
        'biological': f"taste:biological",
        'cultural': f"taste:cultural",
        'emotional': f"taste:emotional"
    },
    'body': {
        'biological': f"body:biological",
        'cultural': f"body:cultural",
        'emotional': f"body:emotional"
    },
    'time': {
        'biological': "body:biological",
        'cultural': "body:cultural",
        'emotional': "body:emotional"
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
    def get_memories(self, bce_modified_by_senses: dict):

        print(f"bce_modified_by_sense: {bce_modified_by_senses}")
        states = {
            "biological": 0,
            "cultural": 0,
            "emotional": 0,
        }

        memories = {}
        for sense in SENSES:
            # just to create the dictionary with the states
            memories[sense] = states

        for sense in bce_modified_by_senses:
            bce_by_sense = bce_modified_by_senses[sense]
            for state in bce_by_sense:
                bce_modified = bce_by_sense[state]
                if bce_modified:
                    memories[sense][state] = MEMORIES[sense][state]

        return memories

    def get_current_temporal_memory(self):
        return CURRENT_EVENTS

    def get_details(self):
        details = {}
        for sense in CURRENT_EVENTS:
            details[sense] = {
                "number_registers": 10,
                "number_occurrences": 9,
            }
        return details
