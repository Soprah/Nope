import unittest

from src.gamelogic.card.ActionCard import ActionCard


class TestActionCardInit(unittest.TestCase):
    def test_init_valid_effect(self):
        restart_card = ActionCard(3, (("red"), ("blue"), ("yellow"), ("green")), "RESTART")
        view_card = ActionCard(8, ("yellow"), "VIEW")
        selection_card = ActionCard(19, ("blue"), ("SELECTION"))

    def test_init_invalid_effect(self):
        with self.assertRaises(ValueError):
            invalid_effect_card = ActionCard(1, ("green"), ("MONKEY"))


if __name__ == '__main__':
    unittest.main()
