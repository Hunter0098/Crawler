from FetchHTML import *
from Find_links import Gethtml
from FileOperations import set_to_file

def crawling(chooseMethod,base_url,url,toCrawlPath):
    if chooseMethod == 1:
        websitesHTML = gethtml_urllib(url)
    else:
        websitesHTML = gethtml_requests(url)

    gethtml = Gethtml(base_url,url)
    try:
        gethtml.feed(websitesHTML)
    except Exception as e:
        print("\n\nAn error occurred: "+str(e)+"\n\n")

    mainLinksSet = set()
    mainLinksSet = gethtml.linksSet

    set_to_file(mainLinksSet,toCrawlPath)