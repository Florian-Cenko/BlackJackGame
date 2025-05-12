# ♠️ Blackjack Game (Python Terminal)

This is a simple **Blackjack (21)** game built in Python using object-oriented programming principles.  
The player plays against a dealer, managing chips and making bets each round.

---

## 🕹 Features

- Full deck of 52 cards with suits and values
- Dealer and player hands
- Betting system (starts with 100 chips)
- Ace automatically adjusts value from 11 to 1 if needed
- Input validation (bets, moves)
- Game loop with replay option

---

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/Florian-Cenko/BlackjackPython.git
   cd BlackjackPython

Run the game:
   - python BlackJack.py


🎮 How to Play
1. Place your bet: At the beginning of each round, you'll be prompted to enter how many chips you'd like to bet.

2. Player's turn: After the initial cards are dealt, you can choose to either "Hit" (get another card) or "Stand" (end your turn).

3. Dealer's turn: The dealer will automatically hit until they reach a value of 17 or more.

4. End of round: After both the player and the dealer complete their turns, the winner is determined:

   -If the player's total hand value exceeds 21, they bust and lose the bet.

   -If the dealer's hand exceeds 21, the dealer busts and the player wins.

   -If the player's hand value is higher than the dealer's, the player wins.

   -If both hands have the same value, it's a tie (push).

5. Play again: After each round, you can choose to play again.


