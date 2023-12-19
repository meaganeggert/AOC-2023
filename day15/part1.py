data = open('puzzleData.txt')

values = data.readline().split(",")
print(values) # debug

sum = 0
currentValue = 0
asciiVal = 0

for value in values: # For each value in the list
    # print(value) # debug
    for char in range(len(value)): # For each character in the value (string)
        # print(ord(value[char])) # debug
        # Custom HASH function
        asciiVal = ord(value[char]) # Convert to ascii
        currentValue += asciiVal
        currentValue *= 17 
        currentValue = currentValue % 256
    sum += currentValue # Add string's value to the sum
    currentValue = 0 # Reset current value for next string

print("Sum", sum)

data.close()