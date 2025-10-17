"""
Scrapes .NET Core 8.0 versions from versionsof.net using XPath and saves version, URL, and date to CSV.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

url = "https://versionsof.net/core/8.0/8.0.0/"

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=Service(), options=options)

driver.get(url)
time.sleep(3)

data = []
rows = driver.find_elements(By.XPATH, "(//table)[1]//tr[position()>1]")

for row in rows:
    cells = row.find_elements(By.XPATH, ".//td")
    if len(cells) >= 2:
        version = cells[0].text.strip()
        date = cells[1].text.strip()
        data.append({"Version": version, "Date": date, "URL": url})

driver.quit()

pd.DataFrame(data).to_csv("dotnet_core8_versions.csv", index=False, encoding="utf-8-sig")
print(".NET Core 8 versions saved to dotnet_core8_versions.csv")
