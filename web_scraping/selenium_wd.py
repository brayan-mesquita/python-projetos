from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
file_url = 'https://google.com'
file_url = 'https://facebook.com'
driver.get(file_url)
driver.get(url)