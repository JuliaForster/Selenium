from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from iMidiaTV7.testes import test_Login_imidia_campanha
from utilities import links_acesso as links
from utilities.db_connect import cursor

logging = test_Login_imidia_campanha.logging
driver = test_Login_imidia_campanha.driver
adicionar_midia: str = links.adicionar_midia

def UploadMidias():
    test_Login_imidia_campanha.logging.info("SCRIPT DE UPLOAD DE MIDIAS")
    # fazer o upload de uma mídia de vídeo para testar o processamento
    test_Login_imidia_campanha.driver.get(links.adicionar_midia)
    botao = test_Login_imidia_campanha.driver.find_element(By.XPATH, '//input[@id="upload-file-name"]')
    test_Login_imidia_campanha.logging.info("Acessando a pagina para subir midia")

    File_Path = 'C:\\Users\\pixmi\\workspace_python\\SeleniumWDTutorial\\iMidiaTV7\\teste-upload-video-1.mp4'

    botao.send_keys(File_Path)
    test_Login_imidia_campanha.driver.find_element(By.XPATH, "//form[@id='form-upload-midia']//button[@type='submit']").click()
    test_Login_imidia_campanha.logging.info("Upload realizado com sucesso")
    return 0


def VerificaProcessado():
    # verifica se o vídeo que subiu não está corrompido
    test_Login_imidia_campanha.logging.info("SCRIPT DE UPLOAD - Verificar Processamento")
    try:
        while True:
            try:
                corpo_thumb = test_Login_imidia_campanha.driver.find_element(By.XPATH,
                                                                    "//div[@id='corpo-painel-midias']/div[2]//img[@class='thumb']")
                test_Login_imidia_campanha.logging.info("Midia saiu do processamento")
                break
            except:
                test_Login_imidia_campanha.driver.refresh

        link_thumb = corpo_thumb.get_attribute('src')
        link_midia = str(link_thumb).rstrip("-THUMB.jpg")
        link_midia = link_midia + ".mp4"
        driver2 = test_Login_imidia_campanha.driver
        driver2.get(link_midia)
        try:
            # acessando o arquivo do video que está hospedado no nosso site e verificando se retorna uma tela de erro
            driver2.find_element(By.CSS_SELECTOR, "div#folder0 > div:nth-of-type(1) > .html-tag")
            test_Login_imidia_campanha.logging.info("Acessando arquivo de midia")
        except NoSuchElementException:
            # se não trouxer erro ou exceções, irá voltar para a página de midias do imidiatv
            test_Login_imidia_campanha.logging.info("Processamento realizado com sucesso")
            test_Login_imidia_campanha.driver.get(links.minhas_midias)
        return 1
    except:
        raise
        return 0


def ExcluirMidia():
    try:
        # após todas as validações, a mídia será excluída para que na próxima validação não tenha erros ao encontrar as PATH
        test_Login_imidia_campanha.driver.find_element(By.XPATH,
                                              "/html//div[@id='content']//div[@class='col-lg-8 col-md-8 col-sm-9 col-xs-12']//div[@class='col-md-12']/div[3]/a[@href='/midia']//i[@class='im-film3']").click()
        test_Login_imidia_campanha.logging.info("SCRIPT DE UPLOAD - Verificar se há midias para excluir")
        # verificar se há midia na primeira posição:
        try:
            id_midia = test_Login_imidia_campanha.driver.find_element(By.XPATH,
                                                             '//div[@id="corpo-painel-midias"]/div[2]/a[@class="link-midia-file"]')
        except:
            id_midia = None
        # se existe midia, vai trabalhar ela
        if id_midia:
            id_midia = str(id_midia.get_attribute('href')).strip(links.local_midia)
            test_Login_imidia_campanha.logging.info("Existe uma midia na pasta")
            query = "SELECT ID_GRADE_PROGRAMACAO FROM GM_GRADE_PROGRAMACAO_MIDIA WHERE ID_MIDIA = " + id_midia
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                test_Login_imidia_campanha.driver.find_element(By.XPATH,
                                                      "//div[@id='corpo-painel-midias']/div[2]//img[@class='thumb']").click()
                # clicando no botao remover de todas as grades
                remover_botao = test_Login_imidia_campanha.driver.find_elements(By.CSS_SELECTOR, ".btn.btn-default.btn-sm")
                acao = ActionChains(test_Login_imidia_campanha.driver)
                acao.double_click(on_element=remover_botao[0])
                acao.perform()
                test_Login_imidia_campanha.logging.info("Clicando no botão de remover de todas as grades")

                # aceitando o alert
                alert = Alert(test_Login_imidia_campanha.driver)
                alert.accept()
                test_Login_imidia_campanha.logging.info("Alert confirmado")

                test_Login_imidia_campanha.driver.get(links.minhas_midias)
            try:
                test_Login_imidia_campanha.driver.find_element(By.XPATH,
                                                      "//div[@id='corpo-painel-midias']/div[2]/input[@type='checkbox']")
                test_Login_imidia_campanha.driver.find_element(By.XPATH, "//div[@id='menu-selecao']/button[@type='button']").click()
                test_Login_imidia_campanha.driver.find_element(By.XPATH, "/html//a[@id='chk-selecionar-todos']").click()
                test_Login_imidia_campanha.driver.find_element(By.XPATH, "//div[@id='menu-selecao']/button[@type='button']").click()
                test_Login_imidia_campanha.driver.find_element(By.XPATH, "//a[@id='btn-excluir-midias-selecionadas']").click()
                alert = Alert(test_Login_imidia_campanha.driver)
                alert.accept()
            except:
                test_Login_imidia_campanha.logging.info("SCRIPT DE UPLOAD - não há midias nesta pasta")
            while True:
                try:
                    test_Login_imidia_campanha.driver.find_element(By.XPATH,
                                                          "//div[@id='corpo-painel-midias']/div[2]/input[@type='checkbox']")
                    test_Login_imidia_campanha.driver.find_element(By.XPATH,
                                                          "//div[@id='menu-selecao']/button[@type='button']").click()
                    test_Login_imidia_campanha.driver.find_element(By.XPATH, "/html//a[@id='chk-selecionar-todos']").click()
                    test_Login_imidia_campanha.driver.find_element(By.XPATH,
                                                          "//div[@id='menu-selecao']/button[@type='button']").click()
                    test_Login_imidia_campanha.driver.find_element(By.XPATH, "//a[@id='btn-excluir-midias-selecionadas']").click()
                    alert = Alert(test_Login_imidia_campanha.driver)
                    alert.accept()
                    break
                except:
                    test_Login_imidia_campanha.logging.info("SCRIPT DE UPLOAD - não há midias nesta pasta")
        # se não existe, vai encerrar
        else:
            test_Login_imidia_campanha.logging.info("Não há midia para excluir")
        return 0
    except:
        return 1

def test_UploadMidia():
    assert ExcluirMidia() == 0
    assert UploadMidias() == 0
    assert VerificaProcessado() == 1
