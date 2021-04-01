import requests
from bs4 import BeautifulSoup


def busqOCLC(isbn):
    host = "http://classify.oclc.org/classify2/ClassifyDemo?search-standnum-txt="

    search = host + isbn

    r = requests.get(search)

    if r.status_code == 200:
        c = r.content
    else:
        print(r.status_code)

    return BeautifulSoup(c, 'html.parser')


def busqWorldCat(isbn):
    host = "https://www.worldcat.org/search?q=bn%3A"

    search = host + isbn

    r = requests.get(search)

    if r.status_code == 200:
        c = r.content
    else:
        print(r.status_code)

    resultado = BeautifulSoup(c, 'html.parser')

    divi = resultado.find('div', class_="name")

    for en in divi.find_all('a', {'id': 'result-1'}):
        item_url = "https://www.worldcat.org" + en['href']
        new_r = requests.get(item_url)
        new_c = new_r.content
        return BeautifulSoup(new_c, 'html.parser')


def dewey_code(isbn):
    sopa = busqOCLC(isbn)
    tabla = sopa.find("table", class_="dataTable")
    return [t.text for t in tabla.find_all('td')][1]


def catalogo(isbn):
    sopa = busqWorldCat(isbn)
    titulo = [t for t in sopa.find('h1', class_="title")][0]
    autor = sopa.find('td', {'id': 'bib-author-cell'})
    editorial = [ed for ed in sopa.find('td', {'id': 'bib-publisher-cell'})][0]
    clasificacion = dewey_code(isbn)
    try:
        texto_autor = autor.text
    except AttributeError:
        texto_autor = ""

    catalogo = {
        "clasificación": clasificacion,
        "autoría": texto_autor,
        "título": titulo,
        "editorial": editorial,
        "ISBN": isbn
    }

    return catalogo

'''
barra = "9781609621117"

print(type(catalogo(barra)))
'''