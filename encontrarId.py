from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def iniciar_driver():
      opcoes = Options()
      arguments = ['--lang=pt-BR', '--window-size=500,500', '--incognito']

      for argument in arguments:
            opcoes.add_argument(argument)

      driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=opcoes)

      return driver

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')

#encontrar elementos por id

botaoAlerta = driver.find_element(By.ID, 'buttonalerta')
botoes = driver.find_elements(By.ID, 'buttonalerta')
if botaoAlerta is not None:
      print('botao encontrado')
if botoes is not None:
      print('botoes encontrados')



input('')
driver.close()