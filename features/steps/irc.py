from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('Acesso o site do selenium')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://selenium.dev")

@when('Clico no icone IRC')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fas.fa-comments").click()
    print(str(context.driver.current_url))
    titulo= context.driver.window_handles[1]
    context.driver.switch_to.window(titulo)

@then('A página é redirecionada')
def step_impl(context):
    assert context.driver.title == "Kiwi IRC - The web IRC client"

@then('Verifico se o botão Iniciar esta desabilitado')
def step_impl(context):
    botao = context.driver.find_element(By.CSS_SELECTOR, ".u-button").get_attribute("disabled")
    assert botao == "true"
    context.driver.quit()


