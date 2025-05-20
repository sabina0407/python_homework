from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://owasp.org/www-project-top-ten/")

elements = driver.find_elements(By.XPATH, '//li/a[strong and contains(@href, "/Top10/")]')

vulnerabilities = []
for element in elements:
    try:
        title = element.find_element(By.XPATH, './/strong').text.strip()
        url = element.get_attribute('href')
        vulnerabilities.append({"title": title, "Link": url})
    except Exception as e:
        print(f"Error processing element: {type(e).__name__} - {e}")
        
print(f"Number of vulnerabilities found: {len(vulnerabilities)}")
print(vulnerabilities)

df = pd.DataFrame(vulnerabilities)
df.to_csv('owasp_top_10.csv', index=False)
print("Data saved in assignment9 folder as owasp_top_10.csv")

driver.quit()
