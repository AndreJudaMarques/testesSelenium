#desafio1.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def iniciar_driver():
      Opcoes_Chrome = Options()
      arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
      for argument in arguments:
            Opcoes_Chrome.add_argument(argument)

      driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=Opcoes_Chrome)

      return driver

driver = iniciar_driver()

driver.get("https://cursoautomacao.netlify.app/desafios")

botao1 = driver.find_element(By.ID, 'btn1')
botao2 = driver.find_element(By.XPATH, "//*[contains(text(), 'Botão 2')]")
botao3 = driver.find_element(By.XPATH, "//*[contains(text(), 'Botão 3')]")

# botao2 = driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-dark') SOLUCAO DO PROFESSOR
# botao3 = driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-warning')

if botao1.is_enabled():
      print('Botao 1 está habilitado')
else:
      print('Botao 1 está desabilitado')
if botao2.is_enabled():
      print('Botao 2 está habilitado')
else:
      print('Botao 2 está desabilitado')
if botao3.is_enabled():
      print('Botao 3 está habilitado')
else:
      print('Botao 3 está desabilitado')

input('Enter para sair....')
driver.close()