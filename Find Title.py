#  Use me ane bali sari libraries ko import kar rahe hain
from selenium import webdriver as w
from selenium.webdriver.common.by import By as b
from selenium.webdriver.common.keys import Keys as k
import time

# Edge Browser ko open karne ke liye options set kar rahe hain
option = w.EdgeOptions()
driver = None

try:
    driver = w.Edge(options=option)
# Robot ko website dena    
    driver.get("https://www.google.com")
    print(f"Yah hai = {driver.title}")
#  robot ko 2 second ka wait kar rahe hain    
    time.sleep(2)
#   Robot ko search box me "shuse" type karne ke liye find_element ka use kar rahe hain    
    search = driver.find_element(b.NAME, "q")
    search.send_keys("shuse" + k.ENTER)
    time.sleep(5)   
#  Robot ko last me close karne ke liye driver.quit() ka use kar rahe hain    
finally:
    if driver:
        driver.quit()