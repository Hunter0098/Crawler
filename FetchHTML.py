from urllib.request import urlopen
import requests

#Get html from a website using urlopen
def gethtml_urllib(link):
    try:
        response = urlopen(link)
        if 'text/html' in response.getheader('content-type'):
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
            return html_string
        else:
            print("Error in FetchHTML -> gethtml_urllib function\nCan be because the url specified may not contain HTML.")
            return ''
    except Exception as e:
        print("\nAn error occured in FetchHTML.py -> function gethtml_urllib saying:\n"+str(e)+"\nCan be because the url specified may not contain HTML.")
        return ''

#Get HTML from website using requests
def gethtml_requests(link):
    try:
        response = requests.get(link)
        return response.text
    except Exception as e:
        print("\nAn error occured in FetchHTML.py -> function gethtml_requests saying:\n"+str(e)+"\nCan be because the url specified may not contain HTML.")
        return ''
