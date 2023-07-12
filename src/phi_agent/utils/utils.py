def bce_agent_to_mind_translator(bce_senses: list):
    mind_bce = {}

    for sense in bce_senses:
        # Need()
        sense_name = sense[1]
        states = sense[0][1]

        mind_bce[sense_name] = {}
        mind_bce[sense_name]["biological"] = states.biologico
        mind_bce[sense_name]["cultural"] = states.cultural
        mind_bce[sense_name]["emotional"] = states.emocional

    return mind_bce

def get_temporal_memory(memories):
    ## falta por definir
    pass