from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
      Opcoes_Chrome = Options()
      arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
      for argument in arguments:
            Opcoes_Chrome.add_argument(argument)

      driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=Opcoes_Chrome)

      return driver


driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(5)
# Rolar até o fim da página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)
# Rolar até o topo da página
driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
sleep(5)
# Rolar X quantidade em pixels(descer)
# driver.execute_script("window.scrollTo(0, 1500);")
# sleep(5)
# # Rolar X quantidade em pixels(subir)
# driver.execute_script("window.scrollTo(0, -1500);")

input('')
driver.close()