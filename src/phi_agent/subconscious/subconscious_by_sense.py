from phi_agent.conscious.conscious import Conscious
from michael_agent.bce import BCE

from phi_agent.utils.fuzzy_logic import fuzzy_logic


class SubconsciousBySense:
    def __init__(self, conscious: Conscious, sense: str):
        self.sense = sense
        self.conscious = conscious

        self.bce_winners = {}
        self.bce_modified = {}

    def thought_picker(self, memories: dict, temporal_memory: dict):
        current_thoughts = self.conscious.get_phis()
        for state in current_thoughts:
            if not current_thoughts[state]:
                current_thoughts[state] = temporal_memory[state]

        new_thoughts = self.new_thought_selector(memories, current_thoughts, self.bce_modified)
        return new_thoughts

    def bce_comparator(self, agent_bce: BCE, neuronal_network_bce: dict, memory_details: dict):
        number_registers = memory_details.get("number_registers")
        number_occurrences = memory_details.get("number_occurrences")

        # log.msg(f"agent_bce: {agent_bce}")
        # log.msg(f"neuronal_network_bce: {neuronal_network_bce}")

        for state in neuronal_network_bce.keys():
            rn_value = neuronal_network_bce[state]
            if state == "biological":
                agent_value = agent_bce.biological
            elif state == "cultural":
                agent_value = agent_bce.culture
            elif state == "emotional":
                agent_value = agent_bce.emotional

            if rn_value == agent_value:

                agent_degree_value = (agent_value.state[1] / agent_value.len_degree)*100
                tendency = fuzzy_logic(
                    number_registers=number_registers,
                    number_occurrences=number_occurrences,
                    agent_current_state=agent_degree_value
                )

                if tendency <= 50:
                    self.bce_winners[state] = agent_value
                    self.bce_modified[state] = 0
                else:
                    self.bce_winners[state] = rn_value
                    self.bce_modified[state] = 1
            elif rn_value >= agent_value:
                self.bce_winners[state] = rn_value
                self.bce_modified[state] = 1
            elif agent_value > rn_value:
                self.bce_winners[state] = agent_value
                self.bce_modified[state] = 0

        return self.bce_winners, self.bce_modified

    def new_thought_selector(
            self,
            memories: dict,
            current_thoughts: dict,
            states_modified: dict,
    ):
        """
        #Multiplexor
        Take memories and current thoughts, for those states that were modified by a memory
        creates a new thought and remove the old ones
        :param memories: data from the memory
        :param current_thoughts: current thoughts inside phi windows
        :param states_modified: have what states were modified by a memory and those
        that weren't
        :return: Descriptors of the new thoughts
        """

        new_thoughts = {}
        for state in current_thoughts:
            if states_modified[state]:
                new_thoughts[state] = memories[state]  # solo regresa los estados que se actualizaron
            else:
                new_thoughts[state] = current_thoughts[state]
        return new_thoughts
