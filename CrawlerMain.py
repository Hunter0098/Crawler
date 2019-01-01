from FileOperations import *
from Find_Domain import *
from Crawling import crawling

#Taking input from user
url = str(input("Please enter the url here: "))

directoryName = getDomainName(url)
domainName = directoryName
makeFolder(directoryName)
toCrawlPath,crawledPath,backup_crawledPath = makeFiles(directoryName,url)

chooseMethod = int(input("Which method you wish to use to fetch HTML:\n1 for urllib\n2 for requests (Recommended)\nEnter your choice here: "))

mainSet = set()
crawledSet = set()
crawledSet.add(url)

print("Crawling: \n"+url)
set_to_file(crawledSet,crawledPath)
crawling(chooseMethod,url,url,toCrawlPath)

while (True):
    mainSet = file_to_set(toCrawlPath)
    make_file_empty(toCrawlPath)

    #Terminating condition
    if(len(mainSet) == 0):
        print("All links crawled.")
        break

    #Take each link from mainSet and crawl it
    for linkInSet in mainSet:
        if domainName != getDomainName(linkInSet):
            print("Found link to external site..")
            continue
        if linkInSet in crawledSet:
            print("Duplicate link found..")
            continue
        
        crawling(chooseMethod,url,linkInSet,toCrawlPath)
        crawledSet.add(linkInSet)
        print(linkInSet)

    #Delete contents of crawled and write updated crawledset
    #Making backup before deleting
    if os.path.isfile(backup_crawledPath):
        os.remove(backup_crawledPath)   #Delete old backup

    os.rename(crawledPath,backup_crawledPath)   #Backup created

    make_file_empty(crawledPath)    #Delete the content of crawled.txt
    set_to_file(crawledSet,crawledPath) #Write new content
