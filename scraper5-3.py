from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://shopee.tw/mall/%E5%B1%85%E5%AE%B6%E7%94%9F%E6%B4%BB-cat.11040925')
time.sleep(5)

cards = driver.find_elements(By.CSS_SELECTOR, 'div[class="col-xs-2 recommend-products-by-view__item-card-wrapper"]')

items = []
for card in cards:
    title = card.find_element(By.CSS_SELECTOR, 'div[class="ie3A+n bM+7UW Cve6sh"]').text
    price = card.find_element(By.CSS_SELECTOR, 'div[class="vioxXd rVLWG6"]').text
    link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
    items.append((title, price, link))

print(items)
