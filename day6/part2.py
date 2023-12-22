import re

data = open('puzzleData.txt')

times = []
distances = []


# Record the times and distances from the file, but ignore spaces
line = data.readline()
line = line.split(":")
line = line[1].strip()
line = line.replace(" ", "")
# print(line) # debug 
time = int(line)

line = data.readline()
line = line.split(":")
line = line[1].strip()
line = line.replace(" ", "")
# print(line) # debug
distance = int(line)

waysToWin = 0

# ------- RACES ------- #
for timePressed in range(time, -1, -1):
    distanceTraveled = (time - timePressed) * timePressed
    # print("You traveled", distanceTraveled, "after pushing the button for", timePressed, "milliseconds")
    if distanceTraveled > distance:
        waysToWin += 1
        
print(waysToWin)

data.close()
