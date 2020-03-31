"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.

        Note that this works correctly for hands with more than 2 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_two_pair(self):
        """Returns True if the hand has two pairs, False otherwise.

        Note that this works correctly for hands with more than 2 cards.
        """
        self.rank_hist()
        count_pairs = 0
        for val in self.ranks.values():
            if val >= 2:
                count_pairs += 1
                if count_pairs >= 2:
                    return True
        return False

    def has_three_of_a_kind(self):
        """Returns True if the hand has three of a kind, False otherwise.

        Note that this works correctly for hands with more than 3 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        """Return True if the hand has a straight, False otherwise.

        Note that this works correctly for hands with more then 5 cards.
        """
        cards_rank = []
        for card in self.cards:
            cards_rank.append(card.rank)
        cards_rank = list(set(cards_rank))
        if cards_rank == []:  # used in check for straight flush
            return False
        cards_rank.sort()
        if cards_rank[0] == 1:  # add ace to the end of list
            cards_rank.append(14)
        max_card_in_seq = card_in_seq = 1
        for j in range(len(cards_rank)-1):
            if cards_rank[j]+1 == cards_rank[j+1]:
                card_in_seq += 1
                if card_in_seq > max_card_in_seq:
                    max_card_in_seq = card_in_seq
            else:
                card_in_seq = 1
        if max_card_in_seq >= 5:
            return True
        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_full_house(self):
        """Returns True if the hand has a full house, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        three_of_a_kind = False
        two_of_a_kind = False
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                three_of_a_kind = True
            else:
                if val >= 2:
                    two_of_a_kind = True
        if three_of_a_kind and two_of_a_kind:
            return True
        return False

    def has_four_of_a_kind(self):
        """Returns True if the hand has a four of a kind, False otherwise.

        Note that this works correctly for hands with more than 4 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_straight_flush(self):
        """Returns True if the hand has a straight flush, False otherwise.

        Note that this works correctly for hands with more than 4 cards.
        """
        clubs_hand = PokerHand()
        dimonds_hand = PokerHand()
        hearts_hand = PokerHand()
        spades_hand = PokerHand()
        self.cards.sort()
        for card in self.cards:
            if card.suit == 0:
                clubs_hand.add_card(card)
            if card.suit == 1:
                dimonds_hand.add_card(card)
            if card.suit == 2:
                hearts_hand.add_card(card)
            if card.suit == 3:
                spades_hand.add_card(card)
        if clubs_hand.has_straight():
            return True
        if dimonds_hand.has_straight():
            return True
        if hearts_hand.has_straight():
            return True
        if spades_hand.has_straight():
            return True
        return False

    def classify(self):
        """figures out the highest-value classification for a hand
           and sets the label attribute accordingly"""
        if self.has_pair():
            self.label = "Pair"
        if self.has_two_pair():
            self.label = "Two pair"
        if self.has_three_of_a_kind():
            self.label = "Three of a kind"
        if self.has_straight():
            self.label = "Straight"
        if self.has_flush():
            self.label = "Flush"
        if self.has_full_house():
            self.label = "Full house"
        if self.has_four_of_a_kind():
            self.label = "Four of a kind"
        if self.has_straight_flush():
            self.label = "Straight flush"
        return self.label


if __name__ == '__main__':

    HIST_OF_HANDS = {}

    def deal_hands():
        """Count the number of each classified hand"""
        # make a deck
        deck = Deck()
        deck.shuffle()

        # deal the cards and classify the hands
        for k in range(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            HIST_OF_HANDS[hand.classify()] = \
                HIST_OF_HANDS.get(hand.classify(), 0) + 1
            # print(hand)
            # print(hand.classify())
            # print('')
            # print('')

    for i in range(10):
        deal_hands()
    print(HIST_OF_HANDS)
