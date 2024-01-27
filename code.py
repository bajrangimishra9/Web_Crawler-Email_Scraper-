import requests
from bs4 import BeautifulSoup
import re

# Define the URL of the webpage to scrape
url = 'https://thapar.edu/sitemap.xml'

# Send a GET request to the webpage
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all email addresses on the webpage using regular expressions
emails = re.findall(r'[\w\.-]+@[\w\.-]+', soup.get_text())

# Print the extracted email addresses
for email in emails:
    print(email)
