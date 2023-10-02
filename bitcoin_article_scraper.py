import os
import re
import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By

# Create a directory to store article texts if it doesn't exist
if not os.path.exists("article_texts"):
    os.makedirs("article_texts")

# Define a function to convert relative time to formatted date
def convert_relative_time(date_time):
    now = datetime.now()
    if "hours" in date_time:
        hours = int(date_time.split()[0])
        publication_date = now - timedelta(hours=hours)
    elif "days" in date_time:
        days = int(date_time.split()[0])
        publication_date = now - timedelta(days=days)
    elif "weeks" in date_time:
        weeks = int(date_time.split()[0])
        publication_date = now - timedelta(weeks=weeks)
    elif "month" in date_time:
        months = int(date_time.split()[0])
        publication_date = now - timedelta(days=months * 30)
    else:
        publication_date = now

    return publication_date.strftime("%B %Y")

# Define a function to collect paragraph texts
def collect_paragraph_texts(link):

    paragraph_texts = []
    driver.execute_script("window.open('{}', '_blank');".format(link))
    driver.switch_to.window(driver.window_handles[1])

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.content-inner p"))
        )
        paragraphs = driver.find_elements(By.CSS_SELECTOR, "div.content-inner p")
        for paragraph in paragraphs:
            paragraph_texts.append(paragraph.text)
    except TimeoutException:
        print("Timeout: Unable to load content for link:", link)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return paragraph_texts

loop_count, total_time, index = 0, 0, 1028
unwanted_elements = {"BitStarz", "Punt Casino", "Trust Dice", "mBit"}
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('./chromedriver', options=chrome_options)


skipped_file_path = os.path.join("article_texts", "skipped_count.txt")
if not os.path.exists(skipped_file_path):
    with open(skipped_file_path, "w") as skipped_file:
        skipped_file.write("0")
    skipped_count = 0
else:
    with open(skipped_file_path, "r") as skipped_file:
        skipped_count = int(skipped_file.read().strip())

# saves results into file
def sanitize_filename(article_name):
    # Remove characters that are not allowed in filenames
    sanitized_name = re.sub(r'[<>:"/\\|?*]', '', article_name)
    return sanitized_name

def save_results(article_name, index, author, date_time, link):
    paragraph_texts = collect_paragraph_texts(link)
    sanitized_name = sanitize_filename(article_name)
    file_path = os.path.join("article_texts", f"{sanitized_name}_{index}.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Title: {article_name}\n")
        file.write(f"Author: {author}\n")
        file.write(f"Date/Time: {date_time}\n")
        file.write(f"URL: {link}\n")
        file.write("Text:\n")
        file.write("".join(paragraph_texts))

# Loop through pages and collect article information
for page in range(106, 108):
    start_time = time.time()
    url = f"https://www.newsbtc.com/page/{page}/?s=bitcoin+"
    driver.get(url)
    driver.implicitly_wait(10)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("div", class_="jeg_postblock_content")

    print("Page\tArticle Number")
    for idx, article in enumerate(articles):
        try:
            name = article.find("h3", class_="jeg_post_title")
            article_name, author, link = "", "", ""
            if name.get_text().strip() not in unwanted_elements:
                article_name = name.get_text().strip()
                link = article.find("a")["href"]

            authors_element = article.find("div", class_="jeg_meta_author")
            if authors_element:
                author = authors_element.find("a").text

            try:
                date_element = article.find("div", class_="jeg_meta_date").find("a")
                date_time = date_element.text if date_element else "Unknown Date/Time"
            except AttributeError:
                date_time = "Unknown Date/Time"
            formatted_date = convert_relative_time(date_time)

            if article_name != "":
                save_results(article_name, index, author, formatted_date, link)
                index = index + 1
                print("{}\t\t{}".format(page, idx + 1))
        except StaleElementReferenceException:
            print("Stale element encountered, skipping...")
            skipped_count += 1
            continue

    elapsed_time = time.time() - start_time
    print("Processing completed for page {} in {} time".format(page, elapsed_time))
    total_time += elapsed_time

with open(skipped_file_path, "w") as skipped_file:
    skipped_file.write(str(skipped_count))

# Print the total number of articles and saved files
print(f"\nTotal number of articles: {index}")
print(f"Total number of saved text files: {len(os.listdir('article_texts'))}")
print(f"Total time taken: {total_time:.2f} seconds")
driver.quit()
