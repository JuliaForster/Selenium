import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from iMidiaTV7.utilities.driver_chrome import driver, logging


class Encontra_elementos_home():
    def __init__(self):
        assert isinstance(driver, object)
        self.driver = driver

    def pop_up_cookies(self):
        while True:
            while True:
                try:
                    element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Prosseguir')
                    action = ActionChains(driver)
                    action.double_click(on_element=element)
                    action.perform()
                    logging.info('SCRIPT DE LOGIN: Botão Prosseguir foi clicado')
                    break
                except:
                    time.sleep(7)

    def login_botao(self):
        while True:
            while True:
                try:
                    driver.find_element(By.LINK_TEXT, "Login").click()
                    break
                except:
                    raise

    def agende_uma_demo(self):
        while True:
            try:
                botao_demo_home = driver.find_element(By.LINK_TEXT, 'AGENDE UMA DEMO')
                logging.info("HOMEPAGE - Botão para agendar demonstração no banner inicial consultado e encontrado")
                return botao_demo_home
                break
            except:
                logging.info(
                    "HOMEPAGE - Botão para agendar demonstração no banner inicial consultado e não foi encontrado")

    def logo_imidia(self):
        while True:
            try:
                logo_pixmidia_home = driver.find_element(By.CSS_SELECTOR,
                                                         '[class] #header:nth-of-type(1) .attachment-full')
                logging.info("HOMEPAGE - Logo da Pix Midia consultado e encontrado")
                return botao_demo_home
                break
            except:
                logging.info("HOMEPAGE - Logo da Pix Midia consultado e não foi encontrado")

    def menu_imidiatv(self):
        while True:
            try:
                botao_imidiatv = driver.find_element(By.LINK_TEXT, 'AGENDE UMA DEMO')
                logging.info("HOMEPAGE - Botão para agendar demonstração no banner inicial consultado e encontrado")
                return botao_imidiatv
                break
            except:
                logging.info("HOMEPAGE - Botão para agendar demonstração no banner inicial consultado e encontrado")

    def menu_imidiaApp(self):
        while True:
            try:
                botao_imidiaapp = driver.find_element(By.LINK_TEXT, 'AGENDE UMA DEMO')
                print("Link de AGENDE UMA DEMO encontrado")
                return botao_imidiaapp
                break
            except:
                print("Link de AGENDE UMA DEMO nao encontrado")

    def menu_conteudo(self):
        while True:
            try:
                botao_demo_home = driver.find_element(By.LINK_TEXT, 'AGENDE UMA DEMO')
                print("Link de AGENDE UMA DEMO encontrado")
                return botao_demo_home
                break
            except:
                print("Link de AGENDE UMA DEMO nao encontrado")

    def menu_sobre(self):
        while True:
            try:
                botao_demo_home = driver.find_element(By.LINK_TEXT, 'AGENDE UMA DEMO')
                print("Link de AGENDE UMA DEMO encontrado")
                return botao_demo_home
                break
            except:
                print("Link de AGENDE UMA DEMO nao encontrado")

    def menu_login(self):
        while True:
            try:
                botao_demo_home = driver.find_element(By.LINK_TEXT, 'AGENDE UMA DEMO')
                print("Link de AGENDE UMA DEMO encontrado")
                return botao_demo_home
                break
            except:
                print("Link de AGENDE UMA DEMO nao encontrado")

    def menu_agende_uma_demo(self):
        while True:
            try:
                botao_demo_home = driver.find_element(By.LINK_TEXT, 'AGENDE UMA DEMO')
                print("Link de AGENDE UMA DEMO encontrado")
                return botao_demo_home
                break
            except:
                print("Link de AGENDE UMA DEMO nao encontrado")
