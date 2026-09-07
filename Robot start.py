from selenium import webdriver as w
from selenium.webdriver.support.ui import WebDriverWait

options = w.EdgeOptions()
options.add_argument("--start-minimized")
drivet = None

try:
    driver = w.Edge(options=options)
    WebDriverWait
    driver.get("https://www.google.com")
    titel = driver.title
    print(titel)
    
except Exception as e:
    print(f"Daya{e}")

finally:
    if driver:
        driver.quit()  