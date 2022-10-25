from selenium.webdriver.common.by import By
from iMidiaTV7.testes import test_Login_imidia_campanha
from selenium.webdriver.common.alert import Alert
from utilities import links_acesso as links
from utilities.db_connect import cursor

logging = test_Login_imidia_campanha.logging
driver = test_Login_imidia_campanha.driver

def acessar_pagina_campanhas():
    driver.get("https://imidiatv.com.br/dashboard")
    links_acesso = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/a[1]/h1[1]/i[1]")
    if links_acesso:
        links_acesso.click()
        return 0
    else:
        return 1

def verifica_retorno_cria_campanha(resposta_real, campo_inserido, resposta_esperada):
    resposta_alert = ["Favor escolher um cliente válido",
                      "Favor informar o nome da campanha",
                      "Favor escolher um executivo válido",
                      "Favor informar o número do pedido de inserção",
                      "Favor informar o número de telas contratadas",
                      "Favor informar o impacto estimado",
                      "Favor informar o número de inserções estimadas",
                      "Favor informar a data de início",
                      "Favor informar a data de finalização"]

    driver.find_element(By.XPATH, "//form[@id='form-campanha']//button[@type='submit']")
    alerta = driver.switch_to.alert
    alerta = alerta.text

def criar_nova_campanha():
    driver.find_element(By.XPATH, "//div[@id='content']/div[@class='content-wrapper']//a[@href='/campanha/criar']").click()

#campos a serem preenchidos:
    campo_nome = driver.find_element(By.XPATH, "//input[@id='nome_campanha']")
    campo_cliente = driver.find_element(By.XPATH, "//select[@id='select-cliente']")
    campo_executivo = driver.find_element(By.XPATH, "//select[@id='select-executivo']")
    campo_PI = driver.find_element(By.XPATH, "//input[@id='pedido_insercao']")
    campo_telas = driver.find_element(By.XPATH, "//input[@id='telas_contratadas']")
    campo_impacto = driver.find_element(By.XPATH, "//input[@id='impacto_estimado']")
    campo_insercoes = driver.find_element(By.XPATH, "//input[@id='insercoes_estimadas']")
    dt_inicio = driver.find_element(By.XPATH, "//input[@id='data_inicio']")
    dt_fim = driver.find_element(By.XPATH, "//input[@id='data_fim']")
    segmento = driver.find_element(By.XPATH, "//select[@id='id-setor-mercado']")
    novo_email = driver.find_element(By.XPATH, "//input[@id='emailLista']")
#submit
    driver.find_element(By.XPATH, "//form[@id='form-campanha']//button[@type='submit']")


def test_criar_nova_campanha():
    assert acessar_pagina_campanhas() == 0
    assert criar_nova_campanha() == 0