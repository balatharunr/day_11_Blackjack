import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(art.logo)
def sum_cards(hand):
    total = sum(hand)
    # Convert Ace from 11 to 1 if bust
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total
def eligibility(player, dealer):
    player_sum = sum_cards(player)
    dealer_sum = sum_cards(dealer)
    print(f"\nYour final hand: {player}, final score: {player_sum}")
    print(f"Computer's final hand: {dealer}, final score: {dealer_sum}")
    if player_sum > 21:
        print("You went over. Computer Wins!!")
    elif dealer_sum > 21:
        print("Computer went over. You Win!!")
    elif player_sum == dealer_sum:
        print("Draw")
    elif player_sum == 21:
        print("Blackjack! You Win!!")
    elif player_sum > dealer_sum:
        print("You Win!!")
    else:
        print("Computer Wins!!")
while True:
    your_cards = []
    dealer_cards = []
    choice = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if choice != 'y':
        break
    for i in range(2):
        your_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    game_over = False
    while not game_over:
        your_sum = sum_cards(your_cards)
        print(f"\nYour cards: {your_cards}, current score: {your_sum}")
        print(f"Computer's first card: {dealer_cards[0]}")
        if your_sum >= 21:
            game_over = True
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if hit == 'y':
                your_cards.append(random.choice(cards))
            else:
                game_over = True
    while sum_cards(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))
    eligibility(your_cards, dealer_cards)
