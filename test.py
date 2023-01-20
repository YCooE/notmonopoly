import unittest
from notmonopoly import game as game
from notmonopoly import rolls1 as r1
from notmonopoly import rolls2 as r2
import playerdef as p_init

class TestsNames(unittest.TestCase):
    def test_own_name(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]
        rolls = [1, 2, 3, 4, 4, 4, 4, 4]

        max_play1, max_val1, own_name1, own_stat1 = game(rolls, own_status, owner_name, locals(), p_list)
        self.assertEqual(own_name1, [None, 'Peter', 'Billy', 'Charlotte', 'Sweedal', 'Peter', 'Billy', 'Charlotte', 'Sweedal'], "should be one of each, twice")
    def test_own_stat(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]
        rolls = [1, 2, 3, 4, 4, 4, 4, 4]

        max_play1, max_val1, own_name1, own_stat1 = game(rolls, own_status, owner_name, locals(), p_list)
        self.assertEqual(own_stat1, [True] * 9, "should be all true")

    def test_own_winner(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]
        rolls = [1, 2, 3, 4, 4, 4, 4, 4]

        max_play1, max_val1, own_name1, own_stat1 = game(rolls, own_status, owner_name, locals(), p_list)
        self.assertEqual(max_play1, 'Peter', "should be Peter")

    def test_own_winner(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]
        rolls = [1, 2, 3, 4, 4, 4, 4, 4]

        max_play1, max_val1, own_name1, own_stat1 = game(rolls, own_status, owner_name, locals(), p_list)
        self.assertEqual(max_val1, 12, "should be 12, start 16-1 for first space, 15-3 for 5th pos")



    def test_rolls1_name(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]

        max_play1, max_val1, own_name1, own_stat1 = game(r1, own_status, owner_name, locals(), p_list)
        self.assertEqual(own_name1, [None, 'Peter', 'Peter', 'Billy', 'Peter', 'Billy', None, 'Peter', 'Peter'], "Peter buys everything")


    def test_rolls1_stat(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]

        max_play1, max_val1, own_name1, own_stat1 = game(r1, own_status, owner_name, locals(), p_list)
        self.assertEqual(own_stat1, [True, True, True, True, True, True, False, True, True], "All but one is true")

    def test_rolls1_winner(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]

        max_play1, max_val1, own_name1, own_stat1 = game(r1, own_status, owner_name, locals(), p_list)
        self.assertEqual(max_play1, 'Peter', "Peter wins by buying everything")

    def test_rolls1_max_score(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]

        max_play1, max_val1, own_name1, own_stat1 = game(r1, own_status, owner_name, locals(), p_list)
        self.assertEqual(max_val1, 40, "Highscore of 40")

    def test_rolls2_name(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]

        max_play1, max_val1, own_name1, own_stat1 = game(r2, own_status, owner_name, locals(), p_list)
        self.assertEqual(own_name1, [None, 'Sweedal', 'Billy', 'Billy', 'Charlotte', 'Peter', 'Billy', 'Billy', 'Charlotte'], "Billy buys everything")


    def test_rolls2_stat(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]

        max_play1, max_val1, own_name1, own_stat1 = game(r2, own_status, owner_name, locals(), p_list)
        self.assertEqual(own_stat1, [True] * 9, "Everything bought")


    def test_rolls2_winner(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]

        max_play1, max_val1, own_name1, own_stat1 = game(r2, own_status, owner_name, locals(), p_list)
        self.assertEqual(max_play1, 'Billy', "Billy wins with most properties")


    def test_rolls2_score(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]

        max_play1, max_val1, own_name1, own_stat1 = game(r2, own_status, owner_name, locals(), p_list)
        self.assertEqual(max_val1, 27, "High score of 27")

    def testGOfunctionality(self):
        own_status = [False] * 9
        own_status[0] = True
        owner_name = [None] * 9
        Peter = p_init.Player("Peter", 16, 0, [], False)
        Billy = p_init.Player("Billy", 16, 0, [], False)
        Charlotte = p_init.Player("Charlotte", 16, 0, [], False)
        Sweedal = p_init.Player("Sweedal", 16, 0, [], False)
        p_list = [Peter, Billy, Charlotte, Sweedal]
        rolls = [9, 9, 9, 9, 9, 9, 9, 9]

        max_play1, max_val1, own_name1, own_stat1 = game(rolls, own_status, owner_name, locals(), p_list)
        self.assertEqual(max_val1, 18, "Pass start twice get 18")
if __name__ == '__main__':
    unittest.main()