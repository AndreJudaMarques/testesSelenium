from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()             #largura x altura
    arguments = ['--lang=pt-BR', '--window-size=1000,1000', '--incognito']
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

driver.get('https://cursoautomacao.netlify.app/')
sleep(2)

janela1 = driver.current_window_handle

driver.execute_script("window.scrollTo(0, 600);")
sleep(1)

botaoAbrir = driver.find_element(By.XPATH, "//button[@onclick='abrirJanela()']")
botaoAbrir.click()
sleep(2)

janelas = driver.window_handles
#print(janelas)
#--------------------------------------SEGUNDA JANELA---------------------------------------
segundaJanela = janelas[1]

driver.switch_to.window(segundaJanela)

campoSenha = driver.find_element(By.XPATH, "//input[@id='campo_pesquisa']")
campoSenha.click()
sleep(1)
campoSenha.send_keys('Olá mundo!!!')
sleep(1)
botaoPesquisar = driver.find_element(By.XPATH, "//button[@id='fazer_pesquisa']") 
botaoPesquisar.click()
sleep(2)
driver.close()

input('')
driver.close()