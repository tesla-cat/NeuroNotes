import json
from scholarly import scholarly
from bs4 import BeautifulSoup
import warnings
warnings.simplefilter('ignore')

def splitStrip(x:str, sep): return [y.strip() for y in x.split(sep)]

def getAuthor(author = 'Giorgio Parisi'):
    try:
        search_query = scholarly.search_author(author)
        first_author_result = next(search_query)
        scholarly.pprint(first_author_result)
        return first_author_result
    except:
        pass

def getNobels():
    results = []
    def getAuthors(authors, field, year):
        for author in authors:
            res = getAuthor(author)
            if res:
                res['author'] = author
                res['year'] = year
                res['field'] = field
                results.append(res)
    with open('nobel.html','r',encoding='utf8') as f:
        nobel = f.read()
    soup = BeautifulSoup(nobel)
    trs = soup.find_all('tr')
    for tr in trs[1:-1]:
        tr:str = tr.get_text()
        cols = [c for c in splitStrip(tr, '\n') if c]
        if len(cols)==7:        
            Year = int(cols[0])
            if Year > 0:
                Physics = splitStrip(cols[1], ';')
                Chemistry = splitStrip(cols[2], ';')
                Medicine = splitStrip(cols[3], ';')
                print(Year, Physics, Chemistry, Medicine)
                getAuthors(Physics, 'Physics', Year)
                getAuthors(Chemistry, 'Chemistry', Year)
                getAuthors(Medicine, 'Medicine', Year)
                with open('nobel.json','w+') as f:
                    json.dump(results, f, indent=2)

getNobels()