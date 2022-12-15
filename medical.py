import re
import requests
from bs4 import BeautifulSoup
url='https://pubmed.ncbi.nlm.nih.gov/?term='
inp=input('enter the any query-regarding the medical field..: ')
text=requests.get(f'https://pubmed.ncbi.nlm.nih.gov/?term={inp}').text
#print(text)
link=[]
urls=[]
output=[]
soap=BeautifulSoup(text,'html.parser')
for links in soap.find_all('a',href=True):
    tex=links['href']
    link.append(tex)
urls.append(link[38:48])
med='https://pubmed.ncbi.nlm.nih.gov'
for i in range(10):
    txt=requests.get(med+urls[0][i]).text
    soap=BeautifulSoup(txt,'html.parser')
    for links in soap.find_all('div',id='eng-abstract'):
        tex=links.get_text()
        #print(tex)
        output.append(tex)
for i in output:
    text=re.sub('\n','',i)
    print(text)
#sentence summarizer has to be done
