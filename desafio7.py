from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
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

driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(2)

janela_inicial = driver.current_window_handle
driver.execute_script("window.scrollTo(0, 2500);")
sleep(1)

abrirJanela = driver.find_element(By.XPATH, "//*[contains(text(), 'Abrir nova janela')]") 
abrirJanela.click()
sleep(1)

janelas = driver.window_handles
print(janelas)

driver.switch_to.window(janelas[1])

campoPesquisa = driver.find_element(By.XPATH, "//textarea[@id='opiniao_sobre_curso']")
campoPesquisa.click()
sleep(1)
campoPesquisa.send_keys('Cade o computador')
sleep(1)

botaoPesquisar = driver.find_element(By.XPATH, "//button[@id='fazer_pesquisa']")
botaoPesquisar.click()
sleep(1)
driver.execute_script("window.scrollTo(0, 500);")
sleep(1)
driver.close()

driver.switch_to.window(janelas[0])

campoDepoimento = driver.find_element(By.XPATH, "//textarea[@name='campo_depoimento']")
campoDepoimento.click()
sleep(1)
campoDepoimento.send_keys('exercicio finalizad!!!')
sleep(2)

input('')
driver.close()