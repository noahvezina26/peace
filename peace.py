# Import necessary modules
import random
import time

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Split the deck into two hands
player1_hand = deck[:26]
player2_hand = deck[26:]


def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
    Return 1 if player 1's card is strong, 2 for player 2
    if the cards are equal, return 0.

    Hint, using the index function will make this very simple (one liner)"""

    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
        return 1
    elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
        return 2
    else:
        return 0


print(card_comparison(("2", "hearts"), ("K", "diamonds")))


def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
    That is, each player flips a card, and the winner is determined using the card_comparison function
    if both players flip the same value card, call the war function
    """

    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)

    wager = []

    while True:
        wager.append(p1_card)
        wager.append(p1_card)

        print(f"Player 1 played a {p1_card[0]} of {p1_card[1]}!")
        print(f"Player 2 played a {p2_card[0]} of {p2_card[1]}!")

        case = card_comparison(p1_card, p2_card)

        if case == 1:
            player1_hand += wager
            print("Player 1 wins the battle!\n")
            break
        elif case == 2:
            player2_hand += wager
            print("Player 2 wins the battle!\n")
            break
        else:
            print("\nWAR! Each player has put down an additional three cards!\n")
            p1_card, p2_card, extra_cards = war(player1_hand, player2_hand)
            wager += extra_cards


def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
    recall the rules of war, both players put 3 cards face down,
    then both players flip face up a 4th card. The player with the stronger
    card takes all the cards.
    """

    if len(player1_hand) > 4:
        p1_cards = player1_hand[:4]
        del player1_hand[:4]
    else:
        p1_cards = player1_hand
        del player1_hand

    if len(player2_hand) > 4:
        p2_cards = player2_hand[:4]
        del player2_hand[:4]
    else:
        p2_cards = player2_hand
        del player2_hand

    return p1_cards[-1], p2_cards[-1], p1_cards[:-1] + p2_cards[:-1]


def play_game():
    """Main function to run the game."""

    while len(player1_hand) > 0 and len(player2_hand) > 0:
        play_round(player1_hand, player2_hand)
        time.sleep(1)

    if len(player1_hand) == 0:
        print("Player 2 won!")
    else:
        print("Player 1 won!")


# Call the main function to start the game
play_game()
