from flask import Flask, render_template, request
import sqlite3
from scraper import fetch_case_details
from scraper import fetch_case_details


app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('data/queries.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    case_type TEXT,
                    case_number TEXT,
                    filing_year TEXT,
                    raw_response TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']

        # Fetch scraped case details
        result = fetch_case_details(case_type, case_number, filing_year)

        # Log input and output
        conn = sqlite3.connect('data/queries.db')
        c = conn.cursor()
        c.execute('INSERT INTO logs (case_type, case_number, filing_year, raw_response) VALUES (?, ?, ?, ?)',
                  (case_type, case_number, filing_year, str(result)))
        conn.commit()
        conn.close()

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
