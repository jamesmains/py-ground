import requests
from bs4 import BeautifulSoup

# Set URL to target site
url = "http://quotes.toscrape.com"

# Get the response from URL
response = requests.get(url)

# Init soup with response
soup = BeautifulSoup(response.text, "html.parser")

# Scrape for quotes
quotes = soup.find_all("span",class_="text")

# Decorative line
print(f"--- Top Quotes from {url} ---\n")

# Print all fetched quotes
for i, quote in enumerate(quotes, 1):
    print(f"{i}. {quote.text}")