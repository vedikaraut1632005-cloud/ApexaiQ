"""
Windows Server Versions Scraper
Scrapes Windows Server release info from Microsoft docs
and saves the data into a CSV file. If date is missing, only Version and URL are included.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime

def format_date(date_str):
    date_str = date_str.strip()
    if not date_str:
        return ""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
    except:
        pass
    for fmt in ("%d %B %Y", "%B %Y", "%Y"):
        try:
            return datetime.strptime(date_str, fmt).strftime(
                "%Y-%m-%d" if fmt=="%d %B %Y" else ("%Y-%m" if fmt=="%B %Y" else "%Y")
            )
        except:
            continue
    return ""

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

class WindowsServerScraper:
    """Scraper class for Windows Server versions"""
    def __init__(self):
        self.url = "https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info"
        self.table_xpath = "//table[contains(@class,'table')]"
        self.output_csv = "windows_server_versions.csv"

    def scrape(self):
        driver = get_driver()
        driver.get(self.url)
        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.presence_of_element_located((By.XPATH, self.table_xpath)))
        rows = table.find_elements(By.TAG_NAME, "tr")

        data = []
        last_date = ""
        for row in rows[1:]:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) < 1:
                continue

            # Handle date
            if len(cols) > 1:
                date_elements = cols[1].find_elements(By.TAG_NAME, "time")
                if date_elements:
                    last_date = date_elements[0].get_attribute("datetime")
                else:
                    if cols[1].text.strip():
                        last_date = cols[1].text.strip()
                formatted_date = format_date(last_date)
            else:
                formatted_date = ""

            # Split versions into separate rows
            versions = cols[0].text.split(",")
            for v in versions:
                row_data = {"Version": v.strip(), "URL": self.url}
                if formatted_date:
                    row_data["Release Date"] = formatted_date
                data.append(row_data)

        df = pd.DataFrame(data)
        df.to_csv(self.output_csv, index=False)
        print(f"Saved: {self.output_csv}")
        driver.quit()

if __name__ == "__main__":
     scraper = WindowsServerScraper()
     scraper.scrape()
