from bs4 import BeautifulSoup
import lxml
import requests

url = "https://www.gta.ufrj.br/grad/06_1/wap/"

#usando request

html = requests.get(url +"index.htm").text
soup = BeautifulSoup(html, "lxml")

lista_paginas = []
for i in soup.html.body.find_all('a'):
    nome_pagina = url + i.get('href')
    html = requests.get(nome_pagina).text
    soup = BeautifulSoup(html, 'lxml')
    lista_paginas.append(soup)

for s in lista_paginas:
    print(s.html.head.title.text)