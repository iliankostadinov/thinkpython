#!/usr/bin/env python3
"""Represent a card game"""

import random


class Card(object):
    """Represent standard playing card."""

    suit_names = ['Clubs', 'Dimonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Return a human readable representation"""
        return '%s of %s' % \
            (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit:
            return True

        if self.suit > other.suit:
            return False

        # suits are the same ... check ranks
        return self.suit < self.rank


class Deck(object):
    """Represent a standard 52 cards deck"""

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        """Remove card from deck"""
        return self.cards.pop()

    def add_card(self, card):
        """Add card to deck"""
        self.cards.append(card)

    def shuffle(self):
        """Shuffle a deck"""
        random.shuffle(self.cards)

    def sort(self):
        """Sort cards in deck"""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Modifies both self and hand

        hand: Hand object
        num: number of cards to deal
        """
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_hands, num_cards):
        """Create appropriate number of Hand objects,
        deal apropriate number of cards per hand,
        and return list of Hands.

        num_hands: number of hands
        num_cards: number of cards per hand
        """
        list_of_hands = []
        for i in range(num_hands):
            new_hand = Hand()
            self.move_cards(new_hand, num_cards)
            list_of_hands.append(new_hand)

        return list_of_hands


class Hand(Deck):
    """Represent a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 5)
    hand.sort()
    print(hand)
    dealed = deck.deal_hands(4, 3)
    for i in dealed:
        print(i)
