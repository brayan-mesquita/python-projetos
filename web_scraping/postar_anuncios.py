from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

driver = webdriver.Chrome(ChromeDriverManager().install())

# file_url = 'http://servicos.contabilidade.ro.gov.br:8080/'
#checar se online antes de acesso
#get password
EMAIL = 'brayanmesquita@gmail.com'
def password():
    with open('/Users/brayan/Documents/projetos/projetos_python/web_scraping/token') as password:
        senha = password.read()
    return senha

class Facebook:
    def __init__(self, driver):
        self.driver = driver
    def fazer_login(self):
        try:
            url_login = 'https://www.facebook.com/login/'
            self.driver.get(url_login)
            self.driver.find_element(By.NAME, "email").send_keys(EMAIL)
            self.driver.find_element(By.NAME, "pass").send_keys(password())
            self.driver.find_element(By.NAME, "login").click()
        except:
            print('Deu ruim!')
    def postar_anuncio(self):
        self.driver.get("https://www.facebook.com/marketplace/?ref=app_tab")
fb = Facebook(driver)
fb.fazer_login()
fb.postar_anuncio()





driver.get('https://conta.olx.com.br/acesso')
email = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/input")
email.send_keys(EMAIL)
senha = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[1]/div[2]/form/div[2]/div[2]/div/div/input")
senha.send_keys(password())
driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[1]/div[2]/form/button").click()

class Olx(): 
    def __init__(self, driver):
        self.driver = driver
    def fazer_login(self):
        pass
    def postar_anuncio(self):
        pass
