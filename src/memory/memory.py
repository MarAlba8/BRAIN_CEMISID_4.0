class Memory:
    def __init__(self, factor):
        self.factor = factor
        self.life_history = {}
        self.life_episode = {}
        self.stats = {}

    def add_memory(self, event, sense, neuron_number, pattern_list=None):
        new_memory = {
            'event': event,
            'sense': sense,
            'neuron_number': neuron_number,
            'pattern_list': pattern_list,
            'linked_to': []
        }

        if pattern_list is not None:
            for pattern in pattern_list:
                if pattern is not None:
                    memory = self.life_history.get(pattern)
                    if memory is not None and memory['pattern_list'] is not None:
                        memory['linked_to'].append(event)

        # Cancion -> pattern_list: [Agrado]
        # Tesis -> pattern_list: [Cancion]
        # Cancion -> pattern_list: [Agrado], linked_to: [Tesis]

        # Pelicula -> pattern_list: [Tesis]
        # Tesis -> pattern_list: [Cancion], linked_to: [Pelicula]

        # Tesis, Pelicula, Cancion, Agrado

        self.stats.setdefault(sense, {'number_registers': 0})
        self.stats[sense]['number_registers'] += 1
        self.life_history[event] = new_memory

    def fill_life_episode(self, event, sense, neuron_number, pattern_list):
        life_episode = {
            'event': event,
            'sense': sense,
            'neuron_number': neuron_number,
            'pattern_list': pattern_list
        }

        self.stats[sense]['number_occurrences'] = 0
        for key, values in self.life_history.items():
            if values['pattern_list'] is not None and event in values['pattern_list']:
                self.stats[sense]['number_occurrences'] += 1

        self.life_episode[event] = life_episode

    def update_memory(self, event, pattern):
        # What about if multiple patterns are linked to that memory??? 🤔
        self.life_history[event]['pattern_list'] = [pattern]

    def handle_attention(self, memory_sequence, pattern=None):
        new_event_key = memory_sequence.split(',')[0]
        new_event = self.life_episode.get(new_event_key, None)

        # handle bidirectional memories

        if self.life_history.get(new_event_key, None) is None and new_event is not None:
            self.add_memory(**new_event)

            if pattern is not None:
                self.update_memory(event=new_event['event'], pattern=pattern)

        elif self.life_history.get(new_event_key) is not None and pattern is not None:
            self.update_memory(event=new_event_key, pattern=pattern)

    def get_memory_sequence(self, sense):
        event = next((value for value in self.life_episode.values() if value['sense'] == sense), None)
        memory_sequence = []

        if event:
            # let's say an event exists in life_history, would it have the same patterns?
            element = self.life_history.get(event['event']) or event

            memory_sequence.append(element['event'])
            for pattern in element['pattern_list']:
                memory = self.life_history.get(pattern, None)
                self._traverse_memory(memory=memory, memory_sequence=memory_sequence)

        return memory_sequence

    def _traverse_memory(self, memory: dict, memory_sequence: list):
        memory_sequence.append(memory['event'])

        if self.life_history[memory['event']]['pattern_list'] is None:
            return

        for pattern in memory['pattern_list']:
            self._traverse_memory(self.life_history[pattern], memory_sequence)

    def get_stats(self):
        return self.stats

    def get_all(self):
        return self.life_history