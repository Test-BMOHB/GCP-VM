from lxml import html
from lxml.etree import tostring
from datetime import datetime
import requests, csv, re, time
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
                startTime = time.time()
                print "Page: " + str(increment)
                if increment == 1:
                    mainRequest = requests.get(mainURL + "adult")
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
                    mainLinksXPath = mainContent.xpath('/html/body/div//*[@href]')
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
                        count = count + 1
                        linkRequest = requests.get(link)
                        linkContent = html.fromstring(linkRequest.content)
                        linkXPath = linkContent.xpath('//*[@class="postingBody"]')
                        for linkXElement in linkXPath:
                            text = tostring(linkXElement)
                            splitStrArr = text.split(' ')
                            for splitStr in splitStrArr:
                                start = splitStr.find('&')
                                end = splitStr.find(';')
                                if start != -1 and end != -1:
                                    splitStr = splitStr[start+1:end]
                                if re.search("\d{3}-\d{3}-\d{4}", splitStr) is not None \
                                or re.search("\d-\d{3}-\d{3}-\d{4}", splitStr) is not None \
                                or re.search("\d{3}/\d{3}/\d{4}", splitStr) is not None \
                                or re.search("\d/\d{3}/\d{3}/\d{4}", splitStr) is not None \
                                or re.search("\d{3}.\d{3}.\d{4}", splitStr) is not None \
                                or re.search("\d.\d{3}.\d{3}.\d{4}", splitStr) is not None \
                                or re.search("(\d{3})-\d{3}-\d{4}", splitStr) is not None \
                                or re.search("\d-(\d{3})-\d{3}-\d{4}", splitStr) is not None \
                                or re.search("(\d{3})/\d{3}/\d{4}", splitStr) is not None \
                                or re.search("\d/(\d{3})/\d{3}/\d{4}", splitStr) is not None \
                                or re.search("(\d{3}).\d{3}.\d{4}", splitStr) is not None \
                                or re.search("\d.(\d{3}).\d{3}.\d{4}", splitStr) is not None:
                                    splitStr = re.sub("[^0-9]", "", splitStr)
                                    if len(splitStr) == 10 or len(splitStr) == 11:
                                        phoneWriter.writerow([splitStr])
##                                else:
##                                    otherTextWriter.writerow([splitStr])
                        linkXPath = linkContent.xpath('//*[@class="postingBody"]/a')
                        for linkXElement in linkXPath:
                            textA = tostring(linkXElement)
                            if 'mailto:' in textA:
                                start = textA.find('"mailto:')
                                end = textA.find('">')
                                if start != -1 and end != -1:
                                    textA = textA[start+8:end]
                                    emailWriter.writerow([textA])
                    endTime = time.time()
                    totTime = endTime - startTime
                    totTime = ("{0:.1f}".format(round(totTime,2)))
                    print "It took " + str(totTime) + " seconds to complete "
                    print str(count) + " links on Page " + str(increment) 
##	End of Main Links
##	Start of Sponsors Links
                    startTime = time.time()
                    sponsorXPath = mainContent.xpath('//*[@class="sponsorBoxContent"]/a')
                    sponsorCount = 0
                    for sponsorXElement in sponsorXPath:
                        sponsorCount = sponsorCount + 1
                        link = tostring(sponsorXElement)
                        link = link[9:]
                        link = link.split()
                        link = link[0]
                        link = link.split('">')
                        link = link[0]
                        link = "http://toronto.backpage.com" + link
                        linkRequest = requests.get(link)
                        linkContent = html.fromstring(linkRequest.content)
                        linkXPath = linkContent.xpath('//*[@class="postingBody"]')
                        for linkXElement in linkXPath:
                            text = tostring(linkXElement)
                            splitStrArr = text.split(' ')
                            for splitStr in splitStrArr:
                                start = splitStr.find('&')
                                end = splitStr.find(';')
                                if start != -1 and end != -1:
                                    splitStr = splitStr[start+1:end]
                                if re.search("\d{3}-\d{3}-\d{4}", splitStr) is not None \
                                or re.search("\d-\d{3}-\d{3}-\d{4}", splitStr) is not None \
                                or re.search("\d{3}/\d{3}/\d{4}", splitStr) is not None \
                                or re.search("\d/\d{3}/\d{3}/\d{4}", splitStr) is not None \
                                or re.search("\d{3}.\d{3}.\d{4}", splitStr) is not None \
                                or re.search("\d.\d{3}.\d{3}.\d{4}", splitStr) is not None \
                                or re.search("(\d{3})-\d{3}-\d{4}", splitStr) is not None \
                                or re.search("\d-(\d{3})-\d{3}-\d{4}", splitStr) is not None \
                                or re.search("(\d{3})/\d{3}/\d{4}", splitStr) is not None \
                                or re.search("\d/(\d{3})/\d{3}/\d{4}", splitStr) is not None \
                                or re.search("(\d{3}).\d{3}.\d{4}", splitStr) is not None \
                                or re.search("\d.(\d{3}).\d{3}.\d{4}", splitStr) is not None:
                                    splitStr = re.sub("[^0-9]", "", splitStr)
                                    if len(splitStr) == 10 or len(splitStr) == 11:
                                        phoneWriter.writerow([splitStr])
##                                else:
##                                    otherTextWriter.writerow([splitStr])
                        linkXPath = linkContent.xpath('//*[@class="postingBody"]/a')
                        for linkXElement in linkXPath:
                            textA = tostring(linkXElement)
                            if 'mailto:' in textA:
                                start = textA.find('"mailto:')
                                end = textA.find('">')
                                if start != -1 and end != -1:
                                    textA = textA[start+8:end]
                                    emailWriter.writerow([textA])
                    endTime = time.time()
                    totTime = endTime - startTime
                    totTime = ("{0:.1f}".format(round(totTime,2)))
                    print "It took " + str(totTime) + " seconds to complete "
                    print str(sponsorCount) + " sponsor links on Page " + str(increment)
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
