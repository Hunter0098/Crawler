import os

#Create the project folder if it doesn't exist
def makeFolder(projectName):
    if not os.path.exists(projectName):
        os.mkdir(projectName)
        print("Starting new project..\n")
    else:
        print("Project already exists..\nTrying to continue..")

#Create project files that contain links to crawl and the ones that have been crawled
def makeFiles(projectName,baseUrl):
    toCrawl = os.path.join(projectName,"toCrawl.txt")   #Here toCrawl = projectName/toCrawl.txt
    crawled = os.path.join(projectName,"crawled.txt")
    backup_crawledPath = os.path.join(projectName,"backup_crawled.txt")
    #Now create them if they don't exist
    if not os.path.isfile(toCrawl):
        write_in_file(toCrawl,baseUrl)
    if not os.path.isfile(crawled):
        write_in_file(crawled,"")
    if not os.path.isfile(backup_crawledPath):
        write_in_file(backup_crawledPath,"")

    return toCrawl,crawled,backup_crawledPath

#Write_in_file function
def write_in_file(path,data):
    fobject = open(path,'w',encoding='utf-8')
    fobject.write(data)
    fobject.close()

#Append to file
def append_to_file(path,data):
    fobject = open(path,'a',encoding='utf-8')
    fobject.write(data)
    fobject.close()

#Read file and add each line to set
def file_to_set(filename):
    results = set()               #Sets don't allow adding duplicate elements
    fobject = open(filename,'r')
    for line in fobject:
        results.add(line.replace('\n',''))
    fobject.close()
    return results

#Write the data in the set to the file
def set_to_file(linkset,filename):
    fobject = open(filename,'a',encoding = 'utf-8') #Without encoding='utf-8', we may get UnicodeEncodeError
    for line in sorted(linkset):
        fobject.write(line+"\n")
    fobject.close()

#Make the file empty
def make_file_empty(path):
    fobject = open(path,'w',encoding='utf-8')
    fobject.close()
