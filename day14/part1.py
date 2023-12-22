data = open('puzzleData_short.txt')

lines = data.read().splitlines()
# print(lines)

rows = len(lines)
cols = len(lines[0])
print(rows, "x", cols, "grid")

grid = [["." for i in range(cols)] for j in range(rows)]
flipped = [["." for i in range(cols)] for j in range(rows)]
shifted = [["." for i in range(cols)] for j in range(rows)]

# create 2d grid
for row in range(rows):
    for col in range(cols):
        grid[row][col] = lines[row][col]
        flipped[col][row] = lines[row][col]
        shifted[col][row] = lines[row][col]

# # print initial grid
# for x in range(rows):
#     for y in range(cols):
#         print(grid[x][y], " ", end="")
#     print()
# print()
# 
# print flipped grid
for x in range(rows):
    for y in range(cols):
        print(flipped[x][y], " ", end="")
    print()
print()

y = 0
ystart = 0
count = 0
counts = []
roundCounts = {}
lastCube = 0
foundCube = False
firstCube = True

for row in range(rows):
    while (y < cols):
        if flipped[row][y] == "O":
            count += 1
#             print("found O at", row, ",", y) # debug
        if flipped[row][y] == "#":
#             print("found # at", row, ",", y) # debug
            if firstCube:
                ystart = 0
            elif not firstCube and foundCube:
#                 print("check")
#                 print("row", row, "at", y)
                ystart = lastCube + 1
                
#             print("row", row)
#             print("ystart", ystart)
#             print("last", lastCube)
#             print("count", count)
            foundCube = True
            firstCube = False
            lastCube = y

            if count > 0:
                counts.append(count)
#                 print("ystart", ystart)
                for num in range(ystart, lastCube):
                    if count > 0:
                        shifted[row][num] = "O"
                    else:
                        shifted[row][num] = "."
                    count -= 1
                
            
            count = 0
        y += 1
    if firstCube:
        ystart = lastCube
    else:
        ystart = lastCube + 1
#     print(ystart, "at beginning")
    if count > 0:
        counts.append(count)
        for num in range(ystart, cols):
#             print(ystart, "in loop")
            if count > 0:
#                 print("count", count)
                shifted[row][num] = "O"
            else:
#                 print("index", num)
#                 print("count", count)
                shifted[row][num] = "."
            count -= 1
    
    lastCube = 0
    foundCube = False
    firstCube = True
    count = 0
    y = 0
    ystart = 0
    roundCounts[row] = counts.copy()
    counts.clear()
    
# print ("# of round rocks per row:")
# print(roundCounts)
# print()

# print shifted grid
print("After Shift:")
for x in range(rows):
    for y in range(cols):
        print(shifted[x][y], " ", end="")
    print()
print()

load = 0
for x in range(rows):
    for y in range(cols):
        if shifted[x][y] == "O":
            load += (rows-y)
#             print("adding", rows-y) # debug
#     print()


print("Load:", load)

data.close()