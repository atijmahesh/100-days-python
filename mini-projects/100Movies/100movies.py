import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(r.text, "html.parser")
titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

title_texts = []
for t in titles:
    title_texts.append(t.getText())

title_texts = title_texts[::-1]

with open("./movies.txt", mode="w") as f:
    for line in title_texts:
        f.write(f"{line}\n")