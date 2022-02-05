from time import sleep
from data_elements.element_mapper import Endpoints as ed, Elements as el
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def test_launch_site():
    driver.get(ed.home)
    driver.maximize_window()


def test_search_for_an_item():
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, el.search_field)))
    driver.find_element(By.CSS_SELECTOR, el.search_field).send_keys(el.search_text)
    driver.find_element(By.CSS_SELECTOR, el.search_button).click()


def test_check_search_result():
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, el.filter_dropdown)))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, el.result_block)))
    texts = driver.find_element(By.CSS_SELECTOR, el.result_block).text
    try:
        if texts == el.result_checker:
            print ("Text Found")
    except:
        raise AssertionError ('Text not Found')


def test_close_session():
    driver.quit()

