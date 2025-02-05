import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from poker import Hand, compare_hands

class TestStraightFlush:
    @pytest.mark.parametrize(
        "hand1, hand2, expected_winner",
        [
            (["10 club", "J club", "Q club", "K club", "A club"],
             ["K club", "J club", "9 club", "2 club", "3 club"],
             "hand1"),

            (["2 heart", "3 heart", "4 heart", "5 heart", "6 heart"],
             ["3 diamond", "4 diamond", "5 diamond", "6 diamond", "7 diamond"],
             "hand2"),
            
            (["K heart", "J heart", "9 heart", "2 heart", "3 heart"],
             ["K club", "J club", "9 club", "2 club", "3 club"],
             "tie"),
        ],
        ids=[
            "Straight flush beats flush",
            "Higher straight flush beats lower straight flush",
            "Tie"
        ]
    )
    def test_straight_flush(self, hand1, hand2, expected_winner):
        winner = compare_hands(hand1, hand2)
        assert expected_winner == winner

class TestFlush:
    @pytest.mark.parametrize(
        "hand1, hand2, expected_winner",
        [
            (["2 heart", "4 heart", "6 heart", "8 heart", "10 heart"],
             ["3 diamond", "5 diamond", "7 diamond", "9 diamond", "J diamond"],
             "hand2"),  # Higher flush wins

            (["A spade", "K spade", "Q spade", "J spade", "9 spade"],
             ["A club", "K club", "Q club", "J club", "8 club"],
             "hand1"),  # Highest card in flush determines the winner

            (["2 diamond", "4 diamond", "6 diamond", "8 heart", "10 diamond"],
             ["2 club", "4 club", "6 spade", "8 club", "10 club"],
             "tie"),  # Identical flushes in different suits result in a tie
        ],
        ids=[
            "Higher flush wins",
            "Higher card beats lower card",
            "Tie"
        ]
    )
    def test_flush(self, hand1, hand2, expected_winner):
        winner = compare_hands(hand1, hand2)
        assert expected_winner == winner


class TestStraight:
    @pytest.mark.parametrize(
        "hand1, hand2, expected_winner",
        [
            (["A heart", "3 club", "4 diamond", "5 spade", "2 heart"],
             ["3 diamond", "4 spade", "5 club", "6 diamond", "7 heart"],
             "hand2"),  

            (["10 heart", "A diamond", "Q spade", "K club", "J heart"],
             ["9 club", "10 diamond", "J heart", "Q spade", "K diamond"],
             "hand1"),  

            (["A spade", "2 club", "3 heart", "4 diamond", "5 spade"],
             ["A heart", "2 diamond", "3 spade", "4 club", "5 heart"],
             "tie"), 
        ],
        ids=[
            "Higher straight wins",
            "Ace-high straight beats King-high straight",
            "Tie"
        ]
    )
    def test_straight(self, hand1, hand2, expected_winner):
        winner = compare_hands(hand1, hand2)
        assert expected_winner == winner

class TestDoublePairs:
    @pytest.mark.parametrize(
        "hand1, hand2, expected_winner",
        [
            (["10 spade", "10 club", "9 club", "9 diamond", "A heart"],
             ["8 spade", "8 heart", "7 spade", "7 diamond", "3 club"],
             "hand1"),

            (["10 spade", "10 club", "9 club", "9 diamond", "A heart"],
             ["9 spade", "9 heart", "7 spade", "7 diamond", "3 club"],
             "hand1"),

            (["10 spade", "10 club", "Q club", "Q diamond", "A club"],
             ["J spade", "J heart", "9 spade", "2 diamond", "3 club"],
             "hand1"),
            
            (["J spade", "J heart", "9 spade", "2 diamond", "3 club"],
             ["10 spade", "10 club", "Q club", "Q diamond", "A club"],
             "hand2"),
            
            (["10 spade", "10 club", "Q club", "Q diamond", "A club"],
             ["10 diamond", "10 heart", "Q spade", "Q diamond", "A diamond"],
             "tie"),
        ],
        ids=[
            "2 higher pairs beat 2 lower pairs",
            "1 higher pair beat 2 lower pairs",
            "2 pairs beat 1 pair",
            "Higher kicker beats lower kicker",
            "Tie"
        ]
    )
    def test_double_pairs(self, hand1, hand2, expected_winner):
        winner = compare_hands(hand1, hand2)
        assert expected_winner == winner


class TestSinglePair:
    @pytest.mark.parametrize(
        "hand1, hand2, expected_winner",
        [
            (["10 spade", "10 club", "8 club", "9 diamond", "A heart"],
             ["8 spade", "8 heart", "6 spade", "7 diamond", "3 club"],
             "hand1"),

            (["K spade", "10 club", "A heart", "Q diamond", "2 club"],
             ["J spade", "J heart", "9 spade", "2 diamond", "3 club"],
             "hand2"),
            
            (["J spade", "J heart", "9 spade", "2 diamond", "3 club"],
             ["J spade", "J club", "9 club", "5 diamond", "A club"],
             "hand2"),
            
            (["10 spade", "10 club", "K club", "Q diamond", "A club"],
             ["10 diamond", "10 heart", "K spade", "Q diamond", "A diamond"],
             "tie"),
        ],
        ids=[
            "Higher pair beats lower pair",
            "Single pair beats no pair",
            "Higher kicker beats lower kicker",
            "Tie"
        ]
    )
    def test_single_pair(self, hand1, hand2, expected_winner):
        winner = compare_hands(hand1, hand2)
        assert expected_winner == winner

class TestHighCard:
    @pytest.mark.parametrize(
        "hand1, hand2, expected_winner",
        [
            (["2 diamond", "4 spade", "6 heart", "8 club", "J diamond"],
             ["2 diamond", "4 spade", "6 heart", "8 club", "10 diamond"],
             "hand1"),
            
            (["2 diamond", "4 spade", "6 heart", "8 club", "10 diamond"],
             ["2 diamond", "4 spade", "6 heart", "8 club", "10 diamond"],
             "tie"),
        ],
        ids=[
            "Higher card beats lower card",
            "Tie"
        ]
    )
    def test_high_card(self, hand1, hand2, expected_winner):
        winner = compare_hands(hand1, hand2)
        assert expected_winner == winner