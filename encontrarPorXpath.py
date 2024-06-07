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

#encontrar elementos por Xpath

zona = driver.find_element(By.XPATH,"//*[text()='ZONA DE TESTES']")

if zona is not None:
      print('achei a zona')

# //* = todos
# //*[h4]
# //*[contains(text(), 'Exemplo')]
# //*[contains(text(), 'Dropdown') or contains(text(), 'estilizados')]
# //*[starts-with(text(), 'exemplo')]
# //*[starts-with(@class, 'btn')]
# //*[text()='Exemplo Checkbox']
# //h4[text()='Exemplo Checkbox'] MAIS ESPECIFICO
# //button[@aria-label='Toggle navigation'] MAIS ESPECIFICO
# //section[@class='jumbotron']
# //div[@class='form-check']
# //div[@id='select-class-example']//fieldset/h4 ENCONTRAR 1 ELEMENTE DENTRO DE OUTROS
# //thead//tr//th[3] ENCONTRAR 1 ELEMENTE DENTRO DE OUTROS

umatag = driver.find_element(By.XPATH, "//thead//tr//th[3]")
variastag = driver.find_elements(By.XPATH,'//div/fieldset')

if umatag is not None:
      print('achei 1 tag')
if variastag is not None:
      print('achei as tags')

input(' Enter para sair...')
driver.close()
