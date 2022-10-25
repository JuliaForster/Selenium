from selenium import webdriver


class LoginTests():
    baseURL = "https://imidiatv.com.br/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
