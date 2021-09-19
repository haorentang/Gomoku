

dirx = [1,1,0,-1,-1,-1,0,1]
diry = [0,1,1,1,0,-1,-1,-1]

class AI:

    def __init__(self,map,color):
        self.map = map
        self.color = color
        self.level1max = -200000
        self.level2min = 200000

    def getscore(self,x, y):
        score = 0
        for dire in range(4):
            type = line(x, y, dire, self.map)
            if type == "five":
                return 100000
            elif type == "live four":
                return 10000
            elif type == "rush four":
                score += 1050
            elif type == "jump four":
                score += 1050
            elif type == "live three":
                score += 1000
            elif type == "live jump three":
                score += 800
            elif type == "rush three":
                score += 105
            elif type == "rush jump three":
                score += 105
            elif type == "live two":
                score += 100
            elif type == "live jump two":
                score += 80
            elif type == "rush two":
                score += 11
            elif type == "rush jump two":
                score += 11
            elif type == "clear direction":
                score += 10
        return score

    def downOk(self,x, y):
        if self.map[x][y] == 0 & inRange(x, y):
            return True
        else:
            return False

    def AIlevel1(self, col):
        self.level1max = -200000
        if self.map[7][7] == 0:
            return 7, 7
        bestx = -1
        besty= -1
        for x in [7, 8, 6, 5, 9, 4, 10, 3, 11, 2, 12, 1, 13, 0, 14]:
            for y in [7, 8, 6, 5, 9, 4, 10, 3, 11, 2, 12, 1, 13, 0, 14]:
                if not self.downOk(x, y):
                    continue
                self.map[x][y] = col
                tempp = getscore(x, y,self.map)
                if tempp >= 100000:
                    return x, y
                tempp = self.AIlevel2(col)
                self.map[x][y] = 0
                if tempp > self.level1max:
                    self.level1max = tempp
                    bestx = x
                    besty = y
        print(self.level1max)
        return bestx, besty

    def AIlevel2(self, col):
        self.level2min = 200000
        for x in [7, 8, 6, 5, 9, 4, 10, 3, 11, 2, 12, 1, 13, 0, 14]:
            for y in [7, 8, 6, 5, 9, 4, 10, 3, 11, 2, 12, 1, 13, 0, 14]:
                if not self.downOk(x, y):
                    continue
                self.map[x][y] = 3 - col
                currentscore = getscore(x, y,self.map)
                if currentscore >= 100000:
                    self.map[x][y] = 0
                    return -100000
                currentscore = self.AIlevel3(currentscore, col)
                if currentscore < self.level1max:
                    self.map[x][y] = 0
                    return -100000
                self.map[x][y] = 0
                if currentscore < self.level2min:
                    self.level2min = currentscore
        return self.level2min

    def AIlevel3(self,p2, col):
        maxscore = -200000
        for x in [7, 8, 6, 5, 9, 4, 10, 3, 11, 2, 12, 1, 13, 0, 14]:
            for y in [7, 8, 6, 5, 9, 4, 10, 3, 11, 2, 12, 1, 13, 0, 14]:
                if not self.downOk(x, y):
                    continue
                self.map[x][y] = col
                current_score = getscore(x, y,self.map)
                if current_score >= 100000:
                    self.map[x][y] = 0
                    return 100000
                if current_score - p2 * 2 > self.level2min:
                    self.map[x][y] = 0
                    return 100000
                self.map[x][y] = 0
                if current_score - p2 * 2 > maxscore:
                    maxscore = current_score - p2 * 2
        return maxscore

    def ai_move(self):
        x, y = self.AIlevel1(self.color)
        return x, y

def inRange(x,y):
    if (x < 0 or x > 14 or y < 0 or y > 14):
        return False
    return True



def line(x,y,dire,map):
    col = map[x][y]
    length = 1
    jump = False
    liveend1 = True
    liveend2 = True
    for i in range(1,5):
        currentx = x+dirx[dire] * i
        currenty = y+diry[dire] * i
        nextx = x + dirx[dire] * (i + 1)
        nexty = y + diry[dire] * (i + 1)
        if not inRange(currentx,currenty):
            liveend1 = False
            break
        elif (map[currentx][currenty] == 3 - col):
            liveend1 = False
            break
        elif(map[currentx][currenty] == 0 & jump == False):
            if not inRange(nextx, nexty):
                break
            if (map[nextx][nexty] == col):
                jump = True
                continue
            if (map[nextx][nexty] != col):
                break
        elif(map[currentx][currenty] == 0):
            break
        length += 1

    for i in range(1, 5):
        currentx = x - dirx[dire] * i
        currenty = y - diry[dire] * i
        nextx = x - dirx[dire] * (i + 1)
        nexty = y - diry[dire] * (i + 1)
        if not inRange(currentx, currenty):
            liveend2 = False
            break
        if (map[currentx][currenty] == 3 - col):
            liveend2 = False
            break
        if (map[currentx][currenty] == 0 & jump == False):
            if not inRange(nextx, nexty):
                break
            if (map[nextx][nexty] == col):
                jump = True
                continue
            if (map[nextx][nexty] != col):
                break
        elif (map[currentx][currenty] == 0):
            break
        length+= 1
    if(length >= 5 and not jump):
        return "five"
    elif(length == 5):
        return "jump four"
    if (length == 4 and not jump and liveend1 and liveend2):
        return "live four"
    elif(length == 4 and not jump and not liveend1 and not liveend2):
        return "dead four"
    elif (length == 4 and not jump):
        return "rush four"
    elif (length == 4 and jump):
        return "jump four"
    if (length == 3 and not jump and liveend1 and liveend2):
        return "live three"
    elif (length == 3 and not liveend1 and not liveend2):
        return "dead three"
    elif (length == 3 and not jump):
        return "rush three"
    elif (length == 3 and jump and liveend1 and liveend2):
        return "live jump three"
    elif (length == 3 and jump):
        return "rush jump three"
    if (length == 2 and not jump and liveend1 and liveend2):
        return "live two"
    elif (length == 2 and not liveend1 and not liveend2):
        return "dead two"
    elif (length == 2 and not jump):
        return "rush two"
    elif (length == 2 and jump and liveend1 and liveend2):
        return "live jump two"
    elif (length == 2 and jump):
        return "rush jump two"
    elif (length == 1 and liveend1 and liveend2):
        return "clear direction"
    return "None"


def getscore(x,y,map):
    score = 0
    for dire in range(4):
        type = line(x,y,dire,map)
        if(type == "five"):
            return 100000
        elif(type == "live four"):
            return 10000
        elif(type == "rush four"):
            score += 1050
        elif(type == "jump four"):
            score += 1050
        elif(type == "live three"):
            score += 1000
        elif (type == "live jump three"):
            score += 800
        elif (type == "rush three"):
            score += 105
        elif (type == "rush jump three"):
            score += 105
        elif (type == "live two"):
            score += 100
        elif (type == "live jump two"):
            score += 80
        elif (type == "rush two"):
            score += 11
        elif (type == "rush jump two"):
            score += 11
        elif (type == "clear direction"):
            score += 10
    return score


def win1(i,j,map):
    for dire in range(4):
        type = line(i, j, dire, map)
        if (type == "five"):
            return True
    return False
