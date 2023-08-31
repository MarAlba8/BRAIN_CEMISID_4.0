class Memory:
    def __init__(self, factor):
        self.factor = factor
        self.life_history = {}
        self.life_episode = {}
        self.stats = {}

    def add_memory(self, event, sense, neuron_number, pattern_list=None):
        existing_memory = self.life_history.get(event)

        if pattern_list is not None and existing_memory is not None:
            new_patterns = set(pattern_list) - set(existing_memory.get('pattern_list', []))
            existing_memory.setdefault('pattern_list', []).extend(new_patterns)
            existing_memory['neuron_number'] = neuron_number

        self.stats.setdefault(sense, {}).setdefault('number_registers', 0)
        self.stats[sense]['number_registers'] += 1

        if existing_memory is None:
            self.life_history[event] = {
                'event': event,
                'sense': sense,
                'neuron_number': neuron_number,
                'pattern_list': list(set(pattern_list)) if pattern_list is not None else None
            }

    def fill_life_episode(self, event, sense, neuron_number, pattern_list):
        life_episode = {
            'event': event,
            'sense': sense,
            'neuron_number': neuron_number,
            'pattern_list': pattern_list
        }

        if sense not in self.stats:
            self.stats[sense] = {'number_registers': 0, 'number_occurrences': 0}

        self.stats[sense]['number_occurrences'] = 0
        self.life_episode[event] = life_episode
        seq = self.get_memory_sequence(sense)
        self.stats[sense]['number_occurrences'] = len(seq.split(','))

    def update_memory(self, event, pattern):
        self.life_history[event]['pattern_list'] = [pattern]

    def handle_attention(self, memory_sequence, pattern=None):
        new_event_key = memory_sequence.split(',')[0]
        new_event = self.life_episode.get(new_event_key, None)

        if self.life_history.get(new_event_key, None) is None and new_event is not None:
            self.add_memory(**new_event)

            if pattern is not None:
                self.update_memory(event=new_event['event'], pattern=pattern)

        elif self.life_history.get(new_event_key) is not None and pattern is not None:
            self.update_memory(event=new_event_key, pattern=pattern)

    def get_stats(self):
        return self.stats

    def get_all(self):
        return self.life_history

    def _traverse_memory(self, memory: dict, memory_sequence: list, visited: set):
        if memory is None or memory['event'] in visited:
            return

        visited.add(memory['event'])
        memory_sequence.append(memory['event'])

        if memory['pattern_list'] is None:
            return

        for pattern in memory['pattern_list']:
            if pattern in self.life_history:
                self._traverse_memory(self.life_history[pattern], memory_sequence, visited)

    def get_memory_sequence(self, sense):
        event = next((value for value in self.life_episode.values() if value['sense'] == sense), None)
        memory_sequence = []

        if event:
            aux = self.life_history.get(event['event'])
            if aux is not None:
                combined_patterns = set(event['pattern_list']) | set(aux['pattern_list'])
                event['pattern_list'] = list(combined_patterns)

            element = event

            self._traverse_memory(element, memory_sequence, set())

        return ','.join(memory_sequence)
