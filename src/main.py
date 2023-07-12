from michael_agent.intelligent_agent import Intelligent_agent
from michael_agent.sensory_system import Sensory_system
from michael_agent.generator import Generator

from memory.history import History

from phi_agent.mind.mind import Mind
from phi_agent.utils.utils import bce_agent_to_mind_translator, get_temporal_memory


if __name__ == '__main__':
    sensory_system = Sensory_system()
    intelligent_agent = Intelligent_agent()
    memory = History()
    mind = Mind()

    event_generator = Generator()
    event_generator.gen_patterns()

    #entrada de eventos a la red neuronal de michael
    bce_7 = sensory_system.set_event(event_generator.gen_event())

    #entrada del comparador 1 de maria para actualizar los bce de las neuronas
    rn_bce_by_senses = bce_agent_to_mind_translator(bce_senses=bce_7)
    memory_stats = memory.get_stats()
    bce_winners, bce_modified = mind.call_internal_comparator(
        agent_bce=intelligent_agent.status(),
        bce_senses=rn_bce_by_senses,
        memory_stats=memory_stats
    )
    sensory_system.update_neuron(bce_winners)

    memories = memory.get_memory_sequences(params=bce_modified)
    ## falta tomar la primera parte de lo que Daniel regrese, lo que se guardara
    # como memoria temporal
    temporal_memory = get_temporal_memory(memories)
    new_thoughts_by_factor = mind.update_attention(memories=memories, temporal_memory=temporal_memory)

    for factor in new_thoughts_by_factor:
        for memory_sequence in new_thoughts_by_factor[factor]:
            memory.handle_attention(factor, memory_sequence=memory_sequence)

    new_bce = mind.get_unified_bce(bce_by_senses=bce_winners)
    intelligent_agent.add_bce(new_bce)
