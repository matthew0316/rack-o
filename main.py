"""
Rack-O!
GamePlay:
1. Start of Game:
    Shuffle the "deck" ( stack of cards numbered 1 - 60 )
    User and Computer get 10 cards
2. As a player receives a card, they place it in the next available rack
3. The top card is turned over to start the discard pile
4. A player takes a turn by taking the top card from either the discard or the deck pile, the discarding on from his rack
and inserting the new card in its place.
5. The top card of the discard pile is always visible and therefore the player must choose whether or not to take the
top discard or not.
6. ONLY IF the player DOES NOT take the discard pile card can they select the one from the deck
7. The player may discard the card, however, doing so they must take the top discard, then put the card into his rack

FIRST PLAYER TO GET 10 CARDS IN ASCENDING ORDER CALLS 'RACK-O' AND WINS!

Goal:
To create a sequence of numbers in ascending order, starting at slot 1
"""
import sys
import random

totalNumCards = 18
rackSize = 6


def add_card_to_discard(card, discard):
    """
    :param card: card you wish to add to the discard pile
    :param discard: list of cards contained in "discard pile"
    :return: does not return anything
    """
    discard.append(card)


def find_and_replace(new_card, card_to_be_replaced, hand, discard):
    for i in range(len(hand)):
        if hand[i] == card_to_be_replaced:
            hand[i] = new_card
            discard.append(card_to_be_replaced)
        else:
            pass


def get_top_card(card_stack):
    """
    :param card_stack: list of cards
    :return: the top card from any stack of cards and removes it from the card_stack.
    Used at the start of the game for dealing cards, will also be used during each player's turn to remove the top card
    from either the discard pile or from the deck.
    """
    return card_stack.pop(-1)


def add_card_to_discard(card, discard):
    """
    :param card: card you wish to add to the discard pile
    :param discard: list of cards contained in "discard pile"
    :return: does not return anything
    """
    discard.append(card)


def find_and_replace(new_card, card_to_be_replaced, hand, discard):
    for i in range(len(hand)):
        if hand[i] == card_to_be_replaced:
            hand[i] = new_card
            discard.append(card_to_be_replaced)
        else:
            pass


def get_top_card(card_stack):
    """
    :param card_stack: list of cards
    :return: the top card from any stack of cards and removes it from the card_stack.
    Used at the start of the game for dealing cards, will also be used during each player's turn to remove the top card
    from either the discard pile or from the deck.
    """
    return card_stack.pop(-1)


def shuffle(card_stack):
    """
    :param card_stack: list of card numbers
    :return: returns nothing
    """
    random.shuffle(card_stack)


def deal_initial_hands(deck):
    """
    :param deck: the deck of cards
    :return: two lists - one representing the user's hand. the other representing the CPU's hand in tuple form
    function dealing the top card from the deck to the CPU then to the user then to the CPU and repeat until the number
    of cards in each of the hands is equal to rackSize.
    """
    cpuHand = []
    userHand = []

    for i in range(rackSize * 2):
        if i % 2 == 0 and len(cpuHand) != rackSize:
            cpuHand.append(get_top_card(deck))
        elif i % 2 != 0 and len(userHand) != rackSize:
            userHand.append(get_top_card(deck))

    return cpuHand, userHand


def check_racko(hand):
    """
    :param hand: player or CPU hand / rack
    :return: True if Rack-O, False if no Rack-O
    Rack-O means that the cards are in ascending order, i.e. 1,2,3
    """
    if hand == sorted(hand):
        return True
    else:
        return False


def replaceDeck(card_stack):
    """
    :param card_stack: stack of cards
    :return: two lists - the new deck and the new discard pile - in tuple form
    should only pass the discard pile as a parameter since the deck will be empty
    function: pass the discard pile, shuffle the discard pile, and that shuffled pile becomes the new deck
    """
    shuffle(card_stack)
    newDeck = card_stack
    newDiscard = [get_top_card(newDeck)]

    return newDeck, newDiscard


def computer_play(computer_hand, deck, discard):
    """
    :param computer_hand: the computers rack
    :param deck: the game deck
    :param discard: the discard pile
    :return: nothing to return
    """

    if check_racko(computer_hand):
        print('COMPUTER WINS! with hand of {}'.format(computer_hand))
        sys.exit()

    # Print lists corresponding to deck, discard pile, and computer's current hand
    print('deck: \n{}'.format(deck))
    print('discard pile: \n{}'.format(discard))
    print()
    print('Computer Current Hand: \n{}'.format(computer_hand))

    # top discard card
    top_discard_card = discard[-1]
    top_deck_card = deck[-1]

    for i in range(len(computer_hand)):

        if i == len(computer_hand) - 1:
            if top_discard_card > computer_hand[i-1] and top_discard_card > computer_hand[i]:
                print('Computer: Chooses top discard card {}'.format(top_discard_card))
                print('Computer: Replaces it with {}'.format(computer_hand[i]))
                top_discard_card = get_top_card(discard)
                find_and_replace(top_discard_card, computer_hand[i], computer_hand, discard)
                print("Computer's new hand: \n{}".format(computer_hand))
                break
            elif top_deck_card > computer_hand[i-1] and top_deck_card > computer_hand[i]:
                print('Computer: Chooses top deck card {}'.format(top_deck_card))
                print('Computer: Replaces it with {}'.format(computer_hand[i]))
                find_and_replace(get_top_card(deck), computer_hand[i], computer_hand, discard)
                print("Computer's new hand: \n{}".format(computer_hand))
                break
            else:
                print('Computer is passing its turn')
                break

        if computer_hand[i] < computer_hand[i+1]:
            pass
        else:
            if i == 0:
                if top_deck_card < computer_hand[i] and top_deck_card < top_discard_card:
                    print('Computer: Chooses top deck card {}'.format(top_deck_card))
                    print('Computer: Replaces it with {}'.format(computer_hand[i]))
                    find_and_replace(get_top_card(deck), computer_hand[i], computer_hand, discard)
                    print("Computer's new hand: \n{}".format(computer_hand))
                    break
                elif top_discard_card < computer_hand[i] and top_discard_card < top_deck_card:
                    print('Computer: Chooses top discard card: {}'.format(discard[-1]))
                    print('Computer: Replacing it with: {}'.format(computer_hand[i]))
                    find_and_replace(get_top_card(discard), computer_hand[i], computer_hand, discard)
                    print("Computer's new hand: \n{}".format(computer_hand))
                    break
            elif computer_hand[i + 1] > top_discard_card > computer_hand[i - 1]:
                if top_discard_card < top_deck_card:
                    print('Computer: Chooses top discard card: {}'.format(discard[-1]))
                    print('Computer: Replacing it with: {}'.format(computer_hand[i]))
                    find_and_replace(get_top_card(discard), computer_hand[i], computer_hand, discard)
                    print("Computer's new hand: \n{}".format(computer_hand))
                    break
                else:
                    pass
            elif computer_hand[i + 1] > top_deck_card > computer_hand[i - 1]:
                if top_deck_card < top_discard_card:
                    print('Computer: Chooses top deck card: {}'.format(deck[-1]))
                    print('Computer: Replacing it with: {}'.format(computer_hand[i]))
                    find_and_replace(get_top_card(deck), computer_hand[i], computer_hand, discard)
                    print("Computer's new hand: \n{}".format(computer_hand))
                    break
                else:
                    pass
            elif computer_hand[i + 1] < computer_hand[i] and computer_hand[i + 1] < top_discard_card < computer_hand[-1]:
                print('Computer: Chooses top discard card: {}'.format(discard[-1]))
                print('Computer: Replacing it with: {}'.format(computer_hand[i+1]))
                find_and_replace(get_top_card(discard), computer_hand[i+1], computer_hand, discard)
                print("Computer's new hand: \n{}".format(computer_hand))
                break
            elif computer_hand[i + 1] < computer_hand[i] and computer_hand[i + 1] < top_deck_card < computer_hand[-1]:
                print('Computer: Chooses top deck card: {}'.format(deck[-1]))
                print('Computer: Replacing it with: {}'.format(computer_hand[i+1]))
                find_and_replace(get_top_card(deck), computer_hand[i+1], computer_hand, discard)
                print("Computer's new hand: \n{}".format(computer_hand))
                break
            elif computer_hand[i] > computer_hand[i + 1] > top_discard_card and computer_hand[i] > top_discard_card:
                print('Computer: Chooses top discard card: {}'.format(discard[-1]))
                print('Computer: Replacing it with: {}'.format(computer_hand[i]))
                find_and_replace(get_top_card(discard), computer_hand[i], computer_hand, discard)
                print("Computer's new hand: \n{}".format(computer_hand))
                break
            elif computer_hand[i] > computer_hand[i + 1] > top_deck_card and computer_hand[i] > top_deck_card:
                print('Computer: Chooses top deck card: {}'.format(deck[-1]))
                print('Computer: Replacing it with: {}'.format(computer_hand[i]))
                find_and_replace(get_top_card(deck), computer_hand[i], computer_hand, discard)
                print("Computer's new hand: \n{}".format(computer_hand))
                break

    print()


def human_play(userHand, deck, discard):
    # print game info
    print('deck: \n{}'.format(deck))
    print('discard pile: \n{}'.format(discard))
    print()
    print('Your current hand: \n{}'.format(userHand))

    if check_racko(userHand):
        print('HUMAN WINS! with hand of {}'.format(userHand))
        sys.exit()

    # discard choice
    top_card_discard_choice = input(
        'Do you want this discard card: {}\nEnter yes or no: '.format(discard[-1])).lower()

    if top_card_discard_choice == 'y' or top_card_discard_choice == 'yes':
        # Ask for the card they wish the kick out
        card_to_kick_out = int(input('Enter the number of the card you want to kick out: '))
        # Modify the user's hand and the discard pile
        find_and_replace(get_top_card(discard), card_to_kick_out, userHand, discard)
        # Print the user's hand
        print("Your new hand is: \n{}".format(userHand))
        print()

        if check_racko(userHand):
            print('HUMAN WINS! with hand of {}'.format(userHand))
            sys.exit()

    elif top_card_discard_choice == 'n' or top_card_discard_choice == 'no':
        # Get the top card from the deck and show the user
        print('The card you get from the deck is {}'.format(deck[-1]))
        top_card_deck_choice = input('Do you want to keep this card? Enter yes or no: ').lower()
        if top_card_deck_choice == 'y' or top_card_deck_choice == 'yes':
            card_to_kick_out = int(input('Enter the number of the card you want to kick out: '))
            find_and_replace(get_top_card(deck), card_to_kick_out, userHand, discard)
            print("Your new hand is: \n{}".format(userHand))
            print()
            if check_racko(userHand):
                print('HUMAN WINS! with hand of {}'.format(userHand))
                sys.exit()
        else:
            topDeckCard = get_top_card(deck)
            add_card_to_discard(topDeckCard, discard)
            print("Your new hand is: \n{}".format(userHand))
            print()
    else:
        print('Choice can only be yes or no')
        sys.exit()


def main():
    # Create a list of numbers from 1 to numOfCards || "the deck"
    deck = [i for i in range(1, totalNumCards + 1)]
    shuffle(deck)  # the deck: shuffled

    # creating cpu and human racks
    cpuHand, userHand = deal_initial_hands(deck)

    # create an empty discard pile
    discardPile = [get_top_card(deck)]

    # take top card from deck, add it to discard pile

    while check_racko(cpuHand) == False or check_racko(userHand) == False:
        human_play(userHand, deck, discardPile)
        if len(deck) == 0:
            print('\nUser: WOAH! Deck is empty. Shuffling discard pile and using that as the new deck.\n')
            deck, discardPile = replaceDeck(discardPile)

        computer_play(cpuHand, deck, discardPile)

        if len(deck) == 0:
            print('\nComputer: WOAH! Deck is empty. Shuffling discard pile and using that as the new deck.\n')
            deck, discardPile = replaceDeck(discardPile)

        if check_racko(cpuHand):
            print('COMPUTER WINS! with hand of {}'.format(cpuHand))
            break


if __name__ == '__main__':
    main()

