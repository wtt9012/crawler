
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("1"))
#'/Interview/
for link in soup.find_all('a'):
    h = link.get("href")
    if h and h.encode("ascii", "ignore").startswith("/Interview"):
        print h