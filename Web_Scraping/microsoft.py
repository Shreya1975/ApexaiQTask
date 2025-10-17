from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_windows_server_release_info(url: str, output_csv: str):
    """
    Scrapes tables from the Windows Server release info page using Selenium
    and combines the extracted data into a single CSV file.

    Parameters
    ----------
    url : str
        The URL of the Windows Server release information page.
    output_csv : str
        The filename for the combined CSV output.

    Returns
    -------
    None
        Writes a CSV file in the same folder containing all scraped table rows.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(5)  # allow page to load fully

    tables = driver.find_elements(By.TAG_NAME, "table")

    combined_rows = []
    for idx, table in enumerate(tables, start=1):
        header_elems = table.find_elements(By.TAG_NAME, "th")
        headers = [th.text.strip() for th in header_elems]
        for tr in table.find_elements(By.TAG_NAME, "tr")[1:]:
            td_elems = tr.find_elements(By.TAG_NAME, "td")
            row = [td.text.strip().replace("\n", " ") for td in td_elems]
            if row:
                combined_rows.append([f"Table_{idx}"] + row)

    driver.quit()

    if not combined_rows:
        print("No table data found to write.")
        return

    max_len = max(len(r) for r in combined_rows)
    for r in combined_rows:
        while len(r) < max_len:
            r.append("")

    col_names = ["Table_Source"] + [f"Col_{i}" for i in range(1, max_len)]
    df = pd.DataFrame(combined_rows, columns=col_names)
    df.to_csv(output_csv, index=False, encoding="utf-8")
    print(f"Scraping done. Data saved in '{output_csv}'.")


if __name__ == "__main__":
    scrape_windows_server_release_info(
        url="https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info",
        output_csv="windows_server_release_info.csv"
    )
