from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def fetch_case_details(case_type, case_number, year):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://delhihighcourt.nic.in")

        # Click "Judgments"
        page.click('xpath=//*[@id="block-delhihighcourt-views-block-ser-block-1"]/div/div/div/div/ul/li[9]/a')
        page.wait_for_load_state("networkidle")

        # Select values from dropdowns
        page.select_option('xpath=//*[@id="case_type"]', label=case_type)
        page.fill('xpath=//*[@id="case_number"]', case_number)
        page.select_option('xpath=//*[@id="year"]', label=year)

        # Get captcha directly from span tag
        captcha_text = page.inner_text('xpath=//*[@id="captcha-code"]')
        page.fill('xpath=//*[@id="captchaInput"]', captcha_text)

        # Submit the form
        page.click('xpath=//*[@id="search"]')
        page.wait_for_load_state("networkidle")
        time.sleep(3)
        # Parse response with BeautifulSoup
        html = page.content()
        soup = BeautifulSoup(html, 'html.parser')

        rows = soup.select('#s_judgeTable > tbody > tr')
        results = []

        for row in rows:
            cols = row.find_all('td')
            print("cols",cols)
            if len(cols) >= 5:
                s_no = cols[0].text.strip()
                print("Sno:",s_no)
                case_no = cols[1].text.strip()
                judgment_date = cols[2].text.strip()
                a_tags = cols[2].find_all('a')
                if a_tags:
                    first_text = a_tags[0].text.strip()
                    judgment_date = first_text.split()[0]  # Extract '29-07-2025'
                    pdf_url = a_tags[0]['href']
                else:
                    judgment_date = ''
                    pdf_url = None
                # link_tag = cols[2].find('a')
                # pdf_url = link_tag['href'] if link_tag else None
                parties = cols[3].text.strip()
                # corrigendum_link = cols[4].find('a')
                # pdf_url = corrigendum_link['href'] if corrigendum_link else None

                results.append({
                    "serial_no": s_no,
                    "case_no": case_no,
                    "judgment_date": judgment_date,
                    "parties": parties,
                    "pdf_url": pdf_url
                })

            print("Results:",results)

        browser.close()

        return results if results else [{"error": "No judgment data found for given inputs."}]
