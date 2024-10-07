from bs4 import BeautifulSoup
import requests
import csv

# Fetch and parse the webpage
page_to_scrape = requests.get("https://quotes.toscrape.com/")
page_to_scrape.encoding = 'utf-8'  # Ensure UTF-8 encoding is used

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Extract quotes and authors
quotes = soup.find_all("span", attrs={"class": "text"})
authors = soup.find_all("small", attrs={"class": "author"})

# Open CSV file for writing with semicolon as the delimiter
with open("Quotes.csv", "w", newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')  # Use semicolon as delimiter

    # Write the header row
    writer.writerow(["Quotes", "Authors"])

    # Write quotes and authors to the CSV file, putting them in separate columns
    for quote, author in zip(quotes, authors):
        writer.writerow([quote.text.strip(), author.text.strip()])
