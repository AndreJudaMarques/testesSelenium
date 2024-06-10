#login.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

def iniciar_driver():
      opcoes = Options()
      arguments = ['--lang=pt-BR', '--window-size=900,900', '--incognito']

      for argument in arguments:
            opcoes.add_argument(argument)

      driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=opcoes)

      return driver

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(2)

campo_dados = driver.find_element(By.XPATH, "//*[@id='dadosusuario']")
campo_dados.click()
campo_dados.send_keys('Andre Judá Pythonista')
sleep(1)

botao_cliqueAqui = driver.find_element(By.XPATH, "//*[@id='desafio2']")
botao_cliqueAqui.click()

print(' ')
input('ENTER PARA SAIR ....')
driver.close()