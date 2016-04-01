import sys
import re
import urllib2
import PyRSS2Gen

response = urllib2.urlopen('http://www.monmouth.edu/school-of-science/news-and-events.aspx')
html = response.read()

myheadlines = re.findall('<p><strong>(.+)</strong>(?:.+)?</p>',html)
mynames = re.findall('<a name="(.+)" class="anchorMargin"',html)

myrawdata = re.split('<hr />', html)
myrawdata.pop(0)
myrawdata.pop()

mydescriptions = []
for value in myrawdata:
    #value = value.strip()
    final = re.sub('<p .+>.+</p>|<strong>.+</strong>|<div .*?>.+|<.*?>|\d{1,2}/\d{1,2}/\d{1,2}|Read more.+','',value)
    mydescriptions.append(final.strip())

print myheadlines
print len(myheadlines)
print mynames
print len(mynames)
print mydescriptions
print len(mydescriptions)
baselink = "http://www.monmouth.edu/school-of-science/news-and-events.aspx#"

rss = PyRSS2Gen.RSS2(
    title = "Monmouth's CSSE news feed",
    link = "http://www.monmouth.edu/school-of-science/news-and-events.aspx",
    description = "The latest news about CSSE Department at Monmouth",

    items = [])



for x in range(len(myheadlines)):
    rss.items.append(
    PyRSS2Gen.RSSItem(
    title = myheadlines[x],
    link = baselink + mynames[x],
    description = mydescriptions[x]
    ))

rss.write_xml(open("pyrss2gen.xml", "w"))
