from Bio import Entrez
from Bio import Medline

Entrez.email = 'octaviojmaia@gmail.com'
handle = Entrez.egquery(term = 'Legionella pneumophila')
record = Entrez.read(handle)

#number of articles
for row in record['eGQueryResult']:
    if row['DbName']=='pubmed':
        x = row['Count']
        
#places the articles in a list
handle = Entrez.esearch(db='pubmed', term='Legionella  pneumophila', retmax=x)
record = Entrez.read(handle)
idlist = record['IdList']

#fetch
handle = Entrez.efetch(db='pubmed', id=idlist, rettype='medline', retmode='text')
records = list(Medline.parse(handle))
results = open('resultados.txt', 'w')
for record in records:
    tit=('Title: ', record.get('TI', '?'))
    aut=('Authors: ', record.get('AU', '?'))
    sour=('Source: ', record.get('SO', '?'))
    
    results.write(str(tit)+'\n')
    results.write(str(aut)+'\n')
    results.write(str(sour)+'\n')
    results.write('---------------------\n')
results.close()