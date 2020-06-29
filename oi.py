import requests as req
from bs4 import BeautifulSoup as bs

url = 'http://www.digitalinnovation.one'\

pega= req.get(url)

obj_soup = bs(pega.text ,'html.parser')

z = obj_soup.find(class_='document')

print(z.text)