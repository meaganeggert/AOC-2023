# create a custom class for cards
class Hand:
    # setting up card values for comparison
    cardValues = {"A": 14, "K": 13, "Q": 12, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1}
    
    def __init__(self, name, bid):
        self.name = name
        self.bid = int(bid)
        self.rank = 0
        # 5-of-a-kind = 7
        # 4-of-a-kind = 6
        # full-house = 5
        # 3-of-a-kind = 4
        # 2-pair = 3
        # 1-pair = 2
        # high-card = 1
        self.type = 0
        self.typeString = ""
        self.winnings = 0
    def __str__(self):
        return f"Hand: {self.name} -- Type: {self.typeString} -- Bid: {self.bid} -- Rank: {self.rank} -- Winnings: {self.winnings}"
    
    def setTypeString(self, handType):
        typeStrings = {7: "5-of-a-kind", 6: "4-of-a-kind", 5: "full-house", 4: "3-of-a-kind", 3: "2-pair", 2: "pair", 1: "high-card"}
        self.typeString = typeStrings[handType]
        return
    
    # function to figure out what kind of hand it is
    def findType(self):
        uniqueCards = []
        for char in self.name:
            if char not in uniqueCards:
                uniqueCards.append(char)
        # print(uniqueCards) # debug
        if "J" in uniqueCards:
            jokers = self.name.count("J")
            
        # if there's only one type of card, it's a 5-of-a-kind
        if len(uniqueCards) == 1:
            self.type = 7

        # if there are 5 different cards, it's a high-card hand
        elif len(uniqueCards) == 5:
            if not "J" in uniqueCards: # no jokers
                self.type = 1 # high-card
            else: # with a joker
                self.type = 2 # makes it a pair
                
        # if there are 2 different cards, it's a 4-of-a-kind or a full-house
        # if there's a joker, it could be 5-of-a-kind
        elif len(uniqueCards) == 2:
            counts = []
            for card in uniqueCards:
                counts.append(self.name.count(card))
            # if there's 4 of any card, it must be a 4-of-a-kind
            if 4 in counts:
                if not "J" in uniqueCards: # no jokers
                    self.type = 6 # 4-of-a-kind
                else: # with a joker
                    self.type = 7 # makes it a 5-of-a-kind
            else: 
                if not "J" in uniqueCards: # no jokers
                    self.type = 5 # full-house
                else: # with a joker
                    self.type = 7 # 5-of-a-kind

        # if there are 4 different cards, it's a pair
        # if there's a joke, it's a 3-of-a-kind
        elif len(uniqueCards) == 4:
            if not "J" in uniqueCards: # no jokers
                self.type = 2 # pair
            else: # with a joker
                self.type = 4 # 3-of-a-kind
                
        # if there are 3 different cards, it's either a 3-of-a-kind or 2-pair
        # or if there's a joker, it could be a full-house or a 4-of-a-kind
        else:
            counts = []
            for card in uniqueCards:
                counts.append(self.name.count(card))
            # if there's 3 of any card
            if 3 in counts:
                if not "J" in uniqueCards: # no jokers
                    self.type = 4 # 3-of-a-kind
                else: # with jokers
                    self.type = 6 # 4-of-a-kind
            else:
                if not "J" in uniqueCards: # no jokers
                    self.type = 3 # 2-pair
                else:
                    if jokers == 1:
                        self.type = 5 # full-house
                    else:
                        self.type = 6 # 4-of-a-kind

        self.setTypeString(self.type)
        return
    
    # overload < operator to sort hands based on card strength
    def __lt__(self, otherHand : 'Hand'):
        for idx in range(len(self.name)):
            if self.cardValues[self.name[idx]] == self.cardValues[otherHand.name[idx]]:
                continue
            else:
                return self.cardValues[self.name[idx]] < self.cardValues[otherHand.name[idx]]
            
        return

data = open('puzzleData.txt')

# mapping hands to their bids
hands = []
for line in data:
    line = line.split()
    temp = Hand(line[0], line[1])
    hands.append(temp)
    
# find what kind of hand each hand is
for hand in hands:
    hand.findType()

# print original hands
# print("original list:")
# for hand in hands:
#     print(hand)
# print()

# setting up a list of ordered hands
rankedHands = []

# example of how to sort on a certain value
# rankedHands = sorted(hands, key = lambda hand: hand.bid)

# sort the list
rankedHands = sorted(hands, key = lambda hand: (hand.type, hand))

# print sorted hands and figure out rank and winnings
# print("ranked list:")
rank = 1
totalWinnings = 0
for hand in rankedHands:
    hand.rank = rank
    hand.winnings = hand.rank * hand.bid
    totalWinnings += hand.winnings
#     print(hand)
    rank += 1

print("\ntotal winnings:\n", totalWinnings)
data.close()
