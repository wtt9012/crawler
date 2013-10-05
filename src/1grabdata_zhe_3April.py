from bs4 import BeautifulSoup
import urllib2

for num in range(10,11):
    url = "http://www.glassdoor.com/Reviews/computer-software-company-reviews-SRCH_II1121.0,17_IP" + str(num) + ".htm"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    
    #file name(one file per question)
    i = 0
    name = '"disabled"'
    for link in soup.find_all('a'):
        h = link.get("href")
        if h and h.encode("ascii", "ignore").startswith("/Interview"):
            if h.encode("ascii", "ignore").startswith("/Interview/index"):
                continue
                
            #come into each company with interview
            num1 = 1
            i += 1
            length = len(h)
            url1 = "http://www.glassdoor.com" + h[0:length - 4] + "_P" + str(num1) + ".htm"
            print(url1)
            content1 = urllib2.urlopen(url1).read()
            soup1 = BeautifulSoup(content1)
            
	    #come into each question of the company
	    for link1 in soup1.find_all('a'):
	       	h1 = link1.get("href") 
		if h1 and "-Interview-RVW" in h1.encode("ascii", "ignore"):
		    print h1
		    url2 = "http://www.glassdoor.com" + h1   	
            	    content2 = urllib2.urlopen(url2).read()    
		    filename = str(i)
                    file = open(filename, "w")
                    file.write(content2)
		    file.close()
            	    i += 1

            #name in str(soup.find_all(class_='nextBtn')[0]) means we are at the last interview page of this company
            while(not name in str(soup1.find_all(class_='nextBtn')[0])):
                num1 += 1
                url1 = "http://www.glassdoor.com" + h[0:length - 4] + "_P" + str(num1) + ".htm"
                print(url1)
                content1 = urllib2.urlopen(url1).read()
                soup1 = BeautifulSoup(content1)
                
		for link1 in soup1.find_all('a'):
                    h1 = link1.get("href")
		    if h1 and "-Interview-RVW" in h1.encode("ascii", "ignore"):
			print h1
		        url2 = "http://www.glassdoor.com" + h1   	
            	        content2 = urllib2.urlopen(url2).read()    
		        filename = str(i)
                        file = open(filename, "w")
                        file.write(content2)
			file.close()
            	        i += 1		     
         
