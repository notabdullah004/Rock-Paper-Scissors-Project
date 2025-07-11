import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS_player import player, update

# Wrap player to track opponent history
def wrapped(opponent):
    def f():
        move = player()
        return move
    return f

class UnitTests(unittest.TestCase):
    def test_against_quincy(self):
        def p():
            return player()
        def o():
            m = quincy()
            update(m)
            return m
        self.assertTrue(play(p, o, rounds=1000) >= 60)

    # Repeat for abbey, kris, mrugesh ...

if __name__ == "__main__":
    unittest.main()
