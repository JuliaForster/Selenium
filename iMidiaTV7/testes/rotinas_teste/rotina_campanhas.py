import unittest

from iMidiaTV7.testes.test_Login_imidia_campanha import test_realiza_login
from iMidiaTV7.testes.test_UploadMidias_campanha import test_UploadMidia
from iMidiaTV7.testes.test_criar_nova_campanha import test_criar_nova_campanha

class test_campanha(unittest.TestCase):
    def campanha_metodos(self):
        self.assertEqual(test_realiza_login(), True)
        self.assertEqual(test_UploadMidia(), True)
        self.assertEqual(test_criar_nova_campanha(), True)

if __name__ == '__main__':
    unittest.main()
