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
        self.ranking = {
                    'straight_flush': False,
                    'flush': False,
                    'straight': False,
                    'double_pair': False,
                    'single_pair': False,
                    'card': False
                    }

        self.hand_dict = self.parse_input(hand) # The parsed input
        self.sorted_high_to_low = self.sort_high_to_low() # Sort the card numbers from high to low
        
        # Find the highest rank
        self.ranking['double_pair'] = self.check_is_double_pair()
        if not self.ranking['double_pair']:
            self.ranking['single_pair'] = self.check_is_single_pair()
            
            if not self.ranking['single_pair']: 
                self.ranking['flush'] = self.check_is_flush()
                self.ranking['straight'] = self.check_is_straight()

                if self.ranking['straight'] and self.ranking['flush']:
                    self.ranking['straight_flush'] = True
                    self.ranking['straight'] = False
                    self.ranking['flush'] = False

                        
    def __repr__(self):
        return(f"""
              ranking = {self.ranking}
              sorted_high_to_low = {self.sorted_high_to_low}
              """)

        
    def parse_input(self, hand):
        JQKA = {'J': 11 ,'Q': 12 ,'K': 13, 'A': 14}
        
        hand_dict = {}
        
        for card in hand:
            cardArr = card.split()
            #check if card if j,q,or k
            if cardArr[0] in JQKA.keys():
                cardArr[0] = JQKA[cardArr[0]]
            if int(cardArr[0]) in hand_dict:
                hand_dict[int(cardArr[0])].append(cardArr[1])
            else:
                hand_dict[int(cardArr[0])]= [cardArr[1]]
                
        return hand_dict

    def check_is_straight(self):
        straight = True
        print('checking straight', self.sorted_high_to_low)
        
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
        # Not flush if dict only has < 5 keys; each key is a unique card number
        if len(self.hand_dict.keys()) < 5:
            return False
        values = list(self.hand_dict.values())
        
        first_suit = values[0][0]
        return (all(suit[0] == first_suit for suit in values))

    def check_is_double_pair(self):
        #check if there are only 3 keys
        return len(self.sorted_high_to_low) == 3

    def check_is_single_pair(self):
        #check if there are only 4 keys
        return len(self.sorted_high_to_low) == 4
    
    def sort_high_to_low(self):
        nums = [k for k in self.hand_dict.keys()]
        nums.sort(reverse=True)
        
        return nums

def compare_hands(hand1, hand2):
    """Compare 2 hands
    Ignoring 5 of a kind (no wild cards), so the highest hand is a straight flush
    Suits don't matter except in a flush or straight flush
    
    hand1, hand2 follows the format: ["J spade", "J heart", "9 spade", "2 diamond", "3 club"]
    
    #break up into dict
    
    {
        J: [heart, spade],
        9: [spade],
        2: [diamond],
        3: [club]
    }
    also at the same time when parsing see if it is a flush
    """

    hand1_obj = Hand(hand1)
    hand2_obj = Hand(hand2)
    print(hand1_obj, hand2_obj)
  
    tie = False
    #compare both hands
    if hand1_obj.ranking != hand2_obj.ranking:
        print('in here')
        #compare 2 lists and see which one has true first
        hand1_ranks=[a for a in hand1_obj.ranking.values()]
        hand2_ranks=[b for b in hand2_obj.ranking.values()]
        print(hand1_ranks, hand2_ranks)
        
        if True in hand1_ranks and True in hand2_ranks:
            if hand1_ranks.index(True) > hand2_ranks.index(True):
                return "hand2"
            elif hand1_ranks.index(True) < hand2_ranks.index(True):
                return "hand1"
            else:
                tie = True
        else:
            if True in hand1_ranks:
                return "hand1"
            elif True in hand2_ranks:
                return "hand2"
            else:
                tie = True
        

    if hand1_obj.ranking == hand2_obj.ranking or tie:
        print('both are the same')
        for hand1_num, hand2_num in zip(hand1_obj.sorted_high_to_low, hand2_obj.sorted_high_to_low):
            print(hand1_num, hand2_num)
            if hand1_num > hand2_num:
                return 'hand1'
            elif hand2_num > hand1_num:
                return 'hand2'
    
        return "tie"
  
        
        
    
    
    
#flush
# hand1=["10 club", "J club", "Q club", "K club", "3 club"]
#straight flush
#hand1=["A club", "K club", "Q club", "10 club", "J club"]
# #straight
# hand1=["10 spade", "J club", "Q club", "K club", "A club"]
# #straight other way
# hand1=["2 spade", "4 club", "3 club", "A club", "5 club"]
# #double pair
#hand1=["10 spade", "10 club", "Q club", "Q diamond", "A club"]
# #single pair
#hand1=["10 spade", "10 club", "K club", "6 diamond", "A heart"]
# #high card
# hand1=["4 spade", "J heart", "9 spade", "2 diamond", "3 club"]
# hand2=["4 spade", "J heart", "9 spade", "2 diamond", "3 club"]


hand1=["10 club", "J club", "Q club", "K club", "A club"]
hand2=["K club", "J club", "9 club", "2 club", "3 club"]
winner = compare_hands(hand1, hand2)
print ('winner is....', winner, '!')
"""
errors: check that each hand is 5 elements long
elements are from 2-10, JQKA (A can be high or low)
- less than 5 keys in dict (repeated num)
- need to add A as 1 code
- 
"""

    