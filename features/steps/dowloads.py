from selenium import webdriver
from selenium.webdriver.common.by import By

@when('Clico no botão Dowloads')
def step_impl(context):
    menu = context.driver.find_elements(By.CSS_SELECTOR, ".nav-link")
    menu[1].click()

@then('Verifico se a página foi aberta')
def step_impl(context):
    titulo= context.driver.find_element(By.CSS_SELECTOR, ".display-1")
    assert titulo.text == "Downloads"