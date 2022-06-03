from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.google.com")
