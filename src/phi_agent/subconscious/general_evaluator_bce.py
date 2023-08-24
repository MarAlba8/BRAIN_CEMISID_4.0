from src.michael_agent.bce import BCE


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

    current_bce = bce_winners[0]
    bce_average = current_bce.average(bce_winners[1],bce_winners[2],bce_winners[3],bce_winners[4],bce_winners[5],bce_winners[6])
    return bce_average
