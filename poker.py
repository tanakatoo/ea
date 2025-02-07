class Hand:
    """
    Class to encapsulate poker hand variables and functions
    """
    def __init__(self, hand):
        """
        Take a poker hand and calcualte its highest rank

        Args:
            hand (list): list of 5 cards in the form of "<Card number> <suit>" e.g. "J spade"
        """
        # Ranking in order from strongest to weakest
        self.ranking = {
                    'straight_flush': False,
                    'four_of_a_kind': False,
                    'full_house': False,
                    'flush': False,
                    'straight': False,
                    'three_of_a_kind': False,
                    'double_pair': False,
                    'single_pair': False
                    }

        self.hand_dict = self.parse_input(hand) # The parsed input
        self.sorted_high_to_low = self.sort_high_to_low() # Sort the card numbers from high to low
        
        self.ranking['double_pair'] = self.check_is_double_pair()
        self.ranking['full_house'] = self.check_is_full_house()
        self.ranking['three_of_a_kind'] = self.check_is_three_of_a_kind()
        self.ranking['four_of_a_kind'] = self.check_is_four_of_a_kind()
        self.ranking['single_pair'] = self.check_is_single_pair()
        self.ranking['flush'] = self.check_is_flush()
        self.ranking['straight'] = self.check_is_straight()

        if self.ranking['straight'] and self.ranking['flush']:
            self.ranking['straight_flush'] = True
                        
    def __repr__(self):
        return(f"""
              ranking = {self.ranking}
              sorted_high_to_low = {self.sorted_high_to_low}
              """)

        
    def parse_input(self, hand):
        """
        Parses input into a dict. 
        Changes all input into an int and JQKA becomes 11, 12, 13, 14

        Args:
            hand (list): poker hand input from user

        Returns:
            dict: 
                {
                    <num>: [<suit>,<suit>,...]
                }
        """
        JQKA = {'J': 11 ,'Q': 12 ,'K': 13, 'A': 14}
        
        hand_dict = {}
        for card in hand:
            cardArr = card.split()
            
            if cardArr[0] in JQKA.keys():
                cardArr[0] = JQKA[cardArr[0]]
                
            if int(cardArr[0]) in hand_dict:
                hand_dict[int(cardArr[0])].append(cardArr[1])
                
            else:
                hand_dict[int(cardArr[0])]= [cardArr[1]]
                
        return hand_dict

    def sort_high_to_low(self):
        """
        Sorts the hand into a list from high to low numbers

        Returns:
           list: integers representing the hand from high to low
        """
        nums = [k for k in self.hand_dict.keys()]
        nums.sort(reverse=True)
        return nums

    def check_is_straight(self):
        """
        Checks to see if hand is a straight

        Returns:
            Boolean: whether or not the hand is a straight
        """
        if len(self.sorted_high_to_low) < 5:
            return False 
    
        straight = True
        
        for i in range(0,len(self.sorted_high_to_low)-1):
            if not(self.sorted_high_to_low[i] - self.sorted_high_to_low[i+1] == 1):
                straight = False
                
        if straight == False and 14 in self.sorted_high_to_low:
            # check that it is not 12345
            self.sorted_high_to_low = self.sorted_high_to_low[1:]
            self.sorted_high_to_low.append(1)
            
            for i in range(0,len(self.sorted_high_to_low)-1):
                if not(self.sorted_high_to_low[i] - self.sorted_high_to_low[i+1] == 1):
                    straight = False
        
        return straight
        
    def check_is_flush(self):
        """
        Checks to see if hand is a flush. 

        Returns:
            Boolean: whether or not the hand is a flush
        """
        if len(self.hand_dict.keys()) < 5:
            return False
        values = list(self.hand_dict.values())
        
        first_suit = values[0][0]
        return (all(suit[0] == first_suit for suit in values))
    
    def check_is_four_of_a_kind(self):
        """
        Checks to see if hand is a 4 of a kind. 

        Returns:
            Boolean: whether or not the hand is a 4 of a kind
        """
        return len(self.hand_dict) == 2 and any(len(arr) == 4 for arr in self.hand_dict.values())
    
    def check_is_full_house(self):
        """
        Checks to see if hand is a full house

        Returns:
            Boolean: whether or not the hand is a full house
        """
        return len(self.sorted_high_to_low) == 2 and any(len(arr) == 3 for arr in self.hand_dict.values())
    
    def check_is_three_of_a_kind(self):
        """
        Checks to see if hand has a 3 of a kind

        Returns:
            Boolean: whether or not the hand has a 3 of a kind
        """
        return len(self.hand_dict) == 3 and any(len(arr) == 3 for arr in self.hand_dict.values())

    def check_is_double_pair(self):
        """
        Checks to see if hand has 2 pairs

        Returns:
            Boolean: whether or not the hand has 2 pairs
        """
        return len(self.sorted_high_to_low) == 3 and not any(len(arr) == 3 for arr in self.hand_dict.values())

    def check_is_single_pair(self):
        """
        Checks to see if hand has 1 pair

        Returns:
            Boolean: whether or not the hand has 1 pair
        """
        return len(self.sorted_high_to_low) == 4

def compare_hands(hand1, hand2):
    """
    Compare 2 poker hands
    Ignoring 5 of a kind (no wild cards), so the highest hand is a straight flush
    Suits don't matter except in a flush or straight flush
    
    Assume that hand1 and hand2 have been checked and formated to this format: 
    ["J spade", "J heart", "9 spade", "2 diamond", "3 club"]
    
    Args: 
    hand1: One hand of poker
    hand2: The other hand of poker to compare
    
    """
    hand1_obj = Hand(hand1)
    hand2_obj = Hand(hand2)
    tie = False
    
    def determine_winner_3_4_of_a_kind(len_of_repeat):
        hand1_x_of_a_kind_num = [key for key, value in hand1_obj.hand_dict.items() if len(value) == len_of_repeat]
        hand2_x_of_a_kind_num = [key for key, value in hand2_obj.hand_dict.items() if len(value) == len_of_repeat]
        
        if hand1_x_of_a_kind_num[0] > hand2_x_of_a_kind_num[0]:
            return "hand1"
        elif hand1_x_of_a_kind_num[0] < hand2_x_of_a_kind_num[0]:
            return "hand2"
   
    def determine_winner_double_pair_single_card(len_of_repeat):
        hand1_double_pair_nums = [key for key, value in hand1_obj.hand_dict.items() if len(value) == len_of_repeat]
        hand2_double_pair_nums = [key for key, value in hand2_obj.hand_dict.items() if len(value) == len_of_repeat]
        hand1_double_pair_nums.sort(reverse=True)
        hand2_double_pair_nums.sort(reverse=True)
        
        for hand1_num, hand2_num in zip(hand1_double_pair_nums, hand2_double_pair_nums):
            if hand1_num > hand2_num:
                return 'hand1'
            elif hand2_num > hand1_num:
                return 'hand2'

    if hand1_obj.ranking != hand2_obj.ranking:
        # Compare the 2 rankings. Strong hand will have True first
        hand1_ranks=list(hand1_obj.ranking.values())
        hand2_ranks=list(hand2_obj.ranking.values())

        for val1, val2 in zip(hand1_ranks, hand2_ranks):
            if val1 and not val2:
                return "hand1"
            elif val2 and not val1:
                return "hand2"
            else:
                tie = True  

    if hand1_obj.ranking == hand2_obj.ranking or tie:
        if hand1_obj.ranking['four_of_a_kind']:
            return determine_winner_3_4_of_a_kind(4)
            
        if hand1_obj.ranking['three_of_a_kind'] or hand1_obj.ranking['full_house']:
            return determine_winner_3_4_of_a_kind(3)
            
        if hand1_obj.ranking['double_pair']:
            result = determine_winner_double_pair_single_card(2)
            if result in ['hand1', 'hand2']:
                return result
                
        result = determine_winner_double_pair_single_card(1)
        if result in ['hand1', 'hand2']:
            return result
        else:
            return "tie"

    