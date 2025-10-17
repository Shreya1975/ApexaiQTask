from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_dotnet_download_data(url: str, output_csv: str):
    """
    Scrapes all download tables from the .NET 8.0 download page using Selenium
    and combines the extracted data into a single CSV file.

    Parameters
    ----------
    url : str
        The URL of the .NET 8.0 download page.
    output_csv : str
        The name of the CSV file to save the combined scraped data.

    Returns
    -------
    None
        Creates one CSV file in the same folder containing all table data.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(4)

    tables = driver.find_elements(By.TAG_NAME, "table")

    if not tables:
        print("⚠️ No tables found on the page.")
        driver.quit()
        return

    all_data = []
    for i, table in enumerate(tables, start=1):
        headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")]
        for tr in table.find_elements(By.TAG_NAME, "tr")[1:]:
            cells = tr.find_elements(By.TAG_NAME, "td")
            row = [cell.text.strip().replace("\n", " ") for cell in cells]
            if row:
                # add table number to identify which table the row belongs to
                all_data.append([f"Table {i}"] + row)

    if not all_data:
        print("⚠️ No data rows found in tables.")
        driver.quit()
        return

    # Determine the maximum number of columns to pad uneven rows
    max_cols = max(len(row) for row in all_data)
    for row in all_data:
        while len(row) < max_cols:
            row.append("")

    # Create DataFrame with generic headers
    columns = ["Table_Source"] + [f"Column_{i}" for i in range(1, max_cols)]
    df = pd.DataFrame(all_data, columns=columns)

    df.to_csv(output_csv, index=False, encoding="utf-8")
    driver.quit()
    print(f"✅ Scraping complete! All data saved as '{output_csv}' in the same folder.")


if __name__ == "__main__":
    scrape_dotnet_download_data(
        url="https://dotnet.microsoft.com/en-us/download/dotnet/8.0",
        output_csv="dotnet_downloads_combined.csv"
    )
