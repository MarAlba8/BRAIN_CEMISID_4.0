from phi_agent.settings import STATES


def bce_agent_to_mind_translator(bce_senses: list):
    mind_bce = {}

    for sense in bce_senses:
        # Need()
        sense_name = sense[4]
        states = sense[1]

        mind_bce[sense_name] = {}
        mind_bce[sense_name]["biological"] = states.biological
        mind_bce[sense_name]["cultural"] = states.culture
        mind_bce[sense_name]["emotional"] = states.emotional

    return mind_bce


def get_temporal_memory(life_episode: dict):
    temporal_memory = {}

    for sense in life_episode:
        temporal_memory[sense] = {}
        for state in STATES:
            temporal_memory[sense][state] = life_episode[sense]["event"]
    return temporal_memory