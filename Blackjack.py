import random

def create_deck():
    """Creates a standard deck of cards."""
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def draw_card(deck):
    """Draws a random card from the deck."""
    return deck.pop()

def calculate_total(cards):
    """Calculates the total value of the player's or dealer's cards."""
    total = sum(card_value(card) for card in cards)
    if total == 21:
        return total, True  # Blackjack
    elif total > 21:
        return total, False  # Bust
    return total, None

def card_value(card):
    """Returns the value of a card."""
    rank = card[0]
    if rank in ['Jack', 'Queen', 'King']:
        return 10
    elif rank == 'Ace':
        return 11  # For simplicity, Ace is initially considered 11
    else:
        return int(rank)

def play_game():
    """Main function to play the game."""
    starting_cash = 1000
    min_bet = 1
    
    while True:
        cash = starting_cash
        while cash > 0:
            print("\nWelcome to Blackjack!")
            print(f"You have ${cash}.")
            
            max_bet = cash
            bet = int(input(f"Please choose your bet amount (min: ${min_bet}, max: ${max_bet}): "))
            if bet < min_bet or bet > max_bet:
                print("Invalid bet amount. Please choose a valid bet.")
                continue

            # Initialize player and dealer hands
            deck = create_deck()
            player_cards = [draw_card(deck), draw_card(deck)]
            dealer_cards = [draw_card(deck), draw_card(deck)]

            # Display initial hands
            print("\nYour cards:", player_cards)
            print("Dealer's cards:", [dealer_cards[0], '*'])

            # Player's turn
            while True:
                choice = input("\nHit (H) or Stand (S): ").upper()
                if choice == 'H':
                    player_cards.append(draw_card(deck))
                    print("Your cards:", player_cards)
                    total, blackjack = calculate_total(player_cards)
                    if blackjack:
                        print("Blackjack! You win!")
                        cash += bet * 2
                        break
                    elif total > 21:
                        print("Bust! You lose.")
                        cash -= bet
                        break
                elif choice == 'S':
                    break
                else:
                    print("Invalid choice. Please enter H or S.")

            # Dealer's turn
            if total <= 21:
                while True:
                    dealer_total, _ = calculate_total(dealer_cards)
                    if dealer_total >= 17:
                        break
                    dealer_cards.append(draw_card(deck))
                    print("Dealer draws a card.")

                print("\nDealer's cards:", dealer_cards)

                # Determine winner
                player_total, _ = calculate_total(player_cards)
                if dealer_total > 21 or (player_total <= 21 and player_total > dealer_total):
                    print("You win!")
                    cash += bet * 2
                elif dealer_total == player_total:
                    print("It's a tie!")
                else:
                    print("Dealer wins!")
                    cash -= bet

            print(f"Your current balance: ${cash}")

        play_again = input("\nDo you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
