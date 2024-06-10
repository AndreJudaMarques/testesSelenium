# clicarSelenium.py

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

botao_Dropdown = driver.find_element(By.ID,'dropdownMenuButton')
botao_Dropdown.click()
#driver.execute_script('arguments[0].click()', botao_Dropdown) # 'CLICK COM SCRIPT JAVASCRIPT


print(' ')
input('ENTER PARA SAIR ....')
driver.close()