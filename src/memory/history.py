from memory.memory import Memory


class History:
    def __init__(self):
        self.memories = {
            'biological': Memory('biological'),
            'emotional': Memory('emotional'),
            'cultural': Memory('cultural')
        }

    def init_history(self,arr_patters):
        for sense_patters in arr_patters:
            for pattern in sense_patters:
                self.add_pattern(pattern[0], pattern[1], pattern[2])

    def get_memory_sequences(self, params: dict):
        memory_sequence_by_sense = {}

        for sense, sense_params in params.items():
            memory_sequence = {}
            for memory_type, memory_instance in self.memories.items():
                suffix = None
                if sense_params[memory_type] == 1:
                    memory_sequence[memory_type] = memory_instance.get_memory_sequence(sense)

            memory_sequence_by_sense[sense] = memory_sequence

        return memory_sequence_by_sense

    def add_pattern(self, event, sense, neuron_number, pattern_list=None):
        memory_type = self.get_memory_type(event)
        if memory_type is None:
            raise ValueError("Invalid pattern.")

        memory = self.memories[memory_type]
        event_without_suffix = event.rstrip('_bce')
        memory.add_memory(event_without_suffix, sense, neuron_number, pattern_list)

    def add_memory(self, event, sense, neuron_number, pattern_list=None):
        for memory_type, memory_instance in self.memories.items():
            memory_instance.add_memory(event, sense, neuron_number, pattern_list)

    @staticmethod
    def get_memory_type(event):
        suffix_map = {
            '_b': 'biological',
            '_e': 'emotional',
            '_c': 'cultural'
        }

        for suffix, memory_type in suffix_map.items():
            if event.endswith(suffix):
                return memory_type

        return None

    def fill_life_episode(self, event, sense, neuron_number, pattern_list=None):
        for memory_type, memory_instance in self.memories.items():
            memory_instance.fill_life_episode(event, sense, neuron_number, pattern_list)

    def handle_attention(self, factor, memory_sequence, pattern=None):
        memory_instance = self.memories.get(factor)
        memory_instance.handle_attention(memory_sequence, pattern)

    def get_stats(self):
        stats = {}
        for memory_type, memory_instance in self.memories.items():
            stats[memory_type] = memory_instance.get_stats()

        return stats