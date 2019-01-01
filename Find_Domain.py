from urllib.parse import urlparse

def getDomainName(base_url):
    try:
        result = get_sub_domain_name(base_url).split('.')
        return (result[1].replace(result[1],result[1].capitalize()))
    except Exception as e:
        print (e)
        return ''

#Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''