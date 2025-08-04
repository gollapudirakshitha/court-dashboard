from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def fetch_case_details(case_type, case_number, filing_year):
    try:
        options = Options()
        # Comment headless for visible testing
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1366,768")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115 Safari/537.36")

        driver = webdriver.Chrome(options=options)

        driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")
        time.sleep(7)  # give enough time for full CSS + JS load

        # Click "District Court"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "District Court"))
        ).click()

        # Select State: Maharashtra
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sess_state_code"))
        ).send_keys("Maharashtra")

        # Select District: Pune
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sess_dist_code"))
        ).send_keys("Pune")

        time.sleep(2)

        # Click "Case Status"
        driver.find_element(By.LINK_TEXT, "Case Status").click()
        time.sleep(2)

        # Switch to "Case Number" tab
        driver.find_element(By.ID, "tab1").click()

        # Fill in case details
        driver.find_element(By.ID, "case_type").send_keys(case_type)
        driver.find_element(By.ID, "case_no").send_keys(case_number)
        driver.find_element(By.ID, "case_year").send_keys(filing_year)

        # Click submit
        driver.find_element(By.NAME, "submit").click()
        time.sleep(5)

        # Try to find case result table
        try:
            table = driver.find_element(By.CLASS_NAME, "table_b")
        except:
            driver.quit()
            return {"error": "❌ Case not found or details are invalid."}

        # Parse rows
        rows = table.find_elements(By.TAG_NAME, "tr")
        result = {}

        for row in rows:
            try:
                tds = row.find_elements(By.TAG_NAME, "td")
                if len(tds) >= 2:
                    label = tds[0].text.strip().replace(":", "")
                    value = tds[1].text.strip()
                    result[label] = value
            except:
                continue

        driver.quit()
        return result if result else {"error": "No data found for the case."}

    except Exception as e:
        return {"Wait": "⏳ Opening court site in a browser tab... Please wait or retry if it fails."}