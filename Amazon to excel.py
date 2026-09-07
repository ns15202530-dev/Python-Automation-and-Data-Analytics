# use me ane bali sari libraries ko import kar rahe hain
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from openpyxl import load_workbook
# Edge Browser ko open karne ke liye options set kar rahe hain
options = webdriver.EdgeOptions()
# User-agent header set kar rahe hain
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
driver = webdriver.Edge(options=options)
data = []

try:
#  Robot ko Amazon website dena    
    driver.get("https://www.amazon.com")
    time.sleep(4)
#   Robot ko search box me "T-shirts" type karne ke liye find_element method ka use kar rahe hain    
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("T-sharts", Keys.ENTER)
#   Robot ko search results page load hone ke liye wait kar rahe hain    
    time.sleep(4)
    products = driver.find_elements(By.CSS_SELECTOR,"div[data-component-type='s-search-result']")
    print(f"Total products = {len(products)}")

    for product in products:
        try:
#   Robot ko product name find karne ke liye find_element method ka use kar rahe hain            
            name = product.find_element(By.CSS_SELECTOR, "h2 span").get_attribute("textContent").strip()
        except:
#   Agar product name nahi milta hai to name ko empty string set kar rahe hain            
            name = ""
        try:
#   Robot ko product price find karne ke liye find_element method ka use kar rahe hain            
            price_element = product.find_element(By.CSS_SELECTOR, "span.a-price")
            whole = price_element.find_element(By.CSS_SELECTOR, "span.a-price-whole").get_attribute("textContent").strip()
            fraction = price_element.find_element(By.CSS_SELECTOR, "span.a-price-fraction").get_attribute("textContent").strip()
            price = f"${whole}.{fraction}"
        except:
            price = ""
        if name and "cort" in name.lower():
            # Amazon search cards do not expose a separate brand field; use
            # the first word of the product title as the brand.
            brand = name.split()[0]
            data.append({"Brand": brand, "Price": price})
#   Data ko pandas DataFrame me convert kar rahe hain            
    df = pd.DataFrame(data)
    path = "C:/Users/DELL/Downloads/product andprices.xlsx"
    df.to_excel(path, index=False)
    workbook = load_workbook(path)
    worksheet = workbook.active
#   Column widths ko set kar rahe hain    
    worksheet.column_dimensions["A"].width = 29
    worksheet.column_dimensions["B"].width = 20
    workbook.save(path)
    print(f"Data saved: {path}")
except Exception as e:
#   Agar koi error aata hai to usko print kar rahe hain    
    print(f"Error: {e}")
#   Finally block me driver ko quit kar rahe hain taki browser close ho jaye
finally:
    driver.quit()