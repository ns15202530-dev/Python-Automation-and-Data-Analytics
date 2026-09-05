#                       Day 45
import pandas as pd
import numpy as np
import os 
# 1. गंदा डेटा तैयार करना (Sample Messy Corporate Data)
ganda_data = {
    
    'Name': ['Nitish', 'Rahul', 'Amit', 'Nitish', 'Aman', 'Vijay', 'Vijay'],
    'Department': ['IT', 'Sales', 'HR', 'IT', 'Marketing', np.nan, 'IT'],
    'Salary': [45000, np.nan, 35000, 45000, 50000, 60000, 60000],
    'Bonus': [5000, 2000, np.nan, 5000, 4000, 7000, 7000]
}

df = pd.DataFrame(ganda_data)
print("--- 1. गंदा और बिखरा हुआ असली डेटा ---")
print(df)
print("\n" + "="*50 + "\n")

# 2. डेटा क्लीनिंग (Advanced Data Cleaning)

# स्टेप A: डुप्लिकेट रो (Duplicate Rows) को जड़ से हटाना
df.drop_duplicates(inplace=True)

# स्टेप B: डिपार्टमेंट में जहाँ NaN (खाली) है, वहाँ 'Bench' भरना
df['Department'].fillna('Bench', inplace=True)

# स्टेप C: सैलरी में जहाँ NaN है, वहाँ पूरे डिपार्टमेंट की एवरेज (Mean) सैलरी भरना
average_salary = df['Salary'].mean()
df['Salary'].fillna(average_salary, inplace=True)

# स्टेप D: बोनस में जहाँ NaN है, वहाँ 0 (शून्य) भरना
df['Bonus'].fillna(0, inplace=True)

print("--- 2. पांडास द्वारा बिल्कुल साफ़ (Cleaned) किया गया डेटा ---")
print(df)
print("\n" + "="*50 + "\n")

# 3. एक्सेल ऑटोमेशन + लाइव फ़ॉर्मूला इंजेक्शन (Excel Formula Injection)

# एक नई साफ़ एक्सेल फ़ाइल बनाना (बिना गंदे इंडेक्स कॉलम के)
excel_file = "Company_Clean_Report.xlsx"

# ExcelWriter का इस्तेमाल करके पांडास डेटा को एक्सेल में डालना
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Salary_Report', index=False)
    
    # एक्सेल शीट को सीधे एक्सेस करना ताकि फ़ॉर्मूला लिख सकें
    workbook = writer.book
    worksheet = writer.sheets['Salary_Report']
    
    # डेटा के बिल्कुल नीचे (रो नंबर 7 पर) लाइव टोटल फ़ॉर्मूला इंजेक्ट करना
    # सैलरी का टोटल (C कॉलम की रो 2 से 6 तक)
    worksheet['C7'] = "Total Salary:"
    worksheet['D7'] = "=SUM(D2:D6)"
    
    # बोनस का टोटल (E कॉलम की रो 2 से 6 तक)
    worksheet['E7'] = "=SUM(E2:E6)"

print(f"🎉 बधाई हो भैया! डे 45 का प्रोजेक्ट सफल रहा।")
print(f"आपकी कंप्यूटर डायरेक्टरी में '{excel_file}' फ़ाइल बन चुकी है, जिसमें लाइव =SUM फ़ॉर्मूला लगा हुआ है!")
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
excel_file = os.path.join(downloads_path, "Company_Clean_Report.xlsx")
#                       Day 46

import pandas as pd
import numpy as np
import os

# 1. दो अलग-अलग महीनों का डेटा तैयार करना (Simulating 2 different data sheets)
data_month1 = {
    
    'Name': ['Nitish', 'Rahul', 'Amit'],
    'Department': ['IT', 'Sales', 'HR'],
    'Salary': [45000, 52000, 35000]
}

data_month2 = {
    
    'Name': ['Nitish', 'Rahul', 'Aman'],
    'Department': ['IT', 'Sales', 'Marketing'],
    'Salary': [46000, 52000, 48000]  # नीतीश की सैलरी दूसरे महीने बदल गई
}

df1 = pd.DataFrame(data_month1)
df2 = pd.DataFrame(data_month2)

print("--- शीट 1 (पहले महीने का डेटा) ---")
print(df1)
print("\n--- शीट 2 (दूसरे महीने का डेटा) ---")
print(df2)
print("\n" + "="*50 + "\n")


# 2. दोनों शीट्स को एक के नीचे एक जोड़ना (Concatenation)
# ignore_index=True लिखने से इंडेक्स नंबर 0,1,2,3,4,5 बिल्कुल सीधा और साफ़ हो जाता है
df_combined = pd.concat([df1, df2], ignore_index=True)

print("--- 2. दोनों शीट्स को आपस में जोड़ने के बाद (Combined Data) ---")
print(df_combined)
print("\n" + "="*50 + "\n")


# 3. नाम के हिसाब से ग्रुप बनाकर कुल सैलरी का जोड़ निकालना (Groupby & Aggregation)
# यहाँ हम 'Name' और 'Department' के हिसाब से ग्रुप बना रहे हैं और 'Salary' का 'sum' (जोड़) कर रहे हैं
final_report = df_combined.groupby(['Name', 'Department']).agg({'Salary': 'sum'}).reset_index()

print("--- 3. फाइनल ग्रुप रिपोर्ट (टोटल सैलरी के साथ) ---")
print(final_report)
print("\n" + "="*50 + "\n")


# 4. फाइनल रिपोर्ट को सीधे Downloads फ़ोल्डर में एक्सेल बनाकर भेजना
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
excel_file = os.path.join(downloads_folder, "Final_Merged_Salary_Report.xlsx")

# एक्सेल में डेटा डालना
final_report.to_excel(excel_file, sheet_name='Global_Report', index=False)

print(f"🎉 महा-विजय भैया! डे 46 का मर्जिंग प्रोजेक्ट 100% सफल रहा।")
print(f"आपकी फाइनल महा-रिपोर्ट सीधे 'Downloads' फ़ोल्डर में '{os.path.basename(excel_file)}' नाम से सुरक्षित सेव हो चुकी है!")