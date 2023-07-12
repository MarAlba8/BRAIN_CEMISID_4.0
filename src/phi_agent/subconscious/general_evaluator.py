from phi_agent.settings import SENSES, STATES


def general_evaluator(thoughts_by_sense: dict) -> dict:
    senses = SENSES
    states = STATES

    states_new_thoughts = {}
    for state in states:
        states_new_thoughts[state] = []

    for sense in senses:
        for state in states:
            descriptor = thoughts_by_sense[sense].get(state)
            if descriptor:
                states_new_thoughts[state].append(descriptor)

    return states_new_thoughts
