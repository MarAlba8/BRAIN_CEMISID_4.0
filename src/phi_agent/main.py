# from mind.mind import Mind
# from phi_agent.src.memories_mock import Memory
# from phi_agent.src.settings import log
# from phi_agent.src.utils.need import Need
# from utils.utils import bce_agent_to_mind_translator
# from utils.bce import BCE
#
#
# if __name__ == '__main__':
#     from phi_agent.src.utils.fuzzy_logic import fuzzy_logic
#
#     # fuzzy_logic(number_registers=10, number_occurrences=2, agent_current_state=50)
#     # -------------------- Test Michael
#     # from rn_7_sentidos import RN_7_sentidos
#     # from agente_inteligente import Agente_Inteligente
#     #
#     # rn_sentidos = RN_7_sentidos()
#     # agente_inteligente = Agente_Inteligente()
#     #
#     # # Lista de eventos de entradas
#     # eventos = ["evento_a", "evento_b", "evento_c", "evento_d", "evento_e", "evento_f", "evento_g", "evento_h", "evento_i"]
#     #
#     # # entrada de eventos a la red neuronal de michael
#     # bce_7 = rn_sentidos.recibir_evento(eventos)  # -> (BCE, #RN, evento):
#
#     mind = Mind()
#
#     # bce for testing (Michael)
#     bce = BCE()
#     agent_bce = BCE(need_bio=Need(1,2), need_emo=Need(0,0), need_cul=Need(0,3))
#
#     for i in range(3):
#
#         bce_7 = [[[0, bce], 'sight'],
#                  [[2, bce], 'hearing'],
#                  [[0, bce], 'taste'],
#                  [[2, bce], 'touch'],
#                  [[0, bce], 'body'],
#                  [[0, bce], 'smell'],
#                  [[0, bce], 'time']]
#
#         rn_bce_by_senses = bce_agent_to_mind_translator(bce_senses=bce_7)
#
#         # memories for testing (Daniel)
#         memory = Memory()
#
#         ## get_details -> Details for all senses
#         # details["hearing"] = {
#         #     "number_registers": 10,
#         #     "number_occurrences": 9,
#         # }
#         memory_details = memory.get_details()
#
#         bce_winners, bce_modified = mind.call_internal_comparator(
#             agent_bce=agent_bce,
#             bce_senses=rn_bce_by_senses,
#             memory_details=memory_details
#         )
#         log.msg(f"bce winners: {bce_winners}, bce modified: {bce_modified}")
#
#         ## get_memories -> send a dict like this
#         # bce_modified = {
#         #     "biological": 0,
#         #     "cultural": 1,
#         #     "emotional": 1,
#         # }
#         ##
#         memories = memory.get_memories(bce_modified_by_senses=bce_modified)
#
#         temporal_memory = memory.get_current_temporal_memory()
#         mind.update_attention(memories=memories, temporal_memory=temporal_memory)
#
#         new_bce = mind.get_unified_bce(bce_by_senses=bce_winners)
#         agent_bce = new_bce
#         print(f"-------------New BCE {new_bce} -------------")
