from src.gamelogic.card.ActionCard import ActionCard
from src.gamelogic.card.RestartCard import RestartCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard

restart_card = RestartCard(1, (("red"), ("blue"), ("yellow"), ("green")))
view_card = ViewCard(1, ("red"))
selection_card = SelectionCard(1, ("red"))
print(restart_card)
print(view_card)