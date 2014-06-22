import urllib
import xml.etree.ElementTree as ET
import re

class Article(object):

    def __init__(self, title,link,abstract,authors):

        new_title = re.sub('\(([^)]*)\)','', title)
        self.title = new_title

        self.link = link
        
        abstract = re.sub('<[^>]*>','',abstract)
        abstract = abstract.replace('\n', ' ')
        abstract = abstract.strip()
        self.abstract = abstract

        authors = re.sub('<[^>]*>','',authors)
        authors = authors.strip()
        self.authors = authors

        self.group = re.findall('\[([^]]*)\]', title)[0]

    def getTitle(self):
        return self.title

    def getLink(self):
        return self.link

    def getAbstract(self):
        return self.abstract

    def getAuthors(self):
        return self.authors

def get_artlist():
    url = 'http://export.arxiv.org/rss/astro-ph'

    data = urllib.urlopen(url).read()
    root = ET.fromstring(data)

    artList = []

    for n,item in enumerate(root):
        if n > 1:
            artList.append(Article(item[0].text,item[1].text,item[2].text,item[3].text))

    return artList
    
def print_titles(art_list,group='all'):
    '''Possible groups are astro-ph.GA, astro-ph.SR, astro-ph.IM, astro-ph.CO, 
    astro-ph.HE, astro-ph.HE'''

    if group == 'all':
        for n, art in enumerate(art_list):
            print str(n) + ':' + art.title + '\n'
    else:
        for n, art in enumerate(art_list):
            if art.group == 'astro-ph.'+group:
                print str(n) + ':   ' + art.title + '\n'
    
    return

################################################
if __name__ == '__main__':

    artList = get_artlist()

    print_titles(artList, 'GA')
    print_titles(artList, 'CO')