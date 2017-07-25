import urllib
from lxml import html
import requests

page = requests.get('https://blogs.msdn.microsoft.com/mssmallbiz/2016/07/10/free-thats-right-im-giving-away-millions-of-free-microsoft-ebooks-again-including-windows-10-office-365-office-2016-power-bi-azure-windows-8-1-office-2013-sharepoint-2016-sha/')
# displays the urls
tree = html.fromstring(page.content)
links = tree.xpath('//p/a')
for href in links:
    if href.text_content() == 'PDF':
        print(href.attrib['href'])
        try:
            response = urllib.request.urlopen(href.attrib['href'])
            file = open("D:/software/document_" + href.attrib['href'].split('/')[3] + ".pdf", 'wb')
            file.write(response.read())
            file.close()
            print("Completed")
        except:
            print("Oops!  Something goes wrong.  Try again...")


