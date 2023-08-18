from phi_agent.utils.bce import BCE


def general_evaluator_bce(bce_by_senses: dict) -> BCE:
    bigger_bce = BCE()
    for sense in bce_by_senses:
        bce_states = bce_by_senses[sense]
        for state in bce_states:
            if state == "biological":
                if bce_states[state] > bigger_bce.biologico:
                    bigger_bce.biologico = bce_states[state]
            elif state == "cultural":
                if bce_states[state] > bigger_bce.cultural:
                    bigger_bce.cultural = bce_states[state]
            elif state == "emotional":
                if bce_states[state] > bigger_bce.emocional:
                    bigger_bce.emocional = bce_states[state]

    return bigger_bce
