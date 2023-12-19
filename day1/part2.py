import re

data = open('puzzleData.txt')

lines = data.read().splitlines()
# print(lines) # debug

# Map written words to their digit values
translator = {("nine", 9), ("eight", 8), ("seven", 7), ("six", 6), ("five", 5), ("four", 4), ("three", 3), ("two", 2), ("one", 1)}
# print(translator) # debug

indeces = []
values = {}
sum = 0
count = 0

for line in lines:
    temp = re.findall('\d+', line) # Regex to find all explicit numbers in each line
    # print(temp) # debug
    for number in temp:
        numberIdx = line.find(number) # Find the first instance of the number
        # print(numberIdx) # debug
        indeces.append(numberIdx)
        values[numberIdx] = number
        for i in range(numberIdx + 1, len(line)): # Find the other instances of the number
            numberIdx = line.find(number, i)
            if numberIdx == -1:
                break
            indeces.append(numberIdx)
            values[numberIdx] = number
    for key in translator:
        if key[0] in line:
            wordIdx = line.find(key[0]) # Find the first instance of the written number
            indeces.append(wordIdx)
            values[wordIdx] = key[1]
            for i in range(wordIdx + 1, len(line)): # Find the other instances of the written number
                wordIdx = line.find(key[0], i)
                if wordIdx == -1:
                    break
                indeces.append(wordIdx)
                values[wordIdx] = key[1]

    minIdx = min(indeces)
    maxIdx = max(indeces)
    firstNumber = line[minIdx]
    lastNumber = line[maxIdx]
    
    if firstNumber.isdigit():
        firstNumber = firstNumber # First number is the single digit at the lowest index related to a number
    else:
        firstNumber = values[minIdx] # First number is the value represented by the written number that starts at the min index
    if lastNumber.isdigit():
        lastNumber = int(values[maxIdx]) % 10 # We only want the last digit of any explicit numbers
    else:
        lastNumber = values[maxIdx] # Last number is the value represented by the written number that starts at the max index
    numberString = str(firstNumber) + str(lastNumber)
    
    sum += int(numberString)
    indeces.clear()
    # print(values) # debug
    values.clear()
    
    
    
print("Sum:", sum)
data.close()