from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
import json

# Setup driver in headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Loading webpage
url = 'https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart'
driver.get(url)

# Finding all <li> elements
search_results = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
print(f"Number of search results: {len(search_results)}")

results = []

# Loop through each search result
for result in search_results:
    try:
        title_element = result.find_element(By.CSS_SELECTOR, 'span.title-content')
        title = title_element.text.strip()

        authors = result.find_elements(By.CSS_SELECTOR, 'a.author-link')
        author_names = "; ".join([a.text.strip() for a in authors])

        year_element = result.find_element(By.CSS_SELECTOR, 'span.display-info-primary')
        year = year_element.text.strip()

        book_info = {
            'Title': title,
            'Authors': author_names,
            'Year': year
        }
        results.append(book_info)

    except Exception as e:
        print(f"Error processing result: {type(e).__name__} - {e}")

# Convert results to DataFrame
df = pd.DataFrame(results)

# Save data to CSV
df.to_csv('get_books.csv', index=False)
print("Data saved in assignment9 folder as get_books.csv")

# Save data to JSON
with open('get_books.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

print("Data saved in assignment9 folder as get_books.json")

# Closing the driver
driver.quit()
