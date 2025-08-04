# court-dashboard
"Scraper that fetches real-time court case details from the Pune District Court eCourts website using Selenium and ChromeDriver."
# 🏛️ Court Dashboard – Pune District Court Scraper

This project fetches **real case data** from the [Pune District Court eCourts website](https://districts.ecourts.gov.in/pune) using **Selenium** and **ChromeDriver**.  
Users input **Case Type, Number, and Filing Year**, solve the CAPTCHA manually in a browser, and view extracted case metadata like parties, judge, status, and more.  


---

## ⚖️ Court Targeted

- **Court Name**: Pune District Court (Maharashtra)
- **Official Site**: https://services.ecourts.gov.in/ecourtindia_v6/
- **Search Method Used**: Case Type + Case Number + Filing Year

---

## 🔐 CAPTCHA Handling Strategy

- ✅ CAPTCHA is **not bypassed** or automated
- CAPTCHA is entered **manually** inside the Chrome browser opened by Selenium
- Ensures ethical use and complies with the court’s website usage terms

---

## 🧰 Tech Stack

- **Python 3.9+**
- **Selenium**
- **ChromeDriver**
- **BeautifulSoup**
- **SQLite**
- **python-dotenv**

---

## 📁 Folder Structure
Court_dashboard/
├── app.py # (Optional) Interface script
├── scraper.py # Main Selenium scraper logic
├── chromedriver.exe # Required ChromeDriver executable
├── data/ # Folder to store logs or case data
├── templates/ # (Optional) HTML templates for UI
├── venv/ # Python virtual environment
└── README.md # Project documentation

---

## ⚙️ Setup Instructions

1. Clone the Project

```bash
git clone https://github.com/gollapudirakshitha/court-dashboard
cd Court_dashboard

2. Create & Activate Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies

```bash
pip install -r requirements.txt
If requirements.txt is missing, install manually:
pip install selenium beautifulsoup4 python-dotenv

4. Download and Set Up ChromeDriver

Download from: https://chromedriver.chromium.org/downloads

Ensure version matches your installed Chrome browser

Place the file as chromedriver.exe in the project directory
Create a file named .env inside your project folder with:
CHROMEDRIVER_PATH=chromedriver.exe
DB_PATH=data/case_logs.db

▶️ How to Run
```bash
python scraper.py

A Chrome browser window will open using Selenium
Enter the Case Type, Case Number, and Filing Year
Manually enter the CAPTCHA when prompted
The scraped case details will be displayed in the terminal

```bash
python app.py

| Field       | Example |
| ----------- | ------- |
| Case Type   | CC      |
| Case Number | 1234    |
| Filing Year | 2022    |

📹 Demo Video
c:\Users\Sai Avinash\Downloads\Court_dashboard\demo video.mkv

📸 Screenshot Placeholder
c:\Users\Sai Avinash\Downloads\Court_dashboard\screenshot_result.png
Chrome window with CAPTCHA
Result display in terminal/UI

👩‍💻 Author
Gollapudi Rakshitha.
Email: gollapudirakshitha@gmail.com






