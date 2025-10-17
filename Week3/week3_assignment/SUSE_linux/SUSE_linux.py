"""
Scrapes SUSE Linux Enterprise version and date info using XPath and saves to a CSV file.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

url = "https://en.wikipedia.org/wiki/SUSE_Linux_Enterprise"

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=Service(), options=options)

driver.get(url)
time.sleep(3)

data = []
rows = driver.find_elements(By.XPATH, "(//table[contains(@class,'wikitable')])[1]//tr[position()>1]")

for row in rows:
    cells = row.find_elements(By.XPATH, ".//td")
    if len(cells) >= 2:
        version = cells[0].text.strip()
        date = cells[1].text.strip()
        data.append({"Version": version, "Date": date, "URL": url})

driver.quit()

pd.DataFrame(data).to_csv("suse_linux_versions.csv", index=False, encoding="utf-8-sig")
print("SUSE Linux Enterprise versions saved to suse_linux_versions.csv")
