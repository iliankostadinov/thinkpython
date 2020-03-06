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






class Hand(Deck):
    """Represent a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label
