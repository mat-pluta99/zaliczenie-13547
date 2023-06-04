import unittest
from blackjack import round


class TestRound(unittest.TestCase):
    def test_round(self):
        wynik = round()
        self.assertTrue(wynik)


if __name__ == "__main__":
    unittest.main()
