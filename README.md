# Court Data Fetcher & Mini-Dashboard

This project is a web application built using Flask and Playwright that scrapes court case metadata from Indian court websites (e.g., Delhi High Court) based on user input. It stores the results in a MySQL database and presents them in a user-friendly dashboard.

## Features

- Fetches court case details using Case Type, Case Number, and Filing Year.
- Automatically scrapes and extracts structured metadata including:
  - Serial Number
  - Case Number
  - Petitioner and Respondent
  - Judge
  - Listing Date and Judgment Date
  - Judgment PDF link
- Stores all successful queries and results in a MySQL database.
- Displays scraped data in a clean HTML table using Jinja templates.
- Handles timeout and scraping errors gracefully with user-friendly alert messages.
- Includes navigation between the result and search pages.

## Technology Stack

- **Backend**: Python, Flask
- **Web Scraping**: Playwright (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS (with Jinja templating)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Manishk93930/Think-Act.git
cd court-data-fetcher

### 2. Configure youre DB Credentials in main.py
