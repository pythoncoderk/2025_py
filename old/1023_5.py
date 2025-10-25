import requests
from bs4 import BeautifulSoup

url = "https://www.ohtashp.com/topics/takarakuji/loto7/table.html"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

rows = soup.find_all("tr")

found = False
for r in rows:
    nums = [int(x) for x in r.text.split() if x.isdigit()]
    if set([1,2,3,4,5,6,7]).issubset(set(nums)):
        print("出現回号:", r.text)
        found = True

if not found:
    print("1,2,3,4,5,6,7 は過去に当選したことがありません。")
