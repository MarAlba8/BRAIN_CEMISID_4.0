from history import History

if __name__ == "__main__":
    h = History()
    b = h.memories.get('biological')

    h.add_pattern(event='Agrado_b', sense='sight', neuron_number=1)
    h.add_pattern(event='Agrado_e', sense='sight', neuron_number=89)
    h.add_pattern(event='Test_b', sense='touch', neuron_number=7)
    h.add_pattern(event='Test_e', sense='touch', neuron_number=42)
    h.add_memory(event='Cancion', sense='sight', neuron_number=2, pattern_list=['Agrado'])
    h.add_memory(event='Tesis', sense='sight', neuron_number=3, pattern_list=['Cancion'])
    h.fill_life_episode(event='Pelicula', sense='sight', neuron_number=9, pattern_list=['Tesis'])
    h.add_memory(event='asd', sense='touch', neuron_number=234, pattern_list=['Test'])
    h.fill_life_episode(event='Evento 2', sense='touch', neuron_number=98, pattern_list=['Test'])
    h.handle_attention('biological', 'Pelicula,Tesis,Cancion')
    h.handle_attention('emotional', 'Pelicula,Tesis,Cancion')

    print('le', h.get_life_episodes())
    print(h.get_stats())
    print(b.get_all())

    MEMORIES = {
        'hearing': {
            'biological': 1,
            'cultural': 1,
            'emotional': 1
        },
        'touch': {
            'biological': 1,
            'cultural': 1,
            'emotional': 1
        },
        'sight': {
            'biological': 1,
            'cultural': 1,
            'emotional': 1
        },
        'smell': {
            'biological': 1,
            'cultural': 0,
            'emotional': 0
        },
        'taste': {
            'biological': 1,
            'cultural': 0,
            'emotional': 0
        },
    }

    print(h.get_memory_sequences(MEMORIES))

