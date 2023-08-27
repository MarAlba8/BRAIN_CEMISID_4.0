from time import sleep

from phi_agent.conscious.conscious import Conscious
from phi_agent.subconscious.general_evaluator import general_evaluator
from phi_agent.subconscious.general_evaluator_bce import general_evaluator_bce
from phi_agent.subconscious.subconscious_by_sense import SubconsciousBySense

from phi_agent.settings import SENSES
from phi_agent.utils.bce import BCE

from phi_agent.settings import log


class Mind:
    def __init__(self):
        self.conscious = Conscious()
        senses = SENSES

        self.senses = {}
        for sense in senses:
            self.senses[sense] = SubconsciousBySense(conscious=self.conscious, sense=sense)

        self.bce_winners = {}
        self.states_new_thoughts = {}
        self.new_thoughts_by_sense = {}

    def call_internal_comparator(self, agent_bce: BCE, bce_senses: dict, memory_stats: dict):
        """
        Receive all seven BCE by sense and send it to each sense accordingly
        :param agent_bce:
        :param bce_senses:
        :return: BCE that wins inside the internal comparator
        """
        bce_modified = {}
        #print("DEBUG_MIND",memory_stats.values())
        winners = {}
        for sense in self.senses:
            self.bce_winners[sense] = {}
            
            self.bce_winners[sense], bce_modified[sense], winners[sense] = self.senses[sense].bce_comparator(
                agent_bce=agent_bce,
                neuronal_network_bce=bce_senses[sense],
                memory_details=memory_stats[sense]
            )

        #log.msg(self.bce_winners)
        return self.bce_winners, bce_modified, winners

    def update_attention(self, memories: dict, temporal_memory: dict):

        for sense in self.senses:
            new_thoughts = self.senses[sense].thought_picker(
                memories[sense], temporal_memory[sense]
            )
            self.new_thoughts_by_sense[sense] = new_thoughts

        self.states_new_thoughts = general_evaluator(
            self.new_thoughts_by_sense
        )

        ##version 2
        # for state in self.states_new_thoughts:
        len_biological = len(self.states_new_thoughts["biological"])
        len_cultural = len(self.states_new_thoughts["cultural"])
        len_emotional = len(self.states_new_thoughts["emotional"])

        max_len_state_thoughts = max(len_biological, len_cultural, len_emotional)

        log.msg("Updating attention")

        for i in range(max_len_state_thoughts):
            if i < len_biological:
                thought = self.states_new_thoughts["biological"][i]
                self.conscious.update_scope(state="biological", thought=thought)

            if i < len_cultural:
                thought = self.states_new_thoughts["cultural"][i]
                self.conscious.update_scope(state="cultural", thought=thought)

            if i < len_emotional:
                thought = self.states_new_thoughts["emotional"][i]
                self.conscious.update_scope(state="emotional", thought=thought)

            # sleep(1)

        log.msg("Current Phis")
        log.msg(self.conscious.get_phis())
        return self.states_new_thoughts

    def get_unified_bce(self):
        unified_bce = general_evaluator_bce(
            bce_by_senses=self.bce_winners
        )
        return unified_bce
