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


class TestFourOfAKind:
    @pytest.mark.parametrize(
        "hand1, hand2, expected_winner",
        [
            (["3 heart", "3 diamond", "3 spade", "3 club", "8 heart"], 
             ["2 diamond", "2 club", "2 spade", "2 heart", "J diamond"], 
             "hand1")
        ],
        ids=[
            "Higher four of a kind wins"
        ]
    )
    def test_full_house(self, hand1, hand2, expected_winner):
        winner = compare_hands(hand1, hand2)
        assert expected_winner == winner

class TestFullHouse:
    @pytest.mark.parametrize(
        "hand1, hand2, expected_winner",
        [
            (["3 heart", "3 diamond", "3 spade", "8 club", "8 heart"], 
             ["2 diamond", "2 club", "2 spade", "J heart", "J diamond"], 
             "hand1")
        ],
        ids=[
            "Higher full house wins"
        ]
    )
    def test_full_house(self, hand1, hand2, expected_winner):
        winner = compare_hands(hand1, hand2)
        assert expected_winner == winner

class TestThreeOfAKind:
    @pytest.mark.parametrize(
        "hand1, hand2, expected_winner",
        [
            (["3 heart", "3 diamond", "3 spade", "8 club", "10 heart"],
             ["2 diamond", "2 club", "2 spade", "J heart", "K diamond"],
             "hand1"),
        ],
        ids=[
            "Higher three of a kind wins"
        ]
    )
    def test_three_of_a_kind(self, hand1, hand2, expected_winner):
        winner = compare_hands(hand1, hand2)
        assert expected_winner == winner

class TestDoublePairs:
    @pytest.mark.parametrize(
        "hand1, hand2, expected_winner",
        [
            (["10 spade", "10 club", "9 club", "9 diamond", "A heart"],
             ["8 spade", "8 heart", "7 spade", "7 diamond", "3 club"],
             "hand1"),

            (["10 spade", "10 club", "6 club", "6 diamond", "A heart"],
             ["9 spade", "9 heart", "7 spade", "7 diamond", "3 club"],
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
            
            (["J spade", "J heart", "9 spade", "2 diamond", "3 club"],
             ["J diamond", "J club", "9 club", "5 diamond", "A club"],
             "hand2"),
            
            (["10 spade", "10 club", "K club", "Q diamond", "A club"],
             ["10 diamond", "10 heart", "K spade", "Q spade", "A diamond"],
             "tie"),
        ],
        ids=[
            "Higher pair beats lower pair",
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
        

class TestDifferentRankings:
    FOUR_OF_A_KIND = ["3 heart", "3 diamond", "3 spade", "3 club", "8 heart"]
    THREE_OF_A_KIND =  ["2 diamond", "2 club", "2 spade", "J heart", "K diamond"]
    FULL_HOUSE = ["3 heart", "3 diamond", "3 spade", "8 club", "8 heart"]
    DOUBLE_PAIR = ["10 spade", "10 club", "Q club", "Q diamond", "2 club"]
    SINGLE_PAIR = ["10 spade", "10 club", "2 club", "3 diamond", "4 club"]
    HIGH_CARD = ["2 diamond", "4 spade", "6 heart", "8 club", "A diamond"]
    FLUSH = ["2 heart", "3 heart", "4 heart", "10 heart", "6 heart"]
    STRAIGHT_FLUSH = ["2 heart", "3 heart", "4 heart", "5 heart", "6 heart"]
    STRAIGHT = ["2 heart", "3 diamond", "4 heart", "5 heart", "6 heart"]

    @pytest.mark.parametrize(
        "hand1, hand2, expected_winner",
        [
            (SINGLE_PAIR, HIGH_CARD, "hand1"),
            (DOUBLE_PAIR, SINGLE_PAIR, "hand1"),
            (DOUBLE_PAIR, HIGH_CARD, "hand1"),
            (THREE_OF_A_KIND, FULL_HOUSE, "hand2"),
            (DOUBLE_PAIR, FULL_HOUSE, "hand2"),
            (SINGLE_PAIR, FULL_HOUSE, "hand2"),
            (HIGH_CARD, FULL_HOUSE, "hand2"),
            (FLUSH, FULL_HOUSE, "hand2"),
            (STRAIGHT, FULL_HOUSE, "hand2"),
            (THREE_OF_A_KIND, DOUBLE_PAIR, "hand1"),
            (THREE_OF_A_KIND, SINGLE_PAIR, "hand1"),
            (THREE_OF_A_KIND, HIGH_CARD, "hand1"),
            (FOUR_OF_A_KIND, THREE_OF_A_KIND, "hand1"),
            (FOUR_OF_A_KIND, FULL_HOUSE, "hand1"),
            (FOUR_OF_A_KIND, DOUBLE_PAIR, "hand1"),
            (FOUR_OF_A_KIND, SINGLE_PAIR, "hand1"),
            (FOUR_OF_A_KIND, HIGH_CARD, "hand1"),
            (FOUR_OF_A_KIND, FLUSH, "hand1"),
            (FOUR_OF_A_KIND, STRAIGHT, "hand1"),
            (STRAIGHT, FLUSH, "hand2"),
            (THREE_OF_A_KIND, FLUSH, "hand2"),
            (DOUBLE_PAIR, FLUSH, "hand2"),
            (SINGLE_PAIR, FLUSH, "hand2"),
            (HIGH_CARD, FLUSH, "hand2"),
            (STRAIGHT, THREE_OF_A_KIND, "hand1"),
            (STRAIGHT, DOUBLE_PAIR, "hand1"),
            (STRAIGHT, SINGLE_PAIR, "hand1"),
            (STRAIGHT, HIGH_CARD, "hand1"),
            (STRAIGHT_FLUSH, FOUR_OF_A_KIND, "hand1"),
            (STRAIGHT_FLUSH, THREE_OF_A_KIND, "hand1"),
            (STRAIGHT_FLUSH, FULL_HOUSE, "hand1"),
            (STRAIGHT_FLUSH, DOUBLE_PAIR, "hand1"),
            (STRAIGHT_FLUSH, SINGLE_PAIR, "hand1"),
            (STRAIGHT_FLUSH, HIGH_CARD, "hand1"),
            (STRAIGHT_FLUSH, FLUSH, "hand1"),
            (STRAIGHT_FLUSH, STRAIGHT, "hand1"),
        ],
        ids=[
            "Single pair beats high card",
            "Double pair beats single pair",
            "Double pair beats high card",
            "Full house beats 3 of a kind",
            "Full house beats double pair",
            "Full house beats single pair",
            "Full house beats high card",
            "Full house beats flush",
            "Full house beats straight",
            "Three of a kind beats double pair",
            "Three of a kind beats single pair",
            "Three of a kind beats high card",
            "Four of a kind beats 3 of a kind",
            "Four of a kind beats full house",
            "Four of a kind beats double pair",
            "Four of a kind beats single pair",
            "Four of a kind beats high card",
            "Four of a kind beats flush",
            "Four of a kind beats straight",
            "Flush beats straight",
            "Flush beats 3 of a kind",
            "Flush beats double pair",
            "Flush beats single pair",
            "Flush beats high card",
            "Straight beats 3 of a kind",
            "Straight beats double pair",
            "Straight beats single pair",
            "Straight beats high card",
            "Straight flush beats 4 of a kind",
            "Straight flush beats 3 of a kind",
            "Straight flush beats full house",
            "Straight flush beats double pair",
            "Straight flush beats single pair",
            "Straight flush beats high card",
            "Straight flush beats flush",
            "Straight flush beats straight",
        ]
    )
    
    def test_different_rankings(self, hand1, hand2, expected_winner):
        winner = compare_hands(hand1, hand2)
        assert expected_winner == winner