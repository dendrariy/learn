from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    answer = int(num1.text) + int(num2.text)

    browser.find_element(By.CSS_SELECTOR, "#dropdown").click()
    browser.find_element(By.XPATH, f"//option[@value='{answer}']").click()


    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()