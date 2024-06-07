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


# encontrar elementos por name
seuNome = driver.find_element(By.NAME, 'seu-nome')
examples = driver.find_elements(By.NAME, 'exampleRadios')
if seuNome is not None:
      print('achei o campo')
if examples is not None:
      print('achei os examples')


input('')
driver.close()