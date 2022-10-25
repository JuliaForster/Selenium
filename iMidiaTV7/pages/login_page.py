import logging

from selenium.webdriver.common.by import By

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

campo_email = driver.find_element(By.ID, "email")
campo_senha = driver.find_element(By.ID, "password")
botao_login = driver.find_element(By.XPATH, "//form[@id='login-form']//button[@class='btn btn-default pull-right']")
link_cadastro = driver.find_element(By.XPATH, "//form[@id='login-form']//a[@href='/cadastro']")
link_recuperacao_senha = driver.find_element(By.XPATH, "//a[@id='link-esqueci-minha-senha']")
container_page = driver.find_element(By.XPATH, "//div[@class='container-fluid']")
logo_link = driver.find_element(By.XPATH, "//div[@id='login']/a[@href='https://imidiatv.com.br/']")
logo_imagem = driver.find_element(By.XPATH, "/html//img[@id='logo']")


class encontra_elementos_login():
    def campo_email(self):
        while True:
            try:
                campo_email.send_keys("renanpixteste@emailna.co")
                print("campo email disponivel")
                break
            except:
                print("campo email nao disponivel")
                raise
                driver.refresh

    def campo_senha(self):
        while True:
            try:
                campo_senha.send_keys("door102030")
                print("campo senha disponivel")
                break
            except:
                print("campo senha indisponivel")
                raise
                driver.refresh

    def botao_login(self):
        while True:
            try:
                assert botao_login.click()
                print("botao Acessar disponivel")
                break
            except:
                print("botao Acessar indisponivel")
                raise
                driver.refresh

    def link_nao_tenho_cadastro(self):
        while True:
            try:
                assert link_cadastro.click()
                print("Link Não tenho cadastro disponivel")
                break
            except:
                print("Link Não tenho cadastro indisponivel")
                raise
                driver.refresh

    def link_esqueci_minha_senha(self):
        while True:
            try:
                assert link_recuperacao_senha.click()
                print("Link Esqueci minha senha disponivel")
                break
            except:
                print("Link Esqueci minha senhao indisponivel")
                raise
                driver.refresh

    def container_fluido(self):
        while True:
            try:
                assert container_page is not None
                print("Container disponivel")
                break
            except:
                print("Container indisponivel")
                raise
                driver.refresh

    def imagem_logo_imidia(self):
        while True:
            try:
                assert logo_imagem.click()
                assert logo_link.click()
                print("Logo imidiatv disponivel")
                break
            except:
                print("Logo imidiatv indisponivel")
                raise
                driver.refresh


encontra_elementos_login.botao_login('self')
encontra_elementos_login.link_nao_tenho_cadastro('self')
encontra_elementos_login.link_esqueci_minha_senha('self')
encontra_elementos_login.campo_email('self')
encontra_elementos_login.campo_senha('self')
encontra_elementos_login.container_fluido('self')
