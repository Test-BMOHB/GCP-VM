from lxml import html
from lxml.etree import tostring
from datetime import datetime
import requests, csv, re, time
liHTML = []
##  Function to scrap info from toronto.backpage.com
def scrapInfo(mainURL, mainContent, xPath):
    global liHTML
    li = []
    mainLinksXPath = mainContent.xpath(xPath)
    for mainLinksElements in mainLinksXPath:
        link = tostring(mainLinksElements)
##  Takes out <a href="
        link = link[9:]
##	Splits text on spaces
        link = link.split()
        link = link[0]
        link = link.split('">')
##  Only grab the link and not the rest of the HTML 'a' tag
        link = link[0]
##	Takes '/' off end of mainURL
        url = mainURL[:-1]
        if re.search(url, link) is None:
            link = url + link
##  Moves past pages that have are not postings
        if re.search("https://my.backpage.com/classifieds", link) is not None or re.search("http://toronto.backpage.com/adult/?page=", link) is not None or re.search("http://my.backpage.com/classifieds", link) is not None or re.search(mainURL, link) is None:
            continue
        phoneNumber = []
        linkRequest = requests.get(link)
        linkContent = html.fromstring(linkRequest.content)
##  Only grabs HTML tags with class = "postingBody"
        linkXPath = linkContent.xpath('//*[@class="postingBody"]')
        for linkXElement in linkXPath:
            phoneNumber = []
            text = tostring(linkXElement)
            pageHTML = text
##  Take out small icons in text
            icons = re.findall(r'&#\d*;', text)
            for icon in icons:
                text = re.sub(icon, '', text)
##  Take out HTML tags             
            tags = re.findall('<[^>]+>', text)
            for tag in tags:
##                tag = '<' + tag + '>'
##                if '(' in tag or ')' in tag:
##                    print tag
                text = text.replace(tag, '')
##  Take out whitespace
            text = re.sub('\s*', '', text)
##  Make numbers from words
            numReplace = re.compile(re.escape('zero'), re.IGNORECASE)
            text = numReplace.sub('0', text)
            numReplace = re.compile(re.escape('one'), re.IGNORECASE)
            text = numReplace.sub('1', text)
            numReplace = re.compile(re.escape('two'), re.IGNORECASE)
            text = numReplace.sub('2', text)
            numReplace = re.compile(re.escape('three'), re.IGNORECASE)
            text = numReplace.sub('3', text)
            numReplace = re.compile(re.escape('four'), re.IGNORECASE)
            text = numReplace.sub('4', text)
            numReplace = re.compile(re.escape('five'), re.IGNORECASE)
            text = numReplace.sub('5', text)
            numReplace = re.compile(re.escape('six'), re.IGNORECASE)
            text = numReplace.sub('6', text)
            numReplace = re.compile(re.escape('seven'), re.IGNORECASE)
            text = numReplace.sub('7', text)
            numReplace = re.compile(re.escape('eight'), re.IGNORECASE)
            text = numReplace.sub('8', text)
            numReplace = re.compile(re.escape('nine'), re.IGNORECASE)
            text = numReplace.sub('9', text)
            numReplace = re.compile(re.escape('ten'), re.IGNORECASE)
            text = numReplace.sub('10', text)
            numReplace = re.compile(re.escape('twenty'), re.IGNORECASE)
            text = numReplace.sub('20', text)
            numReplace = re.compile(re.escape('thirty'), re.IGNORECASE)
            text = numReplace.sub('30', text)
            numReplace = re.compile(re.escape('fourty'), re.IGNORECASE)
            text = numReplace.sub('40', text)
            numReplace = re.compile(re.escape('fifty'), re.IGNORECASE)
            text = numReplace.sub('50', text)
            numReplace = re.compile(re.escape('sixty'), re.IGNORECASE)
            text = numReplace.sub('60', text)
            numReplace = re.compile(re.escape('seventy'), re.IGNORECASE)
            text = numReplace.sub('70', text)
            numReplace = re.compile(re.escape('eighty'), re.IGNORECASE)
            text = numReplace.sub('80', text)
            numReplace = re.compile(re.escape('ninety'), re.IGNORECASE)
            text = numReplace.sub('90', text)
##  Finds phone numbers in the text within the HTML
##  10 digit regex
            phonenumbers = re.findall(r'\d{3}[^a-zA-Z]*\d{3}[^a-zA-Z]*\d{4}|\d[.]*\d[.]*\d[.]*\d[.]*\d[.]*\d[.]*\d[.]*\d[.]*\d[.]*\d|\d[-]*\d[-]*\d[-]*\d[-]*\d[-]*\d[-]*\d[-]*\d[-]*\d[-]*\d',text)
##  11 digit regex
            if not phonenumbers:
                phonenumbers = re.findall(r'1\d{3}[^a-zA-Z]*\d{3}[^a-zA-Z]*\d{4}|1[.]*\d[.]*\d[.]*\d[.]*\d[.]*\d[.]*\d[.]*\d[.]*\d[.]*\d[.]*\d|1\d[-]*\d[-]*\d[-]*\d[-]*\d[-]*\d[-]*\d[-]*\d[-]*\d[-]*\d',text)
            if phonenumbers:
                for number in phonenumbers:
                    number = number.replace(' ','')
                    number = number.replace('(','')
                    number = number.replace(')','')
                    number = number.replace('-','')
                    number = number.replace('.','')
                    number = number.replace('*','')
                    number = number.replace('~','')
                    if len(number) == 10 or len(number) == 11:
                        phoneNumber.append(number)
##                      phoneWriter.writerow([number])
##  If phonenumbers list is blank
            else:
                liHTML.append([pageHTML])
##  Only grabs HTML 'a' tags in the tags that have class = "postingBody"
        emailAddress = []
        websiteLink = []
        linkXPath = linkContent.xpath('//*[@class="postingBody"]/a')
        for linkXElement in linkXPath:
            emailAddress = []
            websiteLink = []
            textA = tostring(linkXElement)
            if 'mailto:' in textA:
                start = textA.find('"mailto:')
                end = textA.find('">')
                if start != -1 and end != -1:
                    textA = textA[start+8:end]
                    emailAddress.append(textA)
##                    emailWriter.writerow([textA])
            if 'http' in textA:
                start = textA.find('http')
                end = textA.find('">')
                if start != -1 and end != -1:
                    textA = textA[start:end]
                    websiteLink.append(textA)
##                    webWriter.writerow([textA])
##  Adds list item
        li.append([phoneNumber,emailAddress,websiteLink,link])
    return li

##  Function to remove duplicate list entries
def removeDuplicates(dedup):
    count1 = 0
    finalList = []
    print len(dedup)
    for i in dedup:
        count2 = 0
        for e in dedup:
##  Don't compare the same exact list index
            if count1 == count2:
                continue
            else:
## If all information is the same, delete the list entry
                if i == e:
                    dedup.pop(count2)
## If all information is the same except for the backpage link, delete the list entry
                if i[0] is not None and e[0] is not None:
                    if i[1] is not None and e[1] is not None:
                        if i[2] is not None and e[2] is not None:
                            if i[0] == e[0] and i[1] == e[1] and i[2] == e[2]:
                                dedup.pop(count2)
                        else:
                            if i[0] == e[0] and i[1] == e[1]:
                                dedup.pop(count2)
                    elif i[2] is not None and e[2] is not None:
                        if i[0] == e[0] and i[2] == e[2]:
                                dedup.pop(count2)
                    else:
                        if i[0] == e[0]:
                                dedup.pop(count2)
            count2 = count2 + 1
        count1 = count1 + 1
    for i in dedup:
        finalList.append(i)
    print len(finalList)
    return finalList

##  Function to create the CSV file
def createCSV(liCSV, f1):
    writer = csv.writer(f1, delimiter=',', quoting=csv.QUOTE_NONE, escapechar=' ')
##  Add a header row
    writer.writerow(["PhoneNumber","Email Address", "Website", "BackPage Link"])
    for i in liCSV:
        rowStr = ''
        for n in i:
            if isinstance(n, list):
                countE = 0
                for e in n:
                    if countE == 0:
                        rowStr = rowStr + e
                    else:
                       rowStr = rowStr + ':' + e
                    countE = countE + 1
            else:
                rowStr = rowStr + n
            rowStr = rowStr + ","
        writer.writerow([rowStr])

##  Start timer
def startTimer():
    start = time.time()
    return start

##  End timer and print
def endTimer(st):
    end = time.time()
    tot = end - st
    tot = ("{0:.1f}".format(round(tot,2)))
    print "It took " + str(tot) + " seconds to complete process."

##  Main Function
def main():
    global liHTML
    startTime = time.time()
    mainURL = "http://toronto.backpage.com/"
    currDate = datetime.now().strftime('%Y-%m-%d')
    liData = []
    increment = 1
##  Increment through 999 possible pages
    while increment < 1000:
        print "Page: " + str(increment)
        if increment == 1:
            mainRequest = requests.get(mainURL + "adult/")
        else:
##  To only print one page, change the increment if statement to == 2
##  To print all page's in a day, comment out the if statement below
            if increment == 3:
                currDate = ''
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
            startT = startTimer()
            print "Main Scrap"
            liData.extend(scrapInfo(mainURL, mainContent, '/html/body/div//*[@href]'))
            endTimer(startT)
##  Extend liData to include anything from the sponsorBoxContent xPath
            startT = startTimer()
            print "Sponsor Scrap"
            liData.extend(scrapInfo(mainURL, mainContent, '//*[@class="sponsorBoxContent"]/a'))
            endTimer(startT)
        else:
            startT = startTimer()
            print "Remove Dups from Scrap"
            liData = removeDuplicates(liData)
            endTimer(startT)
            startT = startTimer()
            print "Remove Dups from HTML"
            liHTML = removeDuplicates(liHTML)
            endTimer(startT)
            with open('ScreenScrap.csv','w') as scrapFile:
                startT = startTimer()
                print "Create CSV for Scrap"
                createCSV(liData, scrapFile)
                endTimer(startT)
            with open('Text.csv','w') as htmlFile:
                startT = startTimer()
                print "Create CSV for HTML"
                createCSV(liHTML, htmlFile)
                endTimer(startT)
            endTime = time.time()
            totTime = endTime - startTime
            totTime = ("{0:.1f}".format(round(totTime,2)))
            print "It took " + str(totTime) + " seconds to complete today's pages."
            exit()
        increment = increment + 1

##  Run main
main()
