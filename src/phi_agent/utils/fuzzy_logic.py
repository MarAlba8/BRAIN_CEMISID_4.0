import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


NUMBER_INTERVALS = 3
MAX_NUMBER_STATES = 100


def fuzzy_logic(number_registers: int, number_occurrences: int, agent_current_state: int) -> float:
    resulting_tendency = 0

    if not number_occurrences:
        return resulting_tendency

    occurrence = ctrl.Antecedent(np.arange(0, 100, 1), 'occurrence')
    current_state = ctrl.Antecedent(np.arange(0, 100, 1), 'current_state')
    tendency = ctrl.Consequent(np.arange(0, 100, 1), 'tendency')

    occurrence['low'] = fuzz.trapmf(occurrence.universe, [0, 0, 30, 40])
    occurrence['medium'] = fuzz.trapmf(occurrence.universe, [30, 40, 60, 70])
    occurrence['high'] = fuzz.trapmf(occurrence.universe, [60, 70, 100, 100])

    current_state['good'] = fuzz.trapmf(current_state.universe, [0, 0, 40, 60])
    current_state['bad'] = fuzz.trapmf(current_state.universe, [60, 70, 100, 100])

    tendency['low'] = fuzz.trapmf(tendency.universe, [0, 0, 40, 50]) ## agent  wins
    tendency['high'] = fuzz.trapmf(tendency.universe, [40, 50, 100, 100]) ## neuronal network wins

    rule1 = ctrl.Rule(occurrence['low'] & current_state['bad'], tendency['low'])
    rule2 = ctrl.Rule(occurrence['medium'] & current_state['bad'], tendency['low'])
    rule3 = ctrl.Rule(occurrence['high'] & current_state['bad'], tendency['low'])
    rule4 = ctrl.Rule(occurrence['low'] & current_state['good'], tendency['low'])
    rule5 = ctrl.Rule(occurrence['medium'] & current_state['good'], tendency['high'])
    rule6 = ctrl.Rule(occurrence['high'] & current_state['good'], tendency['high'])

    tendency_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
    tendency_modif = ctrl.ControlSystemSimulation(tendency_ctrl)

    occurrence_calc = (number_occurrences*100)/number_registers
    tendency_modif.input['occurrence'] = occurrence_calc
    tendency_modif.input['current_state'] = agent_current_state
    tendency_modif.compute()

    resulting_tendency = tendency_modif.output['tendency']
    #tendency.view(sim=tendency_modif)
    return resulting_tendency
