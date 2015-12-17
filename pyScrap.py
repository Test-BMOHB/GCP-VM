from lxml import html
from lxml.etree import tostring
from datetime import datetime
import requests, csv, re, time
##  Function to scrap info from toronto.backpage.com
def scrapInfo(mainURL, xPath):
    li = []
    mainLinksXPath = mainContent.xpath(xPath)
    for mainLinksElements in mainLinksXPath:
        link = tostring(mainLinksElements)
##  Takes out <a href="
        link = link[9:]
        link = link.split()
        link = link[0]
        link = link.split('">')
##  Only grab the link and not the rest of the HTML 'a' tag
        link = link[0]
##  Moves past pages that have are not postings
        url = mainURL[:-1]
        if re.search(url, link) is None:
            link = url + link
        if re.search("https://my.backpage.com/classifieds", link) is not None or re.search("http://toronto.backpage.com/adult/?page=", link) is not None or re.search("http://my.backpage.com/classifieds", link) is not None or re.search(mainURL, link) is None:
            continue
        phoneNumber = ''
        emailAddress = ''
        websiteLink = ''
        linkRequest = requests.get(link)
        linkContent = html.fromstring(linkRequest.content)
##  Only grabs HTML tags with class = "postingBody"
        linkXPath = linkContent.xpath('//*[@class="postingBody"]')
        for linkXElement in linkXPath:
            text = tostring(linkXElement)
##  Take out small icons in text
            icons = re.findall(r'&#\d*;', text)
            for icon in icons:
                text = re.sub(icon, '', text)
##  Take out HTML tags
##            tags = re.findall(r'<(.*?)>', text, re.DOTALL)
##            for tag in tags:
##                tag = '<' + tag + '>'
##                text = re.sub(tag, '', text)
##  Finds phone numbers in the text within the HTML
##  10 digit regex
            phonenumbers = re.findall(r'\d{3}\s\d{3}\s\d{4}|\d{3}[^;]\d{3}[^;]\d{4}|\d{3}[^;]\s\d{3}[^;]\d{4}|\d{3}\s\d{7}|\d{3}[^;]\d{7}|\d{10}|\d{3}\s\d{3}\s\d{2}\s\d{2}|\d{3}\S*\s\d{3}\s\S*\d{4}',text)
##  If phonenumbers list is blank
            if not phonenumbers:
##  11 digit regex
                phonenumbers = re.findall(r'1\d{3}\s\d{3}\s\d{4}|1\d{3}[^;]\d{3}[^;]\d{4}|1\d{3}[^;]\s\d{3}[^;]\d{4}|1\d{3}\s\d{7}|1\d{3}[^;]\d{7}|1\d{10}|1\d{3}\s\d{3}\s\d{2}\s\d{2}|1\d{3}\S*\s\d{3}\s\S*\d{4}',text)
            else:
                for number in phonenumbers:
                    number = number.replace(' ','')
                    number = number.replace('(','')
                    number = number.replace(')','')
                    number = number.replace('-','')
                    number = number.replace('.','')
                    number = number.replace('*','')
                    number = number.replace('~','')
                    if len(number) == 10 or len(number) == 11:
                        phoneNumber = number
##                      phoneWriter.writerow([number])
##  Only grabs HTML 'a' tags in the tags that have class = "postingBody"
        linkXPath = linkContent.xpath('//*[@class="postingBody"]/a')
        for linkXElement in linkXPath:
            textA = tostring(linkXElement)
            if 'mailto:' in textA:
                start = textA.find('"mailto:')
                end = textA.find('">')
                if start != -1 and end != -1:
                    textA = textA[start+8:end]
                    emailAddress = textA
##                    emailWriter.writerow([textA])
            if 'http' in textA:
                start = textA.find('http')
                end = textA.find('">')
                if start != -1 and end != -1:
                    textA = textA[start:end]
                    websiteLink = textA
##                    webWriter.writerow([textA])
##  Adds list item
        li.append([phoneNumber,emailAddress,websiteLink,link])
    return li

##  Function to remove duplicate list entries
def removeDuplicates(dedup):
    count1 = 0
    for i in dedup:
        count2 = 0
        for e in dedup:
##  Don't compare the same exact list index
            if count1 == count2:
                continue
            else:
                if i == e:
                    dedup.remove(e)
## If all information is the same except for the backpage link, delete the list entry
                elif i[0] == e[0] and i[1] == e[1] and i[2] == e[2] and i[3] != e[3]:
                    dedup.remove(e)
            count2 = count2 + 1
        count1 = count1 + 1
    return dedup

##  Function to create the CSV file
def createCSV(liCSV, f1):
    writer = csv.writer(f1, delimiter=',')
##  Add a header row
    writer.writerow(["PhoneNumber","Email Address", "Website", "BackPage Link"])
    for i in liCSV:
        writer.writerow(i)

startTime = time.time()
mainURL = "http://toronto.backpage.com/"
currDate = datetime.now().strftime('%Y-%m-%d')
liData = []
liHTML = []
increment = 1
##  Increment through 999 possible pages
while increment < 1000:
    print "Page: " + str(increment)
    if increment == 1:
        mainRequest = requests.get(mainURL + "adult/")
    else:
##  To only print one page, comment out the mainRequest line and uncomment the break line                    
##        break
        mainRequest = requests.get(mainURL + "adult/?page=" + str(increment))
    mainContent = html.fromstring(mainRequest.content)
    date = mainContent.xpath('//*[@class="date"]')
    for dateStr in date:
        dateStr = tostring(dateStr)
        dateStr = re.search("\w{3}. \w{3}. \d{2}", dateStr)
        dateStr = datetime.strptime(dateStr.group(), '%a. %b. %d').date()
        dateStr = dateStr.replace(year=datetime.now().year)
        dateStr = dateStr.strftime('%Y-%m-%d')
##  Compare current date to date on webpage
    if dateStr == currDate:
        liData = scrapInfo(mainURL, '/html/body/div//*[@href]')
        liHTML = scrapInfo(mainURL, '//*[@class="sponsorBoxContent"]/a')
        liData = removeDuplicates(liData)
        liHTML = removeDuplicates(liHTML)
        with open('ScreenScrap.csv','w') as scrapFile:
            createCSV(liData, scrapFile)
        with open('Text.csv','w') as htmlFile:
            createCSV(liHTML, htmlFile)
    else:
        endTime = time.time()
        totTime = endTime - startTime
        totTime = ("{0:.1f}".format(round(totTime,2)))
        print "It took " + str(totTime) + " seconds to complete today's pages."
        exit()
    increment = increment + 1
