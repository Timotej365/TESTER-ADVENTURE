import sys
sys.path.append('C:/Users/timot/Desktop/subory do portfolia/tester adventure')
import unittest
from unittest.mock import patch
from tester_adventure import hadanka_otazka  # Importujeme funkciu zo súboru tester_adventure.py

class TestHadankaOtazka(unittest.TestCase):
    
    @patch('random.choice')  # Mockujeme random.choice, aby sme dostali vždy rovnakú otázku
    @patch('builtins.input')  # Mockujeme input, aby sme nemuseli manuálne zadávať odpoveď
    def test_spravna_odpoved(self, mock_input, mock_random_choice):
        # Nastavíme mock pre výber otázky
        mock_random_choice.return_value = {"otazka": "Aký typ testovania vykonáva používateľ? (funkcne, regresne, akceptacne)", "odpoved": "akceptacne"}
        
        # Mockujeme input, aby vrátil správnu odpoveď
        mock_input.return_value = "akceptacne"
        
        # Testujeme, že správna odpoveď vráti True
        result = hadanka_otazka()  # Voláme reálnu funkciu z tester_adventure.py
        self.assertTrue(result)  # Malo by to vrátiť True, keď je odpoveď správna

    @patch('random.choice')  # Mockujeme random.choice, aby sme dostali vždy rovnakú otázku
    @patch('builtins.input')  # Mockujeme input, aby sme nemuseli manuálne zadávať odpoveď
    def test_nespravna_odpoved(self, mock_input, mock_random_choice):
        # Nastavíme mock pre výber otázky
        mock_random_choice.return_value = {"otazka": "Aký typ testovania vykonáva používateľ? (funkcne, regresne, akceptacne)", "odpoved": "akceptacne"}
        
        # Mockujeme input, aby vrátil nesprávnu odpoveď
        mock_input.return_value = "funkcne"
        
        # Testujeme, že nesprávna odpoveď vráti False
        result = hadanka_otazka()  # Voláme reálnu funkciu z tester_adventure.py
        self.assertFalse(result)  # Malo by to vrátiť False, keď je odpoveď nesprávna

if __name__ == '__main__':
    unittest.main()
