import unittest

from iMidiaTV7.testes.test_Login_imidia_PDV import test_realiza_login
from iMidiaTV7.testes.test_UploadMidias_PDV import test_UploadMidia
from iMidiaTV7.testes.test_InsercaoDinamica import test_Agendar
from iMidiaTV7.testes.test_ReagendamentoInsercaoDinamica import test_reagendamento_remocao

class test_reagendamento(unittest.TestCase):
    def reagendamento(self):
        self.assertEqual(test_realiza_login(), True)
        self.assertEqual(test_UploadMidia(), True)
        self.assertEqual(test_Agendar(), True)
        self.assertEqual(test_reagendamento_remocao(), True)


if __name__ == '__main__':
    unittest.main()
