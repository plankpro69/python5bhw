import unittest
from poker_ueberarbeitet1 import get_wert, get_farbe, ein_paar, drilling, strasse

class TestPokerFunctions(unittest.TestCase):
    def setUp(self):
        self.karten_pro_farbe = 13

    def test_get_wert(self):
        self.assertEqual(get_wert(0, self.karten_pro_farbe), 0)
        self.assertEqual(get_wert(13, self.karten_pro_farbe), 0)
        self.assertEqual(get_wert(51, self.karten_pro_farbe), 12)

    def test_get_farbe(self):
        self.assertEqual(get_farbe(0, self.karten_pro_farbe), 0)
        self.assertEqual(get_farbe(13, self.karten_pro_farbe), 1)
        self.assertEqual(get_farbe(51, self.karten_pro_farbe), 3)

    def test_ein_paar(self):
        karten = [0, 13, 1, 2, 3]  # Ass in zwei verschiedenen Farben
        self.assertTrue(ein_paar(karten, self.karten_pro_farbe))

        karten = [0, 1, 2, 3, 4]   # Kein Paar
        self.assertFalse(ein_paar(karten, self.karten_pro_farbe))

    def test_drilling(self):
        karten = [0, 13, 26, 1, 2]  # Drilling Ass
        self.assertTrue(drilling(karten, self.karten_pro_farbe))

        karten = [0, 1, 2, 3, 4]    # Kein Drilling
        self.assertFalse(drilling(karten, self.karten_pro_farbe))

    def test_strasse(self):
        karten = [0, 1, 2, 3, 4]    # Straße
        self.assertTrue(strasse(karten, self.karten_pro_farbe))

        karten = [0, 1, 2, 3, 5]    # Keine Straße
        self.assertFalse(strasse(karten, self.karten_pro_farbe))


if __name__ == "__main__":
    unittest.main()