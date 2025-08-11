import random


def deal_cards():
    """Returns a random card from the deck."""
    cards = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    return random.choice(cards)


def swap_cards(cards):
    """Converts an Ace (11) to 1 if total is over 21."""
    while sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)


def blackjack(cards):
    """Checks if hand is a natural blackjack."""
    return sum(cards) == 21 and len(cards) == 2


# Initial hands
user_cards = [deal_cards(), deal_cards()]
computer_cards = [deal_cards(), deal_cards()]

swap_cards(user_cards)
swap_cards(computer_cards)

print(f"Here are your cards: {user_cards}")
print(f"Computer's first card: {computer_cards[0]}")


# Game function
def game():
    # Check starting blackjack cases
    if blackjack(user_cards) and blackjack(computer_cards):
        print(f"It's a draw! Your cards: {user_cards}, Computer's cards: {computer_cards}")
        return
    elif blackjack(user_cards):
        print(f"You win! You hit blackjack. Your cards: {user_cards}")
        return
    elif blackjack(computer_cards):
        print(f"You lose! Computer hits blackjack. Computer's cards: {computer_cards}")
        return

    # Player's turn
    while True:
        print(f"Your current hand: {user_cards}, current score: {sum(user_cards)}")
        choice = input("Do you want to draw another card? (y/n): ").lower()

        if choice == "y":
            user_cards.append(deal_cards())
            swap_cards(user_cards)

            if sum(user_cards) > 21:
                print(f"You went over 21. You lose! Your cards: {user_cards}")
                return
        else:
            break

    # Computer's turn — stays at 2 cards
    print(f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}")

    # Compare results
    if sum(user_cards) > sum(computer_cards):
        print("You win!")
    elif sum(user_cards) < sum(computer_cards):
        print("You lose!")
    else:
        print("It's a draw!")


# Start game
game()
