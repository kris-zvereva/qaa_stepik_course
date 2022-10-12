import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    book = browser.find_element(By.ID, 'book')
    book.click()

    x = browser.find_element(By.ID, 'input_value').text
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(calc(int(x)))

    submit_button = browser.find_element(By.ID, 'solve')
    submit_button.click()


finally:
    time.sleep(10)
    browser.quit()

