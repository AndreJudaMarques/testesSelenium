from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver

driver = iniciar_driver()

def digitar_naturalmente(texto, elemento):
                         for letra in texto:
                                 elemento.send_keys(letra)
                                 sleep(random.randint(1,5)/ 60) #(1,5)/30

driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(2)

textoO = """Todos sabemos da importância de desenvolver uma estratégia de conteúdo sólida e do crescimento exponencial que ela pode resultar quando bem feita. Mas também há uma variedade de equívocos no mundo do marketing de conteúdo e muitos desses estão relacionados sobre qual o tamanho ideal dos conteúdos de texto. Devem ser longos e com enorme quantidade de palavras, ou um texto curto e o objetivo?"""

driver.execute_script("window.scrollTo(0, 800);")
sleep(2)

paragrafo = driver.find_element(By.ID, 'campoparagrafo')

digitar_naturalmente(textoO, paragrafo)
sleep(1)

validar = driver.find_element(By.XPATH, '/html/body/section[4]/button')
validar.click()

input('')
driver.close()