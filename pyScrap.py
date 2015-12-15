from lxml import html
from lxml.etree import tostring
import requests
import csv
with open('PhoneNumbers.csv','w') as f1:
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
    subcat = [""]
    r = requests.get("http://toronto.backpage.com/adult")
    c = html.fromstring(r.content)
    x = c.xpath('//*[@class="sponsorBoxContent"]/a')
    for e in x:
        strE = tostring(e)
        strE = strE[9:]
        strE = strE.split()
        strE = strE[0]
        strE = strE.split('">')
        strE = strE[0]
        strE = "http://toronto.backpage.com" + strE
        r2 = requests.get(strE)
        c2 = html.fromstring(r2.content)
        x2 = c2.xpath('//*[@class="postingBody"]')
        x3 = c2.xpath('//*[@id="postingTitle"]')
        for e2 in x2:
            strE2 = tostring(e2)
            writer.writerow(strE2)
        for e3 in x3:
            strE3 = tostring(e3)
            writer.writerow(strE3)
