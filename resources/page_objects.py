from time import sleep
from data_elements.element_mapper import Endpoints as ed, Elements as el
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Amazon:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)

    def launch_site(self):
        self.driver.get(ed.home)
        self.driver.maximize_window()

    def search_for_an_item(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, el.search_field)))
        self.driver.find_element(By.CSS_SELECTOR, el.search_field).send_keys(el.search_text)
        self.driver.find_element(By.CSS_SELECTOR, el.search_button).click()

    def check_search_result(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, el.filter_dropdown)))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, el.result_block)))
        texts = self.driver.find_element(By.CSS_SELECTOR, el.result_block).text
        try:
            if texts == el.result_checker:
                print ("Text Found")
        except:
             raise AssertionError ('Text not Found')

    def close_session(self):
        self.driver.quit()
