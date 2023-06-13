class aiPlayer():
    username = "test"
    cards = []

    def think_of_move(self, turn_data):
        top_card =  turn_data["top_card"]
        hand =  turn_data["own_hand_cards"]
        # For example: ("red-red", 1), ("blue", 2), ("green", 3), etc.
        # A wild card has color "wild" and number 0
        # An action card has color "action" and number 0

        # Check if you have any cards that match the top card color or number
        card_frequency = {}
        matching_cards = []
        for card in hand:
            # top farben zu liste machen
            top_farben = []
            if isinstance(top_card[0], tuple):
                top_farben.append(top_card[0][0])
                top_farben.append(top_card[0][1])
            else:
                top_farben.append(top_card[0])

            for farbe in top_farben:
                if isinstance(card[0], tuple):
                    farbe_matched = card[0][0] == farbe or card[0][1] == farbe
                else:
                    farbe_matched = card[0] == farbe
            if farbe_matched or card[0] == "wild" or top_card[0] == "wild":
                matching_cards.append(card)  # farbe matched oder wildcard -> match

            # get color frequency
            if isinstance(card[0], tuple):
                for farbe in card[0]:
                    if farbe in card_frequency.keys():
                        card_frequency[farbe] += 1
                    else:
                        card_frequency[farbe] = 1
            else:
                if card[0] in card_frequency.keys():
                    card_frequency[card[0]] += 1
                else:
                    card_frequency[card[0]] = 1

        # If you have no matching cards, say NOPE and take a card from the draw pile
        if len(matching_cards) == 0:
            return "NOPE"

        # If you have only one matching card, play it
        if len(matching_cards) == 1:
            return matching_cards[0]

        # choose the best one based on some criteria
        # prefer wild cards over action cards over regular cards
        # prefer lower numbers over higher numbers
        # prefer colors that you have less of
        best_card = matching_cards[0]
        for card in matching_cards:
            # Compare the cards based on their type
            if best_card[0] == "wild":
                return best_card
            if card[0] == "wild" and best_card[0] != "wild":
                return card
            elif card[0] == "action" and best_card[0] not in ["wild", "action"]:
                best_card = card
            elif not isinstance(best_card[0], tuple) and isinstance(card[0], tuple):
                best_card = card
            elif card[0] not in ["wild", "action"] and best_card[0] not in ["wild", "action"]:
                # Compare the cards based on their number
                if card[1] < best_card[1]:
                    best_card = card
                elif card[1] == best_card[1]:
                    # Compare the cards based on their color frequency in your hand
                    # check card_frequency of both cards, choose the higher one
                    # if hand.count(card) < hand.count(best_card):
                    #    best_card = card
                    pass

        # Return the best card to play
        return best_card

        print("")

    def select_game_history(self, history_list):
        print("")


artificialPlayer = aiPlayer()


def test_case(hand, card, player, solution, test_name):
    turn_data = {
        "previous_selected_cards": None,
        "top_card": card,
        "amount_opponent_hand": None,
        "own_hand_cards": hand
    }
    move = player.think_of_move(turn_data)
    if solution == move:
        print("PASS {}".format(test_name))
    else:
        print("FAIL {} =/= {} - {}".format(move, solution, test_name))


def test():
    top_card = (("blue"), 1)
    hand = [(("red"), 1), (("blue"), 1), (("red"), 1), (("red"), 1)]
    test_case(hand, top_card, artificialPlayer, (("blue"), 1), "1POS")

    top_card = (("blue"), 1)
    hand = [(("blue"), 1)]
    test_case(hand, top_card, artificialPlayer, (("blue"), 1), "1POS-2")

    top_card = (("blue"), 1)
    hand = [(("red"), 1), (("red", "blue"), 1), (("red"), 1), (("red"), 1)]
    test_case(hand, top_card, artificialPlayer, (("red", "blue"), 1), "1POS-Bicolor")

    top_card = (("blue"), 1)
    hand = [(("red"), 1), (("blue", "red"), 1), (("red"), 1), (("red"), 1)]
    test_case(hand, top_card, artificialPlayer, (("blue", "red"), 1), "1POS-Bicolor")

    top_card = (("blue"), 1)
    hand = [(("wild"), 1), (("blue", "red"), 1), (("red"), 1), (("red"), 1)]
    test_case(hand, top_card, artificialPlayer, (("wild"), 1), "WILD")

    top_card = (("blue"), 1)
    hand = [(("red"), 1)]
    test_case(hand, top_card, artificialPlayer, "NOPE", "NOPE")

    top_card = (("blue"), 1)
    hand = [(("red"), 1), (("blue"), 28), (("blue"), 14), (("red"), 1)]
    test_case(hand, top_card, artificialPlayer, (("blue"), 14), "Lower-Value")

    top_card = (("blue"), 1)
    hand = [(("red"), 1), (("blue"), 28), (("blue","red"), 28), (("red"), 1)]
    test_case(hand, top_card, artificialPlayer, (("blue","red"), 28), "Bicolor")

    top_card = (("blue","red"), 1)
    hand = [(("red"), 1), (("blue"), 1), (("red"), 1), (("red"), 1)]
    test_case(hand, top_card, artificialPlayer, (("red"), 1), "Frequency1")

    top_card = (("blue","red"), 1)
    hand = [ (("blue"), 1),(("red"), 1), (("red"), 1), (("red"), 1)]
    test_case(hand, top_card, artificialPlayer, (("red"), 1), "Frequency2")

    top_card = (("blue","red"), 1)
    hand = [ (("blue"), 1),(("red"), 1), (("blue"), 1), (("blue"), 1)]
    test_case(hand, top_card, artificialPlayer, (("blue"), 1), "Frequency3")

