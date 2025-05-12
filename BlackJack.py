import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' with value ' + str(self.value)


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces +=1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

 while True:
    try:
         chips.bet = int(input("Please how many chips do you want to bet:  "))
    except ValueError:
        print('Sorry, a bet must be an integer!')
    else:
        if chips.bet > chips.total:
            print("Sorry, your bet can't exceed", chips.total)
        else:
            break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # Αυτό λείπει

    # to control an upcoming while loop

    while True:
      inp = input("Would you like to Hit or Stand please insert h or s: ")

      if inp == 'h':
          hit(deck,hand)
      elif inp == 's':
          print("Player stands. Dealer is playing.")
          playing = False
      else:
          print("Sorry, please try again.")
          continue
      break


def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(f" {dealer.cards[1]}")
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print(f"Dealer's Hand = {dealer.value}")
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print(f"Player's Hand = {player.value}")

def player_busts(player,dealer,chips):
    print("Player Busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player Wins!")
    chips.win_bet()


def dealer_busts(player,dealer,chips):
    print("Dealer Busts!")
    chips.win_bet()


def dealer_wins(player,dealer,chips):
    print("Dealer Wins!")
    chips.lose_bet()


def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

if __name__ == "__main__":

    while True:
        print("Game Starts:")

        new_deck = Deck()
        new_deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(new_deck.deal())
        player_hand.add_card(new_deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(new_deck.deal())
        dealer_hand.add_card(new_deck.deal())


        player_chips = Chips()

        take_bet(player_chips)

        show_some(player_hand,dealer_hand)

        playing = True

        while playing:

            hit_or_stand(new_deck,player_hand)

            show_some(player_hand,dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)
                break

        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(new_deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        print(f"Player you have {player_chips.total}")

        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break








