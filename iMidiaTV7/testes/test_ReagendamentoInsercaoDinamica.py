import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from iMidiaTV7.testes.test_InsercaoDinamica import driver, logging
from iMidiaTV7.utilities.db_connect import cursor, conn


def SelecionaAgendamentoExistente():
    try:
        for i in range(0, 10):
            try:
                driver.implicitly_wait(10)
                botaoreagendamento = driver.find_element(By.XPATH,
                                                         '//*[@id="remover-inserscao-dinamica-2"]/td[5]/div/button[1]')
                reagendarbtn = ActionChains(driver)
                reagendarbtn.click(on_element=botaoreagendamento)
                reagendarbtn.perform()
                logging.info("botão de reagendamento encontrado")
                i = 10
                return 1
            except NoSuchElementException:
                time.sleep(10)
                driver.refresh()
    except:
        return 0


def VerificaDataAgendada(id_midia):
    time.sleep(15)
    conn.reset_session()
    query = 'SELECT * FROM GM_FILA_INSERCAO_DINAMICA WHERE ID_TIPO_INSERCAO_DINAMICA = 2 AND ID_USUARIO = 1050 ORDER BY DT_CREATED DESC'
    cursor.execute(query)
    rows = cursor.fetchall()
    rows = rows[0]
    # 3126147
    id_midia_consulta = int(rows[5])
    data = rows[13]
    if id_midia_consulta == int(id_midia):
        return data
    else:
        return ("Problema ao checar id da midia na fila " + str(id_midia_consulta))


# setar data/hora atual no modal de data/hora
def DefinirNovaData():
    counter = 0
    while counter < 12:
        try:
            id_midia = driver.current_url
            id_midia = id_midia.strip("https://imidiatv.com.br/midia/insercaodinamica/midia/")
            data_anterior = VerificaDataAgendada(id_midia)
            driver.find_element(By.XPATH, "/html//input[@id='data-reagendamento-insercao-dinamica']").click()
            DT_HR_ATUAL = driver.find_element(By.CSS_SELECTOR, "[data-handler='today']")
            DT_HR_ATUAL.click()
            sliders = driver.find_elements(By.CLASS_NAME, "ui-slider-handle")
            slider_min = sliders[1]
            move_ponteiro = ActionChains(driver)
            move_ponteiro.click_and_hold(slider_min).move_by_offset(50, 0).release().perform()

            botao_ok = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[3]/button[2]')
            botao_ok.click()

            botao_salvar = driver.find_element(By.CSS_SELECTOR, "#btn-salvar-player")
            driver.execute_script("arguments[0].click()", botao_salvar)
            break
        except:
            counter = counter + 1
            print(counter)
            driver.refresh()
    return data_anterior


# validar se a alteração gerou uma mensagem de sucesso
def ConferirMensagemSucesso():
    data_anterior = DefinirNovaData()
    id_midia = driver.current_url
    id_midia = id_midia.strip("https://imidiatv.com.br/midia/insercaodinamica/midia/")
    driver.implicitly_wait(10)
    time.sleep(5)
    real = driver.find_element(By.XPATH, "//div[@id='modal-default-feedback-panel-body']//div[@class='panel-body']")
    texto = real.text
    texto = texto.split('\n')
    if texto[0] == 'Data do agendamento alterada com sucesso!':
        nova_data = VerificaDataAgendada(id_midia)
        if nova_data != data_anterior:
            return 1
        else:
            print(nova_data)
            print(data_anterior)
            return 0
    else:
        return 0


def Encerra():
    driver.quit()


def test_reagendamento_remocao():
    assert SelecionaAgendamentoExistente() == 1
    assert ConferirMensagemSucesso() == 1
    Encerra()

# validar se realmente a data e hora foram alteradas no banco de dados
#    def ConferirNovaInfoNaFila(self):


# validar se o pedido de inserção/remoção chegou nas grades
#    def ValidarExecucaoQueries(self):


# validar se o pedido de inserção/remoção chegou nos players
#    def ValidarAtualizaçãoPlayers(self):
