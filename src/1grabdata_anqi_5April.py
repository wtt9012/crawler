from bs4 import BeautifulSoup
import urllib2
ques = 0
for num in range(10,11):

    name = '"disabled"'
    #each page with 10 companies
    url = "http://www.glassdoor.com/Reviews/computer-software-company-reviews-SRCH_II1121.0,17_IP" + str(num) + ".htm"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)

    
    for link1 in soup.find_all('a'):
	
    	page = 1 #each page with 10 ques
    	
        h1 = link1.get("href")
        if h1 and h1.encode("ascii", "ignore").startswith("/Interview"):
            if h1.encode("ascii", "ignore").startswith("/Interview/index"):
                continue

            while True:

                length = len(h1)
                #each page with 10 questions
                #print h1
                url1 = "http://www.glassdoor.com" + h1[0:length - 4] + "_P" + str(page) + ".htm"
		print url1
                content1 = urllib2.urlopen(url1).read()
                soup1 = BeautifulSoup(content1)
                    
                for link2 in soup1.find_all('a'):
                    h2 = link2.get("href")
                    if h2 and "-Interview-RVW" in h2.encode("ascii", "ignore"):
                        #each question page
                        url2 = "http://www.glassdoor.com" + h2
                        print url2
                        content2 = urllib2.urlopen(url2).read()
                        ques += 1
                        filename = str(ques)
                        file = open(filename, "w+")
                        file.write(content2)
                        file.close()

                #if it's the last page of questions, break

                if(name in str(soup1.find_all(class_='nextBtn')[0])):
                    break

                page += 1


