# Importa a biblioteca de testes do Python.
import unittest

# Importa o módulo que contém a função de conversão.
import numeroromano as nr


# Cria a classe responsável pelos testes.
class TesteNumeroRomano(unittest.TestCase):

    # Testa o numeral romano I.
    def test_numero_I(self):
        self.assertEqual(nr.converte('I'), 1)

    # Testa o numeral romano V.
    def test_numero_V(self):
        self.assertEqual(nr.converte('V'), 5)

    # Testa o numeral romano II.
    def test_numero_II(self):
        self.assertEqual(nr.converte('II'), 2)

    # Testa o numeral romano XXII.
    def test_numero_XXII(self):
        self.assertEqual(nr.converte('XXII'), 22)

    # Testa o numeral romano IX.
    def test_numero_IX(self):
        self.assertEqual(nr.converte('IX'), 9)

    # Testa o numeral romano XXIV.
    def test_numero_XXIV(self):
        self.assertEqual(nr.converte('XXIV'), 24)


# Executa os testes quando o arquivo é iniciado diretamente.
if __name__ == '__main__':
    unittest.main()