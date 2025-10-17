from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_dotnet_core(url: str, output_csv: str):
    """
    Scrapes all tables from the .NET Core 8.0.0 version page using Selenium
    and combines the extracted data into a single CSV file.

    Parameters
    ----------
    url : str
        The URL of the .NET Core 8.0.0 release information page.
    output_csv : str
        The filename for the combined CSV output.

    Returns
    -------
    None
        Writes a CSV file in the same folder containing all scraped rows.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(5)  # allow page to fully load

    all_rows = []

    # Scrape all tables
    tables = driver.find_elements(By.TAG_NAME, "table")
    for idx, table in enumerate(tables, start=1):
        headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")]
        for tr in table.find_elements(By.TAG_NAME, "tr")[1:]:
            tds = tr.find_elements(By.TAG_NAME, "td")
            row = [td.text.strip().replace("\n", " ") for td in tds]
            if row:
                all_rows.append([f"table_{idx}"] + row)

    driver.quit()

    if not all_rows:
        print("No table data found.")
        return

    # Pad rows to equal length
    max_len = max(len(r) for r in all_rows)
    for r in all_rows:
        while len(r) < max_len:
            r.append("")

    # Create generic column names
    col_names = ["Source"] + [f"Col_{i}" for i in range(1, max_len)]
    df = pd.DataFrame(all_rows, columns=col_names)
    df.to_csv(output_csv, index=False, encoding="utf-8")
    print(f"Scraping complete. Data saved as '{output_csv}'.")

if __name__ == "__main__":
    scrape_dotnet_core(
        url="https://versionsof.net/core/8.0/8.0.0/",
        output_csv="dotnet_core_8_0_0_data.csv"
    )

