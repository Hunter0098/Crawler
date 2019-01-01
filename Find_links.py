from html.parser import HTMLParser
from urllib import parse

class Gethtml(HTMLParser):
    def __init__(self,base_url,site_url):
        super().__init__()
        self.base_url = base_url
        self.site_url = site_url
        self.linksSet = set()
    def handle_starttag(self,tag,attrs):    #Read more about it here https://docs.python.org/3/library/html.parser.html
        if tag == 'a':
            for (attributes,value) in attrs:
                if attributes == 'href':
                    url = parse.urljoin(self.base_url,value)
                    self.linksSet.add(url)
