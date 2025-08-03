from flask import Flask, render_template, request
from scraper import fetch_case_details
import pymysql
from datetime import datetime

app = Flask(__name__)

MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Kjvm*7483',  # <-- CHANGE THIS
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

DB_NAME = 'court_data'

def init_db():
    # Step 1: Connect without selecting DB and create court_data if not exists
    conn = pymysql.connect(**MYSQL_CONFIG)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        conn.commit()
    finally:
        conn.close()

    # Step 2: Connect to court_data and create table if not exists
    conn = pymysql.connect(database=DB_NAME, **MYSQL_CONFIG)
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS case_results (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    case_type VARCHAR(50),
                    case_number VARCHAR(50),
                    filing_year VARCHAR(10),
                    serial_no VARCHAR(10),
                    case_no TEXT,
                    judgment_date VARCHAR(50),
                    parties TEXT,
                    pdf_url TEXT,
                    timestamp DATETIME
                );
            """)
        conn.commit()
    finally:
        conn.close()

def save_results_to_db(case_type, case_number, filing_year, results):
    conn = pymysql.connect(database=DB_NAME, **MYSQL_CONFIG)
    try:
        with conn.cursor() as cursor:
            for item in results:
                cursor.execute("""
                    INSERT INTO case_results 
                    (case_type, case_number, filing_year, serial_no, case_no, judgment_date, parties, pdf_url, timestamp)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())
                """, (
                    case_type,
                    case_number,
                    filing_year,
                    item['serial_no'],
                    item['case_no'],
                    item['judgment_date'],
                    item['parties'],
                    item['pdf_url']
                ))
        conn.commit()
    finally:
        conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            case_type = request.form['case_type']
            case_number = request.form['case_number']
            filing_year = request.form['filing_year'] 
            results = fetch_case_details(case_type, case_number, filing_year)
            save_results_to_db(case_type, case_number, filing_year, results)
            return render_template('result.html', results=results)
        except Exception as e:
            error_message = str(e)
            print("Error during scraping:", error_message)
            return render_template('result.html', results=[], error=f"Sorry, an error occurred while scraping: {error_message}")
    return render_template('index.html')


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
