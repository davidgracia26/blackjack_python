from random import random
from math import floor

from CardType import CardType


class Card:
    def __init__(self):
        self.suit = ""
        self.type = None
        self.values = []

    @staticmethod
    def draw(deck_cards, hand):
        card_idx = floor(random() * len(deck_cards))
        hand.append(deck_cards[card_idx])
        del deck_cards[card_idx]

    @staticmethod
    def sum(hand):
        ace_cards = list(filter(lambda card: card.type == CardType.Ace, hand))
        non_ace_cards = list(filter(lambda card: card.type != CardType.Ace, hand))

        if ace_cards:
            sum_of_non_aces = sum([card.values[0] for card in non_ace_cards])
            if len(ace_cards) == 1:
                sum_using_ace_as_eleven = sum_of_non_aces + max(ace_cards[0].values)
                sum_using_ace_as_one = sum_of_non_aces + min(ace_cards[0].values)

                return sum_using_ace_as_one if sum_using_ace_as_eleven > 21 else sum_using_ace_as_eleven
            else:
                sum_using_one_ace_as_eleven = sum_of_non_aces + max(ace_cards[0].values) + (len(ace_cards) - 1) * min(ace_cards[0].values)
                sum_using_all_aces_as_one = sum_of_non_aces + len(ace_cards) * min(ace_cards[0].values)

                return sum_using_all_aces_as_one if sum_using_one_ace_as_eleven > 21 else sum_using_one_ace_as_eleven

        return sum([card.values[0] for card in hand])

    def get_card_name(self):
        if self.type == CardType.Ace:
            return "A"
        if self.type == CardType.Jack:
            return "J"
        if self.type == CardType.Queen:
            return "Q"
        if self.type == CardType.King:
            return "K"

        return self.values[0]