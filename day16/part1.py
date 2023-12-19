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
data = open('puzzleData_short.txt')

lines = data.read().splitlines()
# print(lines)
rows = len(lines)
cols = len(lines[0])

beams = {"up": [], "down": [], "right": [], "left": []}

lineMap = {}
chargedMap = [["." for i in range(cols)] for j in range(rows)]
lineNo = 0

# chargedMap[0][3] = "*" # debug

for line in lines:
    chars = ([*line])
    lineMap[lineNo] = chars
    lineNo += 1

for colIdx in range(len(lineMap[0])):
    if lineMap[0][colIdx] == ".":
        # chargedMap[0][colIdx] = ">"
        chargedMap[0][colIdx] = "*"
    elif lineMap[0][colIdx] == "|":
        # chargedMap[0][colIdx] = "|"
        chargedMap[0][colIdx] = "*"
        beams["right"].append((0, colIdx))
        VerticalSplitter(0, colIdx)
        break
    elif lineMap[0][colIdx] == "-":
        # chargedMap[0][colIdx] = "-"
        chargedMap[0][colIdx] = "*"
        beams["right"].append((0, colIdx))
        HorizontalSplitter(0, colIdx)
        break
    elif lineMap[0][colIdx] == "\\":
        #chargedMap[0][colIdx] = "\\"
        chargedMap[0][colIdx] = "*"
        beams["right"].append((0, colIdx))
        DownReflector(0, colIdx)
        break
    elif lineMap[0][colIdx] == "/":
        # chargedMap[0][colIdx] = "/"
        chargedMap[0][colIdx] = "*"
        beams["right"].append((0, colIdx))
        UpReflector(0, colIdx)
        break


# print(beams) # debug
# print()
 
count = 0 

# print chargedMap so it actually looks like a grid
for x in range(len(chargedMap)):
    for y in range(len(chargedMap[x])):
        # print(chargedMap[x][y], " ", end="")
        if chargedMap[x][y] == "*":
            count += 1
    # print()
print()

print("Count:", count)

data.close()