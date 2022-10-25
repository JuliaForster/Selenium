from selenium.webdriver.common.action_chains import ActionChains
from utilities.driver_chrome import *
from utilities.links_acesso import *

driver = abreoImidiatv()
def encontrarbotao():
    try:
        element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Prosseguir')
        action = ActionChains(driver)
        action.double_click(on_element=element)
        action.perform()
        logging.info('SCRIPT DE LOGIN: Botão Prosseguir foi clicado')
        try:
            driver.find_element(By.LINK_TEXT, "Login").click()
            logging.info('SCRIPT DE LOGIN: Botão Prosseguir foi clicado')
        except:
            driver.refresh()
        return 1
    except:
        return 0


'''def realiza_Login_errado():
    handles = driver.window_handles
    for handle in handles:
        if handle not in parent:
            driver.switch_to.window(handle)
            try:
                driver.find_element(By.ID, "email").send_keys("renanpixteste@emailna.co")
                driver.find_element(By.ID, "password").send_keys("door102040")
                logging.info('SCRIPT DE LOGIN: Chaves incorretas de acesso enviadas')
            except:
                raise
                driver.refresh
            try:
                driver.find_element(By.PARTIAL_LINK_TEXT, "Usuário ou senha inválida!")
                driver.find_element(By.CLASS_NAME, "im-close").click()
                logging.info("SCRIPT DE LOGIN: Mensagem de erro apareceu e foi fechada")
                return 1
            except:
                logging.info("SCRIPT DE LOGIN: Não apareceu mensagem de erro")
                return 0

'''
def realiza_Login():
    handles = driver.window_handles
    try:
        driver.switch_to.window(handles[1])
        while True:
            try:
                driver.find_element(By.ID, "email").send_keys("thiago.ferrao@pixmidia.com.br")
                driver.find_element(By.ID, "password").send_keys("door102030")
                logging.info('SCRIPT DE LOGIN: Chaves corretas de acesso enviadas')
                break
            except:
                raise
                driver.refresh

        driver.find_element(By.XPATH, "//form[@id='login-form']//button[@class='btn btn-default pull-right']").click()
        logging.info('SCRIPT DE LOGIN: login realizado')
        return 1
    except:
        return 0


def test_realiza_login():
    assert encontrarbotao() == 1
    assert realiza_Login() == 1
