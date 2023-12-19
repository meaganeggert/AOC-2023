data = open('puzzleData.txt')
sum = 0
lineWin = 0

for line in data:
    hands = line.split("|") # Break the data up by hands
    winningNumbers = hands[0].split(":")[1] # Drop "Card X: "
    winningNumbers = winningNumbers.split() # Create list of winning numbers
    myNumbers = hands[1].split() # Create list of my numbers

    # print(winningNumbers)
    # print(myNumbers)
    
    count = 0
    for number in myNumbers:
        if number in winningNumbers:
            # print(number)
            count += 1
    if count < 1:
        lineWin = 0
    else:
        lineWin = pow(2, count - 1)
    # print("LineTotal: " + str(lineWin))
    sum += lineWin
    
    # print("\n")

print("Sum: " + str(sum) + "\n")
