#login.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

def iniciar_driver():
      opcoes = Options()
      arguments = ['--lang=pt-BR', '--window-size=800,800', '--incognito']

      for argument in arguments:
            opcoes.add_argument(argument)

      driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=opcoes)

      return driver

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')

botao_Login = driver.find_element(By.XPATH, '//*[@id="navbarsExample04"]/ul[2]/li[3]/a')
botao_Login.click()
sleep(1)

email = driver.find_element(By.XPATH, "//*[@id='email']")
email.send_keys('teste@test.com')
sleep(1)

senha = driver.find_element(By.XPATH, "//*[@id='senha']") 
senha.send_keys('123456')
sleep(1)

botao_Enviar = driver.find_element(By.XPATH, '/html/body/section/form/div/button')
botao_Enviar.click()

print(' ')
input('ENTER PARA SAIR ....')
driver.close()