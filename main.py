import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5TNJHG/ref=sr_1_1?dchild=1&keywords=iphone&qid=1621914655&sr=8-1"

r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup)
print(soup.prettify)

title = soup.title
#print(title)
#print(type(title))
#print(type(title.string))

paras = soup.find_all('p')
#print(paras)

anchors = soup.find_all('a')
#print(anchors)

#print(soup.find('p').get_text())

#print(soup.get_text())

#for all links on page
#for link in anchors:
#   print(link.get('href'))

for a in soup.findAll('a',href=True):
    price=a.find('div', attrs={'class':'a-size-medium a-color-price priceBlockDealPriceString'})
    print(price)

