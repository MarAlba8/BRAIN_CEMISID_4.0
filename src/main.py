from phi_agent.memories_mock import Memory
from phi_agent.settings import log
from phi_agent.utils.need import Need

from michael_agent.intelligent_agent import Intelligent_agent
from michael_agent.sensory_system import Sensory_system
from phi_agent.mind.mind import Mind
from phi_agent.utils.utils import bce_agent_to_mind_translator
from src.michael_agent.generator import Generator

if __name__ == '__main__':
    from phi_agent.utils.fuzzy_logic import fuzzy_logic

    # fuzzy_logic(number_registers=10, number_occurrences=2, agent_current_state=50)
    # -------------------- Test Michael
    # from rn_7_sentidos import RN_7_sentidos
    # from agente_inteligente import Agente_Inteligente
    #
    # rn_sentidos = RN_7_sentidos()
    # agente_inteligente = Agente_Inteligente()
    #
    # # Lista de eventos de entradas
    # eventos = ["evento_a", "evento_b", "evento_c", "evento_d", "evento_e", "evento_f", "evento_g", "evento_h", "evento_i"]
    #
    # # entrada de eventos a la red neuronal de michael
    # bce_7 = rn_sentidos.recibir_evento(eventos)  # -> (BCE, #RN, evento):

    sensory_system = Sensory_system()
    intelligent_agent = Intelligent_agent()

    #Agente Daniel
    # memoria_daniel = MemoriaDaniel()

    #Lista de eventos de entradas
    # eventos = ["Tesis:Tesis2","pattern_hearing_b:Musica","pattern_smell_c:cafe_olor","pattern_taste_c:Cafe_taste",
    #               "Textura_silla:Textura_cojin","pattern_body_b:Neutro","pattern_time_c:Neutro2"]

    eventos = [
        'pattern_b_sight:event_a',
        'pattern_zero2_hearing:event_i',
        'pattern_zero2_smell:event_d',
        'pattern_zero2_taste:event_c',
        'pattern_f_touch:event_c',
        'pattern_e_body:event_a',
        'pattern_g_time:event_e'
    ]

    event_generator = Generator()
    event_generator.gen_patterns()

    #entrada de eventos a la red neuronal de michael
    # bce_7 = sensory_system.set_event(event_generator.gen_event())
    bce_7 = sensory_system.set_event(eventos)

    #entrada del comparador 1 de maria para actualizar los bce de las neuronas
    rn_bce_by_senses = bce_agent_to_mind_translator(bce_senses=bce_7)

    # memories for testing (Daniel)
    ## Michael pasa el evento y los ID
    memory = Memory()

    ## get_details -> Details for all senses
    # details["hearing"] = {
    #     "number_registers": 10,
    #     "number_occurrences": 9,
    # }
    memory_details = memory.get_details()

    mind = Mind()
    bce_winners, bce_modified = mind.call_internal_comparator(
        agent_bce=intelligent_agent.status(),
        bce_senses=rn_bce_by_senses,
        memory_details=memory_details
    )
    # log.msg(f"bce winners: {bce_winners}, bce modified: {bce_modified}")

    ## get_memories -> send a dict like this
    # bce_modified = {
    #     "biological": 0,
    #     "cultural": 1,
    #     "emotional": 1,
    # }
    ##
    memories = memory.get_memories(bce_modified_by_senses=bce_modified)

    sensory_system.update_neuron(bce_winners)

    temporal_memory = memory.get_current_temporal_memory()
    new_thoughts_by_factor = mind.update_attention(memories=memories, temporal_memory=temporal_memory)

    memory.save(new_thoughts_by_factor)
    # update memory?
    new_bce = mind.get_unified_bce(bce_by_senses=bce_winners)
    # agent_bce = new_bce

    intelligent_agent.add_bce(new_bce)

    print(f"-------------New BCE {intelligent_agent.status()} -------------")


    # bce for testing (Michael)
    # bce = BCE()
    # agent_bce = BCE(need_bio=Need(1,2), need_emo=Need(0,0), need_cul=Need(0,3))









# from src.michael_agent.sensory_system import Sensory_system
# from src.michael_agent.intelligent_agent import Intelligent_agent
#
# sensory_system = Sensory_system()
# intelligent_agent = Intelligent_agent()
#
# #Agente Daniel
# memoria_daniel = MemoriaDaniel()
#
# #Lista de eventos de entradas
# eventos = []
#
# #entrada de eventos a la red neuronal de michael
# bce_7 = sensory_system.set_event(eventos) #-> (BCE, #RN, evento):
#
# #entrada del comparador 1 de maria para actualizar los bce de las neuronas
# sensory_system.update_neuron(AgenteMaria().comparador)
#
# #Datos de las neuronas actualizadas con sus bce
# bce_7_actualizado = agente_inteligente.status()
#
# #Entrada de ids de las neuronas al modulo de memoria de daniel
# memoria_daniel.set_rn(bce_7_actualizado.id)
#
# #Agente Maria que requiere como entrada la memoria de daniel
# mind = Mind(memoria_daniel)
#
# #Agente de Maria que requiere como entrada los BCE en formato de diccionario y
# mind.start_process(bce_7.traduccion,  agente_inteligente.status())
#
