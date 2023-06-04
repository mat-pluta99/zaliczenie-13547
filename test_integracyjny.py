import unittest
from blackjack import round
from player import Player
from cards import Deck


class TestIntegracji(unittest.TestCase):
    def test_integracji_kart(self):
        talia = Deck()

        gracz = Player("Gracz")
        gracz.hit((talia.deck))
        ilosc = len(talia.deck)
        message = "Błąd: nie zgadza się ilość kart w talii"
        self.assertEqual(len((talia.deck)), 51, message)

    def test_integracji_rundy(self):
        gracz = Player("Gracz")
        dealer = Player("Dealer")
        talia = Deck()
        gracz.hit(talia.deck)
        dealer.hit(talia.deck)
        gracz.hit(talia.deck)
        reka_gracza = len(gracz.hand)
        reka_dealera = len(dealer.hand)
        message = "Błąd: dealer ma większą wartość kart"
        self.assertGreater(reka_gracza, reka_dealera, message)


if __name__ == "__main__":
    unittest.main()
