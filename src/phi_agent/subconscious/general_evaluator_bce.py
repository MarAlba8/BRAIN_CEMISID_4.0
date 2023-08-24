from michael_agent.bce import BCE


def general_evaluator_bce(bce_by_senses: dict) -> BCE:
    bce_winners = []
    for sense in bce_by_senses:
        bce_winner = bce_by_senses[sense]
        bce = BCE(
            bce_winner.get("biological"),
            bce_winner.get("cultural"),
            bce_winner.get("emotional"),
        )
        bce_winners.append(bce)

    #current_bce = bce_winners[0]
    bce_average = BCE.average(*bce_winners)
    return bce_average
