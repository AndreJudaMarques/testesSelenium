from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


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
# navegar até o site
driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(2)

driver.execute_script("window.scrollTo(0, 500);")
sleep(1)

button_conversivel = driver.find_element(By.ID, 'conversivelcheckbox')
sleep(1)
if button_conversivel.is_selected() == True:
    print('botao ja selecionado')
else:
    sleep(1)
    button_conversivel.click()

button_offroad = driver.find_element(By.ID, 'offroadcheckbox')
sleep(1)
if button_offroad.is_selected() == True:
    print('botao ja selecionado')
else:
    sleep(1)
    button_offroad.click()

input('')
driver.close()