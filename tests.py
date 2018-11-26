import unittest
from board import *

class TestBoardMethods(unittest.TestCase):

    def test_loadBoard(self):
        board = Board("board1.txt", 14, 8)
        board.loadBoard()
        self.assertEqual(f"{board}",
"""
 L B A G S F L Y F R E E S D
 O W V K L N U G L R Z M I C
 W I N T E R N A T I O N A L
 F R A S A J A N B U Y V O Z
 A W U V K Z X B S U C D G A
 R A P I D R E W A R D S K X
 E T I O A F F G H S R Y T A
 S N O C H A N G E F E E S A
""")
    def test_getLetter(self):
        board = Board("board1.txt", 14, 8)
        board.loadBoard()
        self.assertEqual(board.getLetter(0,0), "L")
        self.assertEqual(board.getLetter(13,7), "A")
        self.assertEqual(board.getLetter(8,3), "B")

    def test_addWord(self):
        board = Board("board1.txt", 14, 8)
        board.addWord("test", (0,0))
        self.assertEqual(board.foundWords, [("test", (0,0))])
        board.addWord("yeet", (8,7))
        self.assertEqual(board.foundWords, [("test", (0,0)),("yeet", (8,7))])

    def test_loadDict(self):
        board = Board("board1.txt", 14, 8)
        board.loadDict("testdict.txt")
        self.assertEqual(board.dict, ['STPV', "B", "BAG", "APPLE", "BANANA", "ORANGE", "PINEAPPLE"])

    def test_findWordsFromCoordHorizontal(self):
        board = Board("board1.txt", 14, 8)
        board.loadBoard()
        board.loadDict("testdict.txt")
        board.findWordsFromCoordHorizontal(1,0)
        self.assertEqual(board.foundWords, [('B', (1, 0)), ('BAG', (3, 0))])
    def test_findWordsFromCoordVertical(self):
        board = Board("board1.txt", 14, 8)
        board.loadBoard()
        board.loadDict("dict.txt")
        board.findWordsFromCoordVertical(4,1)
        self.assertEqual(board.foundWords, [('LEA', (4, 3)), ('LEAK', (4, 4))])
    def test_findWordsFromCoordDiagUp(self):
        board = Board("board1.txt", 14, 8)
        board.loadBoard()
        board.loadDict("testdict.txt")
        board.findWordsFromCoordVertical(0,7)
        self.assertEqual(board.foundWords, [('STPV', (0, 7))])

if __name__ == "__main__":
    unittest.main()
