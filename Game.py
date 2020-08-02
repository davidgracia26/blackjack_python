from Card import Card
from Deck import Deck
from PlayerType import PlayerType


class Game:
    def __init__(self):
        self.turn = PlayerType.Player
        self.is_over = False
        self.winner = None

    def run(self):
        dealer_hand = []
        player_hand = []
        deck = Deck().create()

        deck.initial_deal(deck.cards, dealer_hand, player_hand)
        print("\n")

        self.print_dealer_initial_hand(dealer_hand)
        self.print_hand(player_hand, PlayerType.Player)

        self.check_for_blackjack(dealer_hand, PlayerType.Dealer)
        self.check_for_blackjack(player_hand, PlayerType.Player)

        while self.turn == PlayerType.Player and self.is_over == False:
            response = input("Hit or Stay: Type H or S\n").strip().lower()
            if response == "s":
                self.turn = PlayerType.Dealer
                print("\n")
            elif response == "h":
                print("\n")
                self.draw_card_and_check_for_winner(deck.cards, player_hand, PlayerType.Player)
            else:
                print("\nInvalid response. Please type H or S\n")

        self.print_hand(dealer_hand, PlayerType.Dealer)
        while self.turn == PlayerType.Dealer and self.is_over == False:
            self.check_for_bust(dealer_hand, PlayerType.Dealer)

            dealer_hand_sum = Card.sum(dealer_hand)
            player_hand_sum = Card.sum(player_hand)

            if (17 < dealer_hand_sum <= 21) and dealer_hand_sum > player_hand_sum:
                self.winner = PlayerType.Dealer
                self.is_over = True

            self.draw_card_and_check_for_winner(deck.cards, dealer_hand, PlayerType.Dealer)

        self.print_final_outcome(dealer_hand, player_hand)

        input("\nPress enter key to end game")

    def print_hand(self, hand, player_type):
        if player_type == PlayerType.Player:
            print("Player's hand:")
        elif player_type == PlayerType.Dealer:
            print("Dealer's hand:")

        [print(f"{Card.get_card_name(card)} {card.suit}\n") for card in hand]

    def print_dealer_initial_hand(self, hand):
        print("Dealer's Hand")
        card_to_show = hand[-1]
        print(f"?? {Card.get_card_name(card_to_show)} {card_to_show.suit}\n")

    def print_final_outcome(self, dealer_hand, player_hand):
        print("-------------------")
        print(f"Dealer Score {Card.sum(dealer_hand)}")
        print(f"Player Score {Card.sum(player_hand)}")
        print("-------------------")

        if self.winner == PlayerType.Dealer:
            print("Dealer Wins")
        if self.winner == PlayerType.Player:
            print("Player Wins")

    def end(self, winner):
        if winner == PlayerType.Player:
            print("Player Wins")
        elif winner == PlayerType.Dealer:
            print("Dealer Wins")

        self.is_over = True

    def check_for_blackjack(self, hand, player_type):
        if Card.sum(hand) == 21:
            self.winner = player_type
            self.is_over = True

    def check_for_bust(self, hand, player_type):
        if Card.sum(hand) > 21:
            self.winner = PlayerType.Dealer if player_type == player_type.Player else PlayerType.Player
            self.is_over = True

    def draw_card_and_check_for_winner(self, deck_cards, hand, player_type):
        Card.draw(deck_cards, hand)

        self.check_for_bust(hand, player_type)
        self.check_for_blackjack(hand, player_type)

        self.print_hand(hand, player_type)