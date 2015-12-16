from lxml import html
from lxml.etree import tostring
from datetime import datetime
import requests, csv, re, time

def scrapPhoneNumbers(mainURL, xPath):
    mainLinksXPath = mainContent.xpath(xPath)
    count = 0
    for mainLinksElements in mainLinksXPath:
        link = tostring(mainLinksElements)
        link = link[9:]
        link = link.split()
        link = link[0]
        link = link.split('">')
        link = link[0]
        if re.search("https://my.backpage.com/classifieds", link) is not None:
            continue
        if re.search(mainURL, link) is None:
            continue
        if "http://toronto.backpage.com" not in link:
            link = "http://toronto.backpage.com" + link
        count = count + 1
        linkRequest = requests.get(link)
        linkContent = html.fromstring(linkRequest.content)
        linkXPath = linkContent.xpath('//*[@class="postingBody"]')
        for linkXElement in linkXPath:
            text = tostring(linkXElement)
            phonenumbers = re.findall(r'\d{3}\s\d{3}\s\d{4}|\d{3}\S\d{3}\S\d{4}|\d{3}\d{3}\d{4}|\d{3}\S\s\d{3}\S\d{4}|\d{3}\s\d{7}',text)
            if not phonenumbers:
                phoneWriter.writerow([link])
            else:
                for number in phonenumbers:
                    number = number.replace(' ','')
                    number = number.replace('(','')
                    number = number.replace(')','')
                    number = number.replace('-','')
                    number = number.replace('.','')
                    number = number.replace('*','')
                    if number[:1] == 1:
                        phoneWriter.writerow([link])
                        otherTextWriter.writerow([text])
                    elif len(number) == 10:
                        phoneWriter.writerow([number])
                    else:
                        phoneWriter.writerow([link])
                        otherTextWriter.writerow([text])
        linkXPath = linkContent.xpath('//*[@class="postingBody"]/a')
        for linkXElement in linkXPath:
            textA = tostring(linkXElement)
            if 'mailto:' in textA:
                start = textA.find('"mailto:')
                end = textA.find('">')
                if start != -1 and end != -1:
                    textA = textA[start+8:end]
                    emailWriter.writerow([textA])

with open('PhoneNumbers.csv','w') as phoneFile:
    with open('Emails.csv','w') as emailFile:
        with open('Text.csv','w') as otherTextFile:
            startTotTime = time.time()
            mainURL = "http://toronto.backpage.com/"
            currDate = datetime.now().strftime('%Y-%m-%d')
            phoneWriter=csv.writer(phoneFile)
            emailWriter=csv.writer(emailFile)
            otherTextWriter=csv.writer(otherTextFile)
            increment = 1
            while increment < 1000:
                print "Page: " + str(increment)
                if increment == 1:
                    mainRequest = requests.get(mainURL + "adult/")
                else:
                    mainRequest = requests.get(mainURL + "adult/?page=" + str(increment))
                mainContent = html.fromstring(mainRequest.content)
##	Current date
                date = mainContent.xpath('//*[@class="date"]')
                for dateStr in date:
                    dateStr = tostring(dateStr)
                    dateStr = re.search("\w{3}. \w{3}. \d{2}", dateStr)
                    dateStr = datetime.strptime(dateStr.group(), '%a. %b. %d').date()
                    dateStr = dateStr.replace(year=datetime.now().year)
                    dateStr = dateStr.strftime('%Y-%m-%d')
                if dateStr == currDate:
##	Start of Main Links
                    scrapPhoneNumbers(mainURL, '/html/body/div//*[@href]')
##	End of Main Links
##	Start of Sponsors Links
                    scrapPhoneNumbers(mainURL, '//*[@class="sponsorBoxContent"]/a')
##	End Sponsor Links
                else:
                    endTotTime = time.time()
                    totTime = endTotTime - startTotTime
                    totTime = ("{0:.1f}".format(round(totTime,2)))
                    print "It took " + str(totTime) + " seconds to complete today's pages."
                    exit()
                increment = increment + 1






##        x3 = c2.xpath('//*[@id="postingTitle"]')
##        for e2 in x2:
##            strE2 = tostring(e2)
##            writer.writerow(strE2)
##        for e3 in x3:
##            strE3 = tostring(e3)
##            writer.writerow(strE3)

##gsutil cp gs://web_crawler_bmo/PhoneNumbers.csv .
##gsutil cp PhoneNumbers.csv gs://web_crawler_bmo/
##gsutil cp Emails.csv gs://web_crawler_bmo/
##gsutil cp Text.csv gs://web_crawler_bmo/
