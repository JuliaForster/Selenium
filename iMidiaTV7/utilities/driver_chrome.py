import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from iMidiaTV7.utilities.links_acesso import *


logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

def abreoImidiatv():
    #pip install webdriver-manager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(home)
    return driver


# iniciar o browser
'''class criarDriver():

    def __init__(self):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "link_text":
            return By.LINK_TEXT
        else:
            print("cara, esse tipo de localizador nao é suportado")
        return False
'''
'''  def getElement(self, locator, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("element found")
        except:
            print("Elemento nao encontrado")

        return element

    def isElementPresent(self, locatorType):
        try:
            element = self.getElement(self, locatorType)
            if element is not None:
                self.log.info("element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            print("element not found")
            return False'''
