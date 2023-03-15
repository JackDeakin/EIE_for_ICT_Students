import requests
from bs4 import BeautifulSoup
import csv

query = "deliver entrepreneurship education to ict students"
max_results = 1000
url_template = "https://scholar.google.com/scholar?start={}&q={}&hl=en&as_sdt=0,5"

articles = []
start = 0

while start < max_results:
    url = url_template.format(start, query)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for result in soup.select(".gs_ri"):
        title = result.select_one(".gs_rt").text
        authors = result.select_one(".gs_a").text
        year = result.select_one(".gs_a").text.split(",")[-1].strip()
        abstract = result.select_one(".gs_rs").text
        url = result.select_one(".gs_rt a")
        url = url["href"] if url else ""
        keywords = result.select_one(".gs_kd").text if result.select_one(".gs_kd") else ""
        articles.append((title, authors, year, keywords, abstract, url))

    start += 10

with open("articles.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Authors", "Year", "Keywords", "Abstract", "URL"])
    for article in articles:
        writer.writerow(article)

print(f"Found {len(articles)} articles and saved them to articles.csv.")

