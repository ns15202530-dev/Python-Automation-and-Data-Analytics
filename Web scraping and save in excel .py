from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Robot is reddy

options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
options.add_argument("--remote-allow-origins=*")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

driver = webdriver.Edge(options=options)

try:
    driver.get("https://google.com")
    time.sleep(random.uniform(2, 3))
    
    # गूगल के सर्च बॉक्स को ढूँढकर टाइप करना
    search_box = driver.find_element(By.NAME, "q")
    search_text = "Python Web Scraping"
    
    for letter in search_text:
        search_box.send_keys(letter)
        time.sleep(0.1)
        
    search_box.send_keys(Keys.ENTER)
    time.sleep(4) # सर्च रिजल्ट्स लोड होने का इंतज़ार
    
    print("\nरोबोट अब पन्ने के अंदर से असली डेटा (वेबसाइट्स के नाम) निकाल रहा है:\n")
    
    # गूगल सर्च में सभी हेडिंग्स (H3 टैग) को एक साथ ढूँढना
    headings = driver.find_elements(By.TAG_NAME, "h3")
    
    # Loop चलाकर एक-एक वेबसाइट का नाम टर्मिनल में छापना
    counter = 1
    for heading in headings:
        # सिर्फ वही नाम प्रिंट करना जो खाली न हो
        if heading.text:
            print(f"📊 रिजल्ट {counter}: {heading.text}")
            counter += 1
            
    print("रोबोट ने कुल {counter-1} वेबसाइट्स का डेटा लाइव खोज निकाला है!")

except Exception as e:
    print(f"एरर आया: {e}")

finally:
    if 'driver' in locals():
        time.sleep(2)
        driver.quit()


# next code                           

# ek Anti crash Web scraping ka code
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. एज ब्राउज़र रोबोट की सेटिंग्स (Anti-Crash)
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized") 
options.add_argument("--remote-allow-origins=*")

# रोबोट ड्राइवर चालू करना
driver = webdriver.Edge(options=options)

try:
    print(" रोबोट अब लाइव स्क्रैपिंग वेबसाइट पर जा रहा है...")
    # हम सीधे बिना किसी सुरक्षा ब्लॉक वाली कड़क वेबसाइट पर जा रहे हैं
    driver.get("http://toscrape.com")
    time.sleep(3) # वेबसाइट को पूरी तरह खुलने का समय देना
    
    print("\nरोबोट अब पन्ने के अंदर से महान लोगों के विचार (Quotes) chun रहा है:\n")
    
    # वेबसाइट के अंदर से सभी विचार (Quotes) वाले टेक्स्ट को ढूँढना (क्लास नाम 'text' के ज़रिए)
    all_quotes = driver.find_elements(By.CLASS_NAME, "text")
    # वेबसाइट के अंदर से उनके लेखकों (Authors) के नाम ढूँढना (क्लास नाम 'author' के ज़रिए)
    all_authors = driver.find_elements(By.CLASS_NAME, "author")
    
    # Loop चलाकर दोनों डेटा को आपस में मिलाकर टर्मिनल में छापना
    counter = 1
    for i in range(len(all_quotes)):
        quote_text = all_quotes[i].text
        author_name = all_authors[i].text
        
        print(f"💬 विचार {counter}: \"{quote_text}\"")
        print(f"✍️ लेखक: - {author_name}")
        print("-" * 50)
        counter += 1
            
    print(f"\n रोबोट ने लाइव वेबसाइट से कुल {counter-1} Great विचार और लेखकों का डेटा खोज निकाला है!")

except Exception as e:
    print(f" एक छोटी सी समस्या आई: {e}")

finally:
    if 'driver' in locals():
        print("\n काम पूरा हुआ, रोबोट Edge ब्राउज़र को बंद कर रहा है...")
        driver.quit()


#Data ko scrape aor excel me save karne bala code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time
import random

options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
options.add_argument("--remote-allow-origins=*")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

driver = webdriver.Edge(options=options)

# डेटा स्टोर करने के लिए खाली लिस्ट
scraped_titles = []

try:
    print(" रोबोट अब गूगल पर जा रहा है...")
    driver.get("https://Yaahu.com")
    time.sleep(random.uniform(2, 3))
    
    # गूगल सर्च बॉक्स में टाइप करना
    search_box = driver.find_element(By.NAME, "q")
    search_text = "Python Web Scraping"
    
    for letter in search_text:
        search_box.send_keys(letter)
        time.sleep(0.1)
        
    search_box.send_keys(Keys.ENTER)
    time.sleep(5) # रिजल्ट्स पूरी तरह लोड होने का इंतज़ार
    
    print(" लाइव पन्ने से वेबसाइट्स के नाम नोच रहा है...")
    headings = driver.find_elements(By.TAG_NAME, "h3", "title")
    
    for heading in headings:
        if heading.text:
            # नाम को लिस्ट के अंदर सुरक्षित जमा करना
            scraped_titles.append(heading.text)
            
    print(f" रोबोट ने मुट्ठी में कुल {len(scraped_titles)} नाम जमा कर लिए हैं।")

    # --- PANDAS & EXCEL AUTOMATION ---
    if len(scraped_titles) > 0:
        print(" पांडास (Pandas) की मदद से डेटा को एक्सेल में बदल रहा हूँ...")
        
        # १. लिस्ट को सुंदर टेबल (DataFrame) में बदलना
        df = pd.DataFrame({'Serial_No': range(1, len(scraped_titles) + 1), 'Website_Title': scraped_titles})
        
        # २. डाउनलोड्स फ़ोल्डर का रास्ता ढूंढना
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        excel_file = os.path.join(downloads_folder, "Google_Scraped_Results.xlsx")
        
        # ३. एक्सेल फाइल बनाकर सीधे डाउनलोड्स में भेजना
        df.to_excel(excel_file, index=False, sheet_name="Google_Data")
        
        print(f"\n आपकी लाइव एक्सेल फ़ाइल सीधे 'Downloads' फ़ोल्डर में '{os.path.basename(excel_file)}' नाम से सुरक्षित सेव हो चुकी है!")
    else:
        print(" कोई डेटा नहीं मिला, इसलिए एक्सेल नहीं बनी।")

except Exception as e:
    print(f"एरर आया : {e}")

finally:
    if 'driver' in locals():
        print(" काम पूरा हुआ, रोबोट Edge ब्राउज़र को बंद कर रहा है...")
        driver.quit()        