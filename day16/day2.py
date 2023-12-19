def StartLeftEdgeTrace(cur_row, cur_col, chargedMap, lineMap, leftEdge_charges):
    count = 0
    for colIdx in range(len(lineMap[0])):
        if lineMap[cur_row][colIdx] == ".":
            chargedMap[cur_row][colIdx] = "*"
        elif lineMap[cur_row][colIdx] == "|":
            chargedMap[cur_row][colIdx] = "*"
            beams["right"].append((cur_row, colIdx))
            VerticalSplitter(cur_row, colIdx)
            break
        elif lineMap[cur_row][colIdx] == "-":
            chargedMap[cur_row][colIdx] = "*"
            beams["right"].append((cur_row, colIdx))
            HorizontalSplitter(cur_row, colIdx)
            break
        elif lineMap[cur_row][colIdx] == "\\":
            chargedMap[cur_row][colIdx] = "*"
            beams["right"].append((cur_row, colIdx))
            DownReflector(cur_row, colIdx)
            break
        elif lineMap[cur_row][colIdx] == "/":
            chargedMap[cur_row][colIdx] = "*"
            beams["right"].append((cur_row, colIdx))
            UpReflector(cur_row, colIdx)
            break
    # print chargedMap so it actually looks like a grid
    for x in range(len(chargedMap)):
        for y in range(len(chargedMap[x])):
            # print(chargedMap[x][y], " ", end="")
            if chargedMap[x][y] == "*":
                count += 1
        # print()
    # print()
    leftEdge_charges[(cur_row, cur_col)] = count

    # print("Count:", count)
    
    
def StartRightEdgeTrace(cur_row, cur_col, chargedMap, lineMap, rightEdge_charges):
    count = 0
    for colIdx in range(cur_col, -1, -1):
        if lineMap[cur_row][colIdx] == ".":
            chargedMap[cur_row][colIdx] = "*"
        elif lineMap[cur_row][colIdx] == "|":
            chargedMap[cur_row][colIdx] = "*"
            beams["left"].append((cur_row, colIdx))
            VerticalSplitter(cur_row, colIdx)
            break
        elif lineMap[cur_row][colIdx] == "-":
            chargedMap[cur_row][colIdx] = "*"
            beams["left"].append((cur_row, colIdx))
            HorizontalSplitter(cur_row, colIdx)
        elif lineMap[cur_row][colIdx] == "\\":
            chargedMap[cur_row][colIdx] = "*"
            beams["left"].append((cur_row, colIdx))
            UpReflector(cur_row, colIdx)
            break
        elif lineMap[cur_row][colIdx] == "/":
            chargedMap[cur_row][colIdx] = "*"
            beams["left"].append((cur_row, colIdx))
            DownReflector(cur_row, colIdx)
            break
    # print chargedMap so it actually looks like a grid
    for x in range(len(chargedMap)):
        for y in range(len(chargedMap[x])):
            # print(chargedMap[x][y], " ", end="")
            if chargedMap[x][y] == "*":
                count += 1
        # print()
    # print()
    rightEdge_charges[(cur_row, cur_col)] = count

    # print("Count:", count)


def StartTopEdgeTrace(cur_row, cur_col, chargedMap, lineMap, topEdge_charges):
    count = 0
    for rowIdx in range(len(lineMap)):
        if lineMap[rowIdx][cur_col] == ".":
            chargedMap[rowIdx][cur_col] = "*"
        elif lineMap[rowIdx][cur_col] == "|":
            chargedMap[rowIdx][cur_col] = "*"
            beams["down"].append((rowIdx, cur_col))
            VerticalSplitter(rowIdx, cur_col)
            break
        elif lineMap[rowIdx][cur_col] == "-":
            chargedMap[rowIdx][cur_col] = "*"
            beams["down"].append((rowIdx, cur_col))
            HorizontalSplitter(rowIdx, cur_col)
            break
        elif lineMap[rowIdx][cur_col] == "\\":
            chargedMap[rowIdx][cur_col] = "*"
            beams["down"].append((rowIdx, cur_col))
            RightReflector(rowIdx, cur_col)
            break
        elif lineMap[rowIdx][cur_col] == "/":
            chargedMap[rowIdx][cur_col] = "*"
            beams["down"].append((rowIdx, cur_col))
            LeftReflector(rowIdx, cur_col)
            break
    # print chargedMap so it actually looks like a grid
    for x in range(len(chargedMap)):
        for y in range(len(chargedMap[x])):
            # print(chargedMap[x][y], " ", end="")
            if chargedMap[x][y] == "*":
                count += 1
        # print()
    # print()
    topEdge_charges[(cur_row, cur_col)] = count

    # print("Count:", count)
    
    
def StartBottomEdgeTrace(cur_row, cur_col, chargedMap, lineMap, bottomEdge_charges):
    count = 0
    for rowIdx in range(cur_col - 1, -1, -1):
        if lineMap[rowIdx][cur_col] == ".":
            chargedMap[rowIdx][cur_col] = "*"
        elif lineMap[rowIdx][cur_col] == "|":
            chargedMap[rowIdx][cur_col] = "*"
            beams["up"].append((rowIdx, cur_col))
            VerticalSplitter(rowIdx, cur_col)
            break
        elif lineMap[rowIdx][cur_col] == "-":
            chargedMap[rowIdx][cur_col] = "*"
            beams["up"].append((rowIdx, cur_col))
            HorizontalSplitter(rowIdx, cur_col)
            break
        elif lineMap[rowIdx][cur_col] == "\\":
            chargedMap[rowIdx][cur_col] = "*"
            beams["up"].append((rowIdx, cur_col))
            LeftReflector(rowIdx, cur_col)
            break
        elif lineMap[rowIdx][cur_col] == "/":
            chargedMap[rowIdx][cur_col] = "*"
            beams["up"].append((rowIdx, cur_col))
            RightReflector(rowIdx, cur_col)
            break
    # print chargedMap so it actually looks like a grid
    for x in range(len(chargedMap)):
        for y in range(len(chargedMap[x])):
            # print(chargedMap[x][y], " ", end="")
            if chargedMap[x][y] == "*":
                count += 1
        # print()
    # print()
    bottomEdge_charges[(cur_row, cur_col)] = count

    # print("Count:", count)
    
# -------------------------------------------------------------------

def VerticalSplitter(line_idx, column_idx):
    # going down
    # print("hit v-splitter at", line_idx, ",", column_idx)
    for row in range(line_idx, len(chargedMap)):
        if lineMap[row][column_idx] == ".":
            # chargedMap[row][column_idx] = "v"
            chargedMap[row][column_idx] = "*"
        elif lineMap[row][column_idx] == "|":
            # chargedMap[row][column_idx] = "|"
            chargedMap[row][column_idx] = "*"
        elif lineMap[row][column_idx] == "-":
            if (row, column_idx) in beams["down"]:
                break
            beams["down"].append((row, column_idx))
            # chargedMap[row][column_idx] = "-"
            chargedMap[row][column_idx] = "*"
            HorizontalSplitter(row, column_idx)
            break
            # chargedMap[row][column_idx] = "@"
        elif lineMap[row][column_idx] == "/":
            if (row, column_idx) in beams["down"]:
                break
            beams["down"].append((row, column_idx))
            # chargedMap[row][column_idx] = "/"
            chargedMap[row][column_idx] = "*"
            LeftReflector(row, column_idx)
            break
        elif lineMap[row][column_idx] == "\\":
            if (row, column_idx) in beams["down"]:
                break
            beams["down"].append((row, column_idx))
            # chargedMap[row][column_idx] = "\\"
            chargedMap[row][column_idx] = "*"
            RightReflector(row, column_idx)
            break
    # going up
    for row in range(line_idx, -1, -1):
        if lineMap[row][column_idx] == ".":
            # chargedMap[row][column_idx] = "^"
            chargedMap[row][column_idx] = "*"
        elif lineMap[row][column_idx] == "|":
            # chargedMap[row][column_idx] = "|"
            chargedMap[row][column_idx] = "*"
        elif lineMap[row][column_idx] == "-":
            if (row, column_idx) in beams["up"]:
                break
            beams["up"].append((row, column_idx))
            # chargedMap[row][column_idx] = "-"
            chargedMap[row][column_idx] = "*"
            HorizontalSplitter(row, column_idx)
            break
            # chargedMap[row][column_idx] = "@"
        elif lineMap[row][column_idx] == "/":
            if (row, column_idx) in beams["up"]:
                break
            beams["up"].append((row, column_idx))
            # chargedMap[row][column_idx] = "/"
            chargedMap[row][column_idx] = "*"
            RightReflector(row, column_idx)
            break
        elif lineMap[row][column_idx] == "\\":
            if (row, column_idx) in beams["up"]:
                break
            beams["up"].append((row, column_idx))
            # chargedMap[row][column_idx] = "\\"
            chargedMap[row][column_idx] = "*"
            LeftReflector(row, column_idx)
            break

def HorizontalSplitter(line_idx, column_idx):
    # going right
    for col in range(column_idx, len(chargedMap[line_idx])):
        if lineMap[line_idx][col] == ".":
            # chargedMap[line_idx][col] = ">"
            chargedMap[line_idx][col] = "*"
        elif lineMap[line_idx][col] == "-":
            # chargedMap[line_idx][col] = "-"
            chargedMap[line_idx][col] = "*"
        elif lineMap[line_idx][col] == "|":
            if (line_idx, col) in beams["right"]:
                break
            beams["right"].append((line_idx, col))
            # chargedMap[line_idx][col] = "|"
            chargedMap[line_idx][col] = "*"
            VerticalSplitter(line_idx, col)
            break
        elif lineMap[line_idx][col] == "/":
            if (line_idx, col) in beams["right"]:
                break
            beams["right"].append((line_idx, col))
            # chargedMap[line_idx][col] = "/"
            chargedMap[line_idx][col] = "*"
            UpReflector(line_idx, col)
            break
        elif lineMap[line_idx][col] == "\\":
            if (line_idx, col) in beams["right"]:
                break
            beams["right"].append((line_idx, col))
            # chargedMap[line_idx][col] = "\\"
            chargedMap[line_idx][col] = "*"
            DownReflector(line_idx, col)
            break
    # going left
    for col in range(column_idx, -1, -1):
        if lineMap[line_idx][col] == ".":
            # chargedMap[line_idx][col] = "<"
            chargedMap[line_idx][col] = "*"
        elif lineMap[line_idx][col] == "-":
            # chargedMap[line_idx][col] = "-"
            chargedMap[line_idx][col] = "*"
        elif lineMap[line_idx][col] == "|":
            if (line_idx, col) in beams["left"]:
                break
            beams["left"].append((line_idx, col))
            # chargedMap[line_idx][col] = "|"
            chargedMap[line_idx][col] = "*"
            VerticalSplitter(line_idx, col)
            break
        elif lineMap[line_idx][col] == "/":
            if (line_idx, col) in beams["left"]:
                break
            beams["left"].append((line_idx, col))
            # chargedMap[line_idx][col] = "/"
            chargedMap[line_idx][col] = "*"
            DownReflector(line_idx, col)
            break
        elif lineMap[line_idx][col] == "\\":
            if (line_idx, col) in beams["left"]:
                break
            beams["left"].append((line_idx, col))
            # chargedMap[line_idx][col] = "\\"
            chargedMap[line_idx][col] = "*"
            UpReflector(line_idx, col)
            break

def UpReflector(line_idx, column_idx):
    # going up
    for row in range(line_idx - 1, -1, -1):
        if lineMap[row][column_idx] == ".":
            # chargedMap[row][column_idx] = "^"
            chargedMap[row][column_idx] = "*"
        elif lineMap[row][column_idx] == "-":
            if (row, column_idx) in beams["up"]:
                break
            beams["up"].append((row, column_idx))
            # chargedMap[row][column_idx] = "-"
            chargedMap[row][column_idx] = "*"
            HorizontalSplitter(row, column_idx)
            break
        elif lineMap[row][column_idx] == "|":
            if (row, column_idx) in beams["up"]:
                break
            beams["up"].append((row, column_idx))
            #chargedMap[row][column_idx] = "|"
            chargedMap[row][column_idx] = "*"
#             VerticalSplitter(row, column_idx)
#             break
        elif lineMap[row][column_idx] == "/":
            if (row, column_idx) in beams["up"]:
                break
            beams["up"].append((row, column_idx))
            # chargedMap[row][column_idx] = "/"
            chargedMap[row][column_idx] = "*"
            RightReflector(row, column_idx)
            break
        elif lineMap[row][column_idx] == "\\":
            if (row, column_idx) in beams["up"]:
                break
            beams["up"].append((row, column_idx))
            # chargedMap[row][column_idx] = "\\"\
            chargedMap[row][column_idx] = "*"
            LeftReflector(row, column_idx)
            break

def RightReflector(line_idx, column_idx):
    # going right
    for col in range(column_idx + 1, len(chargedMap[line_idx])):
        if lineMap[line_idx][col] == ".":
            # chargedMap[line_idx][col] = ">"
            chargedMap[line_idx][col] = "*"
        elif lineMap[line_idx][col] == "|":
            if (line_idx, col) in beams["right"]:
                break
            beams["right"].append((line_idx, col))
            # chargedMap[line_idx][col] = "|"
            chargedMap[line_idx][col] = "*"
            VerticalSplitter(line_idx, col)
            break
        elif lineMap[line_idx][col] == "-":
            if (line_idx, col) in beams["right"]:
                break
            beams["up"].append((line_idx, col))
            #chargedMap[line_idx][col] = "|"
            chargedMap[line_idx][col] = "*"
        elif lineMap[line_idx][col] == "/":
            if (line_idx, col) in beams["right"]:
                break
            beams["right"].append((line_idx, col))
            #chargedMap[line_idx][col] = "/"
            chargedMap[line_idx][col] = "*"
            UpReflector(line_idx, col)
            break
        elif lineMap[line_idx][col] == "\\":
            if (line_idx, col) in beams["right"]:
                break
            beams["right"].append((line_idx, col))
            # chargedMap[line_idx][col] = "\\"
            chargedMap[line_idx][col] = "*"
            DownReflector(line_idx, col)
            break

def DownReflector(line_idx, column_idx):
    # going down
    for row in range(line_idx + 1, len(chargedMap)):
        if lineMap[row][column_idx] == ".":
            # chargedMap[row][column_idx] = "v"
            chargedMap[row][column_idx] = "*"
        elif lineMap[row][column_idx] == "-":
            if (row, column_idx) in beams["down"]:
                break
            beams["down"].append((row, column_idx))
            # chargedMap[row][column_idx] = "-"
            chargedMap[row][column_idx] = "*"
            HorizontalSplitter(row, column_idx)
            break
        elif lineMap[row][column_idx] == "|":
            if (row, column_idx) in beams["down"]:
                break
            beams["up"].append((row, column_idx))
            #chargedMap[row][column_idx] = "|"
            chargedMap[row][column_idx] = "*"
        elif lineMap[row][column_idx] == "/":
            if (row, column_idx) in beams["down"]:
                break
            beams["down"].append((row, column_idx))
            # chargedMap[row][column_idx] = "/"
            chargedMap[row][column_idx] = "*"
            LeftReflector(row, column_idx)
            break
        elif lineMap[row][column_idx] == "\\":
            if (row, column_idx) in beams["down"]:
                break
            beams["down"].append((row, column_idx))
            # chargedMap[row][column_idx] = "\\"
            chargedMap[row][column_idx] = "*"
            RightReflector(row, column_idx)
            break

def LeftReflector(line_idx, column_idx):
    # going left
    for col in range(column_idx - 1, -1, -1):
        if lineMap[line_idx][col] == ".":
            # chargedMap[line_idx][col] = "<"
            chargedMap[line_idx][col] = "*"
        elif lineMap[line_idx][col] == "|":
            if (line_idx, col) in beams["left"]:
                break
            beams["left"].append((line_idx, col))
            # chargedMap[line_idx][col] = "|"
            chargedMap[line_idx][col] = "*"
            VerticalSplitter(line_idx, col)
            break
        elif lineMap[line_idx][col] == "-":
            if (line_idx, col) in beams["left"]:
                break
            beams["left"].append((line_idx, col))
            # chargedMap[line_idx][col] = "/"
            chargedMap[line_idx][col] = "*"
        elif lineMap[line_idx][col] == "/":
            if (line_idx, col) in beams["left"]:
                break
            beams["left"].append((line_idx, col))
            # chargedMap[line_idx][col] = "/"
            chargedMap[line_idx][col] = "*"
            DownReflector(line_idx, col)
            break
        elif lineMap[line_idx][col] == "\\":
            if (line_idx, col) in beams["left"]:
                break
            beams["left"].append((line_idx, col))
            # chargedMap[line_idx][col] = "\\"
            chargedMap[line_idx][col] = "*"
            UpReflector(line_idx, col)
            break

# -------------------------------------------------------------------

import pprint
data = open('puzzleData.txt')

lines = data.read().splitlines()
# print(lines)
rows = len(lines)
cols = len(lines[0])

beams = {"up": [], "down": [], "right": [], "left": []}
lineMap = {}
chargedMap = [["." for i in range(cols)] for j in range(rows)]

lineNo = 0

for line in lines:
    chars = ([*line])
    lineMap[lineNo] = chars
    lineNo += 1



# print("Grid: ", rows, "x", cols) # debug
leftEdge = [(j, 0) for j in range(rows)]
# print(leftEdge) # debug
rightEdge = [(j, cols - 1) for j in range(rows)]
# print(rightEdge) # debug
topEdge = [(0, i) for i in range(cols)]
# print(topEdge) # debug
bottomEdge = [(rows - 1, i) for i in range(cols)]
# print(bottomEdge) # debug

leftEdge_charges = {}
rightEdge_charges = {}
topEdge_charges = {}
bottomEdge_charges = {}

print("// LEFT EDGE TESTING //")
for pair in leftEdge:
    cur_row = pair[0]
    cur_col = pair[1]
    StartLeftEdgeTrace(cur_row, cur_col, chargedMap, lineMap, leftEdge_charges)
    chargedMap = [["." for i in range(cols)] for j in range(rows)]
    beams = {"up": [], "down": [], "right": [], "left": []}

print("// RIGHT EDGE TESTING //")
for pair in rightEdge:
    cur_row = pair[0]
    cur_col = pair[1]
    StartRightEdgeTrace(cur_row, cur_col, chargedMap, lineMap, rightEdge_charges)
    chargedMap = [["." for i in range(cols)] for j in range(rows)]
    beams = {"up": [], "down": [], "right": [], "left": []}
    
print("// TOP EDGE TESTING //")
for pair in topEdge:
    cur_row = pair[0]
    cur_col = pair[1]
    StartTopEdgeTrace(cur_row, cur_col, chargedMap, lineMap, topEdge_charges)
    chargedMap = [["." for i in range(cols)] for j in range(rows)]
    beams = {"up": [], "down": [], "right": [], "left": []}
    
print("// BOTTOM EDGE TESTING //")
for pair in bottomEdge:
    cur_row = pair[0]
    cur_col = pair[1]
    StartBottomEdgeTrace(cur_row, cur_col, chargedMap, lineMap, bottomEdge_charges)
    chargedMap = [["." for i in range(cols)] for j in range(rows)]
    beams = {"up": [], "down": [], "right": [], "left": []}

print("-------------------")
# print("Left Edge Results:") # debug
# print(leftEdge_charges) # debug
print("Max from Left Edge")
print(max(leftEdge_charges.items(), key = lambda x: x[1]))

print("-------------------")
# print("Right Edge Results:") # debug 
# print(rightEdge_charges) # debug
print("Max from Left Edge")
print(max(rightEdge_charges.items(), key = lambda x: x[1]))

print("-------------------")
# print("Top Edge Results:") # debug
# print(topEdge_charges) # debug
print("Max from Top Edge")
print(max(topEdge_charges.items(), key = lambda x: x[1]))

print("-------------------")
# print("Bottom Edge Results:") # debug
# print(bottomEdge_charges) # debug
print("Max from Left Edge")
print(max(bottomEdge_charges.items(), key = lambda x: x[1]))

# print(beams) # debug
print()



data.close()
