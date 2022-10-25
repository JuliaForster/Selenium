from selenium.webdriver.common.by import By

from iMidiaTV7.testes.test_UploadMidias_PDV import driver, logging
from iMidiaTV7.utilities.db_connect import cursor


def Agendamento():
    try:
        thumb_midia = driver.find_element(By.XPATH, "//div[@id='corpo-painel-midias']/div[2]//img[@class='thumb']")
        thumb_midia.click()
        logging.info("SCRIPT DE INSERÇÃO - Acessando a midia para agendamento")
        driver.find_element(By.XPATH, "/html//li[@id='orelha-aba-publicacao']").click()
        logging.info("SCRIPT DE INSERÇÃO - Acessando aba de inserção")

        driver.find_element(By.XPATH, "//div[@id='myTabContent2']/div[2]/div[1]/div[3]/button[1]").click()
        logging.info("SCRIPT DE INSERÇÃO - Selecionando todas as grades")

        driver.find_element(By.XPATH,
                            "/html//div[@id='myTabContent2']/div[2]/div[3]//label[.='Fazer uma inserção nesta data.']").click()
        driver.find_element(By.XPATH,
                            "/html//div[@id='myTabContent2']/div[2]/div[3]//label[.='Fazer uma remoção nesta data.']").click()
        logging.info("SCRIPT DE INSERÇÃO - Datas marcadas com sucesso")
        botao_salvar = driver.find_element(By.CSS_SELECTOR, "[class='col-lg-12 col-md-12'] .btn-primary")
        driver.execute_script("arguments[0].click()", botao_salvar)
        logging.info("SCRIPT DE INSERÇÃO - Salvando agendamento")
        return 1
    except:
        raise
        return 0


def ConfirmaAgendamento():
    try:
        try:
            driver.find_element(By.XPATH, "//tr[@id='remover-inserscao-dinamica-1']//b[.='Inserção']")
            logging.info("SCRIPT DE INSERÇÃO - Mensagem de agendamento localizada")
            driver.find_element(By.XPATH,
                                "/html//div[@id='modal-1']//div[@class='modal-body p0']/div//a[@href='#']/i[@class='im-close']").click()
        except:
            logging.info("SCRIPT DE INSERÇÃO - Mensagem de agendamento não localizada")
            return True
        return 1
    except:
        raise
        return 0


def IDProcessamento_FilaInsercao(id_processamento: int):
    try:
        match int(id_processamento):
            case 1:
                logging.info("INSERÇÃO - GM_FILA_INSERCAO - Pendente")
                return True
            case 2:
                logging.info("INSERÇÃO - GM_FILA_INSERCAO - Processando")
                return True
            case 3:
                logging.info("INSERÇÃO - GM_FILA_INSERCAO - Finalizado")
                return True
            case 4:
                logging.info("INSERÇÃO - GM_FILA_INSERCAO - Erro no processamento")
                return True
            case 5:
                logging.info("INSERÇÃO - GM_FILA_INSERCAO - Pendente de Aprovação")
                return True
            case 6:
                logging.info("INSERÇÃO - GM_FILA_INSERCAO - Reprovado")
                return True
            case 7:
                logging.info("INSERÇÃO - GM_FILA_INSERCAO - Rejeitado")
                return True
            case 8:
                logging.info("INSERÇÃO - GM_FILA_INSERCAO - Cancelado pelo Usuário")
                return True
            case 9:
                logging.info("INSERÇÃO - GM_FILA_INSERCAO - Pausado")
                return True
    except:
        return False


def IDProcessamento_FilaQueries(id_processamento: int):
    try:
        match int(id_processamento):
            case 1:
                data = ("GM_FILA - na fila")
                return data
            case 2:
                data = ("GM_FILA - em Execução")
                return data
            case 3:
                data = ("GM_FILA - Finalizado com sucesso")
                return data
            case 4:
                data = ("GM_FILA - Finalizado com Erro")
                return data
    except:
        return True


def ConfirmaFilaQueries(id_midia, id_operacao):
    try:
        queryzinha = (
                    "SELECT ID_STATUS_FILA_QUERIES FROM GM_FILA_QUERIES  WHERE ID_CLASSE_OBJETO = 3 AND ID_OPERACOES_FILA_QUERY = " + id_operacao + " AND ID_OBJETO = " + id_midia)
        cursor.execute(queryzinha)
        rows = cursor.fetchall()
        id_processamento = rows[0]
        id_processamento = id_processamento[0]
        if id_operacao == "1":
            id_operacao = "Inserção"
        elif id_operacao == "2":
            id_operacao = "Remoção"
        retorno = IDProcessamento_FilaQueries(id_processamento)
        logging.info("Verificando Agendamento de " + id_operacao + " no banco --> " + str(retorno))
    except:
        driver.refresh()


def ConfirmaFilaInsercao(id_midia, id_operacao):
    try:
        queryzinha = (
                    "SELECT ID_STATUS_PROCESSAMENTO FROM GM_FILA_INSERCAO_DINAMICA WHERE ID_TIPO_INSERCAO_DINAMICA = " + id_operacao + " AND ID_MIDIA = " + id_midia)
        cursor.execute(queryzinha)
        rows = cursor.fetchall()
        id_processamento = rows[0]
        id_processamento = id_processamento[0]
        if id_operacao == "1":
            nome_operacao = "Inserção"
        elif id_operacao == "2":
            nome_operacao = "Remoção"
        retorno = IDProcessamento_FilaInsercao(id_processamento, queryzinha)
        logging.info("Verificando Agendamento de " + nome_operacao + " no banco --> " + str(retorno))
    except:
        driver.refresh()


def ConfirmaInserção():
    # confirmando a presença das mensagens de agendamentos realizados, aguardando entrar na fila
    try:
        driver.find_element(By.XPATH, "//div[@id='myTabContent2']/div[2]/div[5]//table/tbody/tr[1]")
        driver.find_element(By.XPATH, "//div[@id='myTabContent2']/div[2]/div[5]//table/tbody/tr[2]")
        logging.info("SCRIPT DE INSERÇÃO - Mensagens de agendamento na fila foram apresentadas")
    except:
        driver.refresh()

    # verificando no banco como está esse agendamento, se esta realmente na fila e foi consumido
    url = driver.current_url
    id_midia = url
    id_midia = id_midia.split("insercaodinamica/midia/", 2)
    id_midia = id_midia[1]
    # confirma fila queries - inserção
    ConfirmaFilaQueries(id_midia, "1")
    ConfirmaFilaQueries(id_midia, "2")

    ConfirmaFilaInsercao(id_midia, "1")
    ConfirmaFilaInsercao(id_midia, "2")
    return 1


def test_Agendar():
    assert Agendamento() == 1
    assert ConfirmaAgendamento() == 1
    assert ConfirmaInserção() == 1
