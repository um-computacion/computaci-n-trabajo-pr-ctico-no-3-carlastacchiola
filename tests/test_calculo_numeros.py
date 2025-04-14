import unittest
from unittest.mock import patch

from src.calculo_numeros import ingrese_numero
from src.exceptions import NumeroDebeSerPositivo

class TestCalculoNumeros(unittest.TestCase):

    @patch('builtins.input', return_value='70')
    def test_ingreso_correcto(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 70)

    @patch('builtins.input', return_value='-70')
    def test_ingreso_incorrecto(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='CCC')
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()
