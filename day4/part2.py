data = open('puzzleData.txt')
sum = 0
count = 0

cards = {} # Empty map to map card IDs with their numbers
cardQty = {} # Empty map to show how many of each card you have
matches = {} # Empty map to show how many matches were made in each round

for line in data:
    hands = line.split("|") # Break the data up by hands
    cardID = hands[0].split(":")[0] # Get the card data
    cardID = cardID.split()[1] # Get just the number of the card
    cardQty[cardID] = 1
    matches[cardID] = 1
    
data.close()

print(cardQty)

data = open('puzzleData.txt')
for line in data:
    hands = line.split("|") # Break the data up by hands
    cardID = hands[0].split(":")[0] # Get the card data
    cardID = cardID.split()[1] # Get just the number of the card
    winningNumbers = hands[0].split(":")[1] # Drop "Card X: "
    winningNumbers = winningNumbers.split() # Create list of winning numbers
    myNumbers = hands[1].split() # Create list of my numbers

    cards[cardID] = winningNumbers
    
    numbersMatched = 0
    for number in myNumbers:
        if number in winningNumbers:
            numbersMatched += 1
    matches[cardID] = numbersMatched
    # print("Numbers matched:" + str(numbersMatched))
        
for card in matches: # For each card
    for i in range(cardQty[card]): # For each copy
        for j in range(matches[card]): # How many cards do I create copies for
            nextCard = str(int(card) + j + 1)
            cardQty[nextCard] += 1
            
for qty in cardQty:
    sum += cardQty[qty]

print("Sum: " + str(sum) + "\n")

data.close()