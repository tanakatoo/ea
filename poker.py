class Hand:
    is_straight_flush = False
    is_flush = False
    is_straight = True
    is_double_pair = False
    is_single_pair = False
    highest_card = ''
    hand_dict = {}
    
    def __init__(self, hand):
        self.hand_dict = self.parse_input(hand)
        print(self.hand_dict)
        self.check_is_double_pair()
        if not self.is_double_pair:
            self.check_is_single_pair()
            if not self.is_single_pair: 
                self.is_straight=self.check_is_straight()
                self.check_is_flush()
                self.is_straight_flush = self.is_straight and self.is_flush
                if not self.is_straight and not self.is_flush and not self.is_straight_flush:
                    self.define_highest_card()
        print("straight", self.is_straight, 'flush', self.is_flush, 'is_straight_flush', self.is_straight_flush, 'double pair', self.is_double_pair, 'single pair', self.is_single_pair, 'high card', self.highest_card)
        
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
        nums = [k for k in self.hand_dict.keys()]
        nums.sort()

        if 14 in nums:
            nums.insert(0,1)
        for i in range(0,len(nums)-2):
            if not(nums[i+1] - nums[i] == 1):
                self.is_straight=False
                break

        
    def check_is_flush(self):
        # not flush if dict only has < 5 keys
        if len(self.hand_dict.keys()) < 5:
            return False
        values = list(self.hand_dict.values())

        self.is_flush = (all(suit[0] == values[0][0] for suit in values))

    def check_is_double_pair(self):
        #check if there are only 3 keys
        self.is_double_pair = len(self.hand_dict.keys()) == 3

    def check_is_single_pair(self):
        #check if there are only 4 keys
        self.is_single_pair = len(self.hand_dict.keys()) == 4
    
    def define_highest_card(self):
        nums = [k for k in self.hand_dict.keys()]
        print(self.hand_dict.keys())
        nums.sort()
        print(nums)
        self.highest_card = f"{nums[4]} of {self.hand_dict[nums[4]][0]}"

def compare_hands(hand1, hand2):
    """Compare 2 hands
    Ignoring 5 of a kind (no wild cards), so the highest hand is a straight flush
    Suits don't matter except in a flush or straight flush
    
    hand1, hand2: [J spade, J heart, 9 spade, 2 diamond, 3 club]
    
    #break up into dict
    
    {
        J: [heart, spade],
        9: [spade],
        2: [diamond],
        3: [club]
    }
    also at the same time when parsing see if it is a flush
    """
    # check hand1
    hand1_obj = Hand(hand1)
    hand2_obj = Hand(hand2)
    
    #compare both hands
    
    
    
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
hand1=["4 spade", "J heart", "9 spade", "2 diamond", "3 club"]
hand2=["J spade", "J heart", "9 spade", "2 diamond", "3 club"]
compare_hands(hand1, hand2)

"""
errors: check that each hand is 5 elements long
elements are from 2-10, JQKA (A can be high or low)
- less than 5 keys in dict (repeated num)
- need to add A as 1 code
- 
"""

    