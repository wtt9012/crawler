from bs4 import BeautifulSoup
import urllib2

for num in range(1,2):
    url = "http://www.glassdoor.com/Reviews/computer-software-company-reviews-SRCH_II1121.0,17_IP" + str(num) + ".htm"
    
    
#url = "http://www.glassdoor.com/Reviews/computer-software-company-reviews-SRCH_II1121.0,17_IP1.htm"
    content = urllib2.urlopen(url).read()
#    filename = str(0)
#    file = open(filename,"w")
#    file.write(content)
#    file.close()

    soup = BeautifulSoup(content)
    i = 0
    for link in soup.find_all('a'):
        h = link.get("href")
#        if(!h.encode("ascii", "ignore").find("index")):    #how to jump the first one
        if h and h.encode("ascii", "ignore").startswith("/Interview"):
            if h.encode("ascii", "ignore").startswith("/Interview/index"):
                continue
            for num1 in range(1,6):
                i +=1
#                print(h)
                length = len(h)
                url1 = "http://www.glassdoor.com" + h[0:length - 4] + "_P" + str(num1) + ".htm"
                print(url1)
                content1 = urllib2.urlopen(url1).read()
                filename = str(i)
                file = open(filename,"w")
                file.write(content1)
                file.close()



#http://www.glassdoor.com/Interview/Microsoft-Interview-Questions-E1651_P2.htm

