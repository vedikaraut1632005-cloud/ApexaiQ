"""
.NET 8 Versions Scraper
Scrapes .NET 8 version numbers and release dates from Microsoft download page
and saves the data into a CSV file. Uses webdriver_manager for ChromeDriver.
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
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

class DotNetScraper:
    """Scraper class for .NET 8 versions"""
    def __init__(self):
        self.url = "https://dotnet.microsoft.com/en-us/download/dotnet/8.0"
        self.table_xpath = "//table[contains(@class,'table')]"
        self.output_csv = "dotnet_versions.csv"

    def scrape(self):
        driver = get_driver()
        driver.get(self.url)
        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.presence_of_element_located((By.XPATH, self.table_xpath)))
        rows = table.find_elements(By.TAG_NAME, "tr")

        data = []
        for row in rows[1:]:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) < 2:
                continue
            versions = cols[0].text.split(",")
            date = cols[1].text
            formatted_date = format_date(date)
            for v in versions:
                data.append({"Version": v.strip(), "Release Date": formatted_date, "URL": self.url})

        pd.DataFrame(data).to_csv(self.output_csv, index=False)
        print(f"Saved: {self.output_csv}")
        driver.quit()

if __name__ == "__main__":
    scraper = DotNetScraper()
    scraper.scrape()  
