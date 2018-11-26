class Board:
    def __init__(self, filename, x, y):
        self.filename = filename
        self.letters = [["\0" for x in range(x)] for y in range(y)]
        self.sizeX = x
        self.sizeY = y
        self.foundWords = []
        self.dict = []

    def loadBoard(self):
        try:
            file = open(self.filename)
            y = 0
            for line in file:
                if (y >= self.sizeY):
                    parts = line.split()

                else:
                    if (len(line) < self.sizeX+1):
                        print(f"Line {y} of map is malformed")
                        exit(1)
                    for x in range(self.sizeX):
                        self.letters[y][x] = line[x]#, x, y
                y += 1
            file.close()
        except:
            print(f"Could not load map file {self.filename}")
            exit(1)

    def loadDict(self, dictName):
        try:
            file = open(dictName, "r")
            lines = file.read().upper().split('\n')
            self.dict = lines[0:-1]
            file.close()
        except:
            print(f"Could not find file {dictName} in directory!")
            exit(1)

    def getLetter(self, x, y):
        return self.letters[y][x]

    # Takes a word ("STRING", startingCoordinate) Ex: ("cat", (0,0)) and adds it to list of words we've found.
    def addWord(self, word, startingCoordinate):
        self.foundWords += [(word, startingCoordinate)]

    # finds all words starting with a given start tile coordinate
    def findWordsFromCoordHorizontal(self, x, y):
        # horizontal
        word = ''
        pos = x
        while pos < self.sizeX:
            print(f"x: {pos}")
            word += self.getLetter(pos, y)
            print(word)
            if word in self.dict:
                self.addWord(word, (pos,y))
                print("^ word added!")
            pos += 1
    def findWordsFromCoordVertical(self, x, y):
        # horizontal
        word = ''
        pos = y
        while pos < self.sizeY:
            print(f"y: {pos}")
            word += self.getLetter(x, pos)
            print(word)
            if word in self.dict:
                self.addWord(word, (x,pos))
                print("^ word added!")
            pos += 1
    def findWordsFromCoordDiagUp(self, x, y):
        # diagonal up
        word = ''
        pos = (x,y)
        while pos[0] < self.sizeX and pos[1] < self.sizeY and pos[1] >= 0 and pos[0] >= 0:
            print(f"posdu: {pos}")
            word += self.getLetter(pos[0],pos[1])
            print(word)
            if word in self.dict:
                self.addWord(word, pos)
                print("^ word added!")
            pos = (pos[0]+1,pos[1])
            pos = (pos[0],pos[1]-1)
    def findWordsFromCoordDiagDown(self, x, y):
        # diagonal up
        word = ''
        pos = (x,y)
        while pos[0] < self.sizeX and pos[1] < self.sizeY and pos[1] >= 0 and pos[0] >= 0:
            print(f"posdd: {pos}")
            word += self.getLetter(pos[0],pos[1])
            print(word)
            if word in self.dict:
                self.addWord(word, pos)
                print("^ word added!")
            pos = (pos[0]+1,pos[1])
            pos = (pos[0],pos[1]+1)

    def findAllWordsFromCoord(self, x, y):
        self.findWordsFromCoordHorizontal(x, y)
        self.findWordsFromCoordVertical(x, y)
        self.findWordsFromCoordDiagUp(x, y)
        self.findWordsFromCoordDiagDown(x, y)

    def findAllWords(self):
        for x in range(self.sizeX-1):
            for y in range(self.sizeY-1):
                self.findAllWordsFromCoord(x, y)

    def printFoundWords(self):
        words = self.foundWords
        for word in words:
            print(f"Found word: {word[0]} starting at {word[1]}")
        print(f"{len(words)} words found!")

    def __str__(self):
        out = "\n"
        letters = self.letters
        for x in letters:
            for y in x:
                out += f" {y}"
            out += "\n"
        return out

if __name__ == "__main__":
    test = Board("board1.txt", 14, 8)
    test.loadBoard()
    print(test)
    test.loadDict("dict.txt")
    test.findAllWords()
    test.printFoundWords()
