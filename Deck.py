from Card import Card
from CardType import CardType


class Deck:
    def __init__(self):
        self.cards = []
        self.deck_size = 52

    def create(self):
        suits = ["\u2660", "\u2665", "\u2666", "\u2663"]
        for suit in suits:
            for value in range(1, 14, 1):
                card = Card()
                card.suit = suit

                if value == CardType.Jack.value:
                    card.type = CardType.Jack
                    card.values.append(10)
                elif value == CardType.Queen.value:
                    card.type = CardType.Queen
                    card.values.append(10)
                elif value == CardType.King.value:
                    card.type = CardType.King
                    card.values.append(10)
                elif value == CardType.Ace.value:
                    card.type = CardType.Ace
                    card.values.extend([1, 11])
                else:
                    card.values.append(value)

                self.cards.append(card)

        return self

    def initial_deal(self, deck_cards, dealer_hand, player_hand):
        for card_count in range(4):
            if card_count % 2 == 0:
                Card.draw(deck_cards, player_hand)
            else:
                Card.draw(deck_cards, dealer_hand)