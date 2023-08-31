# Modulo A
from michael_agent.intelligent_agent import Intelligent_agent
from michael_agent.sensory_system import Sensory_system
# Modulo B
from phi_agent.mind.mind import Mind
# Modulo C
from memory.history import History

from michael_agent.generator import Generator
from phi_agent.utils.utils import bce_agent_to_mind_translator, get_temporal_memory
import time
from rich import print

# Escala de degrees
LEN_DEGREE = 4

if __name__ == '__main__':
    sensory_system = Sensory_system()
    intelligent_agent = Intelligent_agent()
    memory = History()
    mind = Mind()
    event_generator = Generator()

    # Patrones para inicializar
    patterns = event_generator.gen_patterns()
    init_memories = event_generator.gen_init_events()
    # Inicializar el sensory_system y memoria
    init_patterns = sensory_system.init_patterns(patterns)
    memory.init_history(sensory_system.to_memory(), init_memories)

    # Bucle de eventos
    break_loop = False

    for i in range(10):

        sensory_events = event_generator.gen_event()
        print()

        agent_bce = intelligent_agent.status()
        print("\t\t[yellow]Estado Agente Inteligente:\t\t", agent_bce)

        # print("Eventos sensoriales de entrada:",sensory_events)

        # entrada de eventos a la red neuronal de michael
        bce_7 = sensory_system.set_event(sensory_events)

        print("Información de los eventos sensoriales:", bce_7)
        memory.get_events(bce_7)

        # entrada del comparador 1 de maria para actualizar los bce de las neuronas
        rn_bce_by_senses = bce_agent_to_mind_translator(bce_senses=bce_7)
        memory_stats = memory.get_stats()

        bce_winners, bce_modified, winners = mind.call_internal_comparator(
            agent_bce=agent_bce,
            bce_senses=rn_bce_by_senses,
            memory_stats=memory_stats
        )

        arr_bce_winners = sensory_system.get_bce_from_mind(bce_winners)

        print("BCE Ganadores:", bce_winners, winners)

        # update de la red neuronal
        sensory_system.update_neuron(arr_bce_winners)

        memories = memory.get_memory_sequences(params=bce_modified)

        life_episodes = memory.get_life_episodes()
        temporal_memory = get_temporal_memory(life_episodes)
        new_thoughts_by_factor = mind.update_attention(memories=memories, temporal_memory=temporal_memory)

        for factor in new_thoughts_by_factor:
            for memory_sequence in new_thoughts_by_factor[factor]:
                memory.handle_attention(factor, memory_sequence=memory_sequence)

        new_bce = mind.get_unified_bce()

        print("[green]BCE de entrada al Agente Inteligente:\t\t\t", new_bce)

        print("\t\t[yellow]Estado Agente Inteligente:\t\t", intelligent_agent.add_bce(new_bce))

        for factor in intelligent_agent.status().state():
            if factor[1] == intelligent_agent.length:
                print("[red]DEAD")
                break_loop = True
                break
        if break_loop:
            break

        time.sleep(5)

    mind.conscious.stop()
