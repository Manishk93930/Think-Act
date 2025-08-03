# Court Data Fetcher & Mini-Dashboard

This project is a web application built using **Flask** and **Playwright** that scrapes court case metadata from Indian court websites (e.g., Delhi High Court) based on user input. The data is stored in a MySQL database and displayed in a user-friendly dashboard.

## Features

- Fetches court case details using:
  - Case Type
  - Case Number
  - Filing Year
- Automatically extracts structured metadata including:
  - Serial Number  
  - Case Number  
  - Petitioner and Respondent  
  - Judge  
  - Listing Date and Judgment Date  
  - Judgment PDF link
- Stores all successful queries and results in a MySQL database.
- Presents scraped data in a clean HTML table using Jinja2 templating.
- Displays alert messages in case of scraping failure or timeout.
- Includes navigation between the search page and results display.

## Technology Stack

- **Backend**: Python, Flask  
- **Web Scraping**: Playwright (Python)  
- **Database**: MySQL  
- **Frontend**: HTML, CSS (Jinja2 templating)

## Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Manishk93930/Think-Act.git
cd Think-Act/court-data-fetcher
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 4. Configure Database Credentials

Open `main.py` and update the following section with your MySQL configuration:

```python
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database_name',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}
```

Alternatively, you can use environment variables and `python-dotenv` for better security.

## Usage

### Start the Flask Server
```bash
python main.py
```

- Navigate to `http://127.0.0.1:5000` in your browser.
- Input the court case details.
- View results in the dashboard after scraping.

## License

This project is licensed under the MIT License.
