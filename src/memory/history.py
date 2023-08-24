import json
from collections import defaultdict

from memory.memory import Memory


class History:
    def __init__(self):
        self.memories = {
            'biological': Memory('biological'),
            'emotional': Memory('emotional'),
            'cultural': Memory('cultural')
        }

    def init_history(self, arr_patterns):
        for sense_patterns in arr_patterns:
            for pattern in sense_patterns:
                self.add_pattern(pattern[0], pattern[1], pattern[2])

    def get_events(self, arr_events):
        for value in arr_events:
            id_neuron = value[0]
            sense = value[4]
            event = value[3]
            pattern = [value[2]]
            self.fill_life_episode(event, sense, id_neuron, pattern)

    def get_memory_sequences(self, params: dict):
        memory_sequence_by_sense = {}

        for sense, sense_params in params.items():
            memory_sequence = {}
            for memory_type, memory_instance in self.memories.items():
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
        stats = defaultdict(lambda: defaultdict(lambda: {'number_registers': 0, 'number_occurrences': 0}))
        all_memory_types = set(self.memories.keys())

        for memory_type, memory_instance in self.memories.items():
            memory_stats = memory_instance.get_stats()
            for sense, sense_stats in memory_stats.items():
                stats[sense][memory_type].update(sense_stats)

        for sense_stats in stats.values():
            for memory_type in all_memory_types:
                sense_stats.setdefault(memory_type, {'number_registers': 0, 'number_occurrences': 0})

        stats_json = json.dumps(stats)
        stats_dict = json.loads(stats_json)

        return stats_dict

    def get_life_episodes(self):
        life_episodes = {}

        for memory_type, memory_instance in self.memories.items():
            for event, episode in memory_instance.life_episode.items():
                sense = episode['sense']
                if sense not in life_episodes:
                    life_episodes[sense] = episode

        return life_episodes
