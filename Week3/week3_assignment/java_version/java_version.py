"""
DotNet 8.0 Download Table Scraper

This script scrapes download tables from the .NET 8.0 download page.
It extracts Version, OS, and Download Link columns and saves them to a CSV file.
The script uses Selenium, Pandas, and OOP concepts.
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class DotNetScraper:
    """Scrapes .NET 8.0 download tables and saves them to CSV."""

    def __init__(self, url, headless=True):
        """Initialize driver and settings."""
        self.url = url
        self.headless = headless
        self.driver = self._setup_driver()
        self.wait = WebDriverWait(self.driver, 20)
        self.data = []

    def _setup_driver(self):
        """Set up Chrome WebDriver with options."""
        options = Options()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--log-level=3")
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    def open_website(self):
        """Open the target webpage."""
        self.driver.get(self.url)
        # Wait for at least one table to load
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//table[contains(@class,'table-bordered')]")
        ))

    def scrape_tables(self):
        """Scrape all tables: Version, OS, and Download Link."""
        tables = self.driver.find_elements(By.XPATH, "//table[contains(@class,'table-bordered')]")

        for table in tables:
            rows = table.find_elements(By.XPATH, ".//tr")[1:]  # Skip header
            for row in rows:
                cols = row.find_elements(By.XPATH, ".//td")
                if len(cols) >= 3:
                    version = cols[0].text.strip()
                    os_info = cols[1].text.strip()
                    link_elem = cols[2].find_element(By.XPATH, ".//a") if cols[2].find_elements(By.XPATH, ".//a") else None
                    download_link = link_elem.get_attribute("href") if link_elem else "N/A"

                    # Split multiple versions if present
                    versions = [v.strip() for v in version.replace("\n", "/").split("/") if v.strip()]
                    for v in versions:
                        self.data.append({
                            "Version": v,
                            "Operating System": os_info,
                            "Download Link": download_link
                        })

    def save_to_csv(self, filename="dotnet_8_0_downloads.csv"):
        """Save the scraped data to a CSV file."""
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f" Saved {len(df)} rows to {filename}")
        return df

    def close(self):
        """Close the browser."""
        self.driver.quit()


# Usage Example
if __name__ == "__main__":
    scraper = DotNetScraper(
        url="https://dotnet.microsoft.com/en-us/download/dotnet/8.0",
        headless=False  
    )
    scraper.open_website()
    scraper.scrape_tables()
    scraper.save_to_csv("dotnet_8_0_downloads.csv")
    scraper.close()
