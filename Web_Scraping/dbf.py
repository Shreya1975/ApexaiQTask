from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime
import re
import time

def scrape_dbf_news(url: str, output_csv: str):
    """
    Scrapes news from dbf2002.com/news.html and extracts Version, Date, and URL
    for each news entry in the list.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(3)

    all_rows = []

    # News items are <ul> > <li>
    news_list = driver.find_element(By.TAG_NAME, "ul")
    news_items = news_list.find_elements(By.TAG_NAME, "li")

    for item in news_items:
        try:
            # Extract link
            a_tag = item.find_element(By.TAG_NAME, "a")
            news_url = a_tag.get_attribute("href")
            version_text = a_tag.text.strip()
            version_match = re.search(r'v\d+\.\d+(\.\d+)?', version_text)
            version = version_match.group(0) if version_match else version_text

            # Extract date from text (date is before the link in the li text)
            full_text = item.text.strip()
            date_match = re.match(r'(\d{2}\.\d{2}\.\d{4})', full_text)
            if date_match:
                date_str = date_match.group(1)
                formatted_date = datetime.strptime(date_str, "%d.%m.%Y").strftime("%Y-%m-%d")
            else:
                formatted_date = ""

            all_rows.append([version, formatted_date, news_url])
        except Exception:
            continue

    driver.quit()

    if not all_rows:
        print("No news data found.")
        return

    df = pd.DataFrame(all_rows, columns=["Version", "Date", "URL"])
    df.to_csv(output_csv, index=False, encoding="utf-8")
    print(f"Scraping complete. Data saved as '{output_csv}'.")

if __name__ == "__main__":
    scrape_dbf_news(
        url="https://www.dbf2002.com/news.html",
        output_csv="dbf_news.csv"
    )
