data = open('puzzleData.txt')

times = []
distances = []


# Record the times and distances from the file
line = data.readline()
line = line.split()
for x in range(1, len(line)):
    times.append(int(line[x]))
line = data.readline()
line = line.split()
for x in range(1, len(line)):
    distances.append(int(line[x]))
# print(times) # debug
# print(distances) # debug


marginOfError = 1
waysToWin = 0

# ------- RACES ------- #
for race in range(4):
    recordTime = times[race]
    for timePressed in range(times[race], -1, -1):
        distanceTraveled = (recordTime - timePressed) * timePressed
        # print("You traveled", distanceTraveled, "after pushing the button for", timePressed, "milliseconds")
        if distanceTraveled > distances[race]:
            waysToWin += 1
    # print(waysToWin) # debug
    marginOfError *= waysToWin
    waysToWin = 0
        
print(marginOfError)

data.close()