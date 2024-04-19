from bs4 import BeautifulSoup
import requests


url = "https://www.newegg.com/pny-geforce-rtx-4090-vcg409024tfxpb1/p/N82E16814133849"


response = requests.get(url)
doc = BeautifulSoup(response.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")

print(strong.string)