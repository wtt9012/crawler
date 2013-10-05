from bs4 import BeautifulSoup
import urllib2
import re
    
def getQueryWords():
    url = "http://www.careercup.com/categories"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
   
    #initialize list to store query words
    words = []
    flag = 0
    for link in soup.find_all('a'):
        if 'Algorithm' in link:
            flag = 1
        if 'XML' in link:
            words.append(link.get_text())
            flag = 0
        if flag == 1: 
            words.append(link.get_text())
    return words


def createDictionary(words):
    dictionary = {}
    file = open('/afs/umich.edu/user/j/a/jackking/Desktop/549/1')
    
    #get company name
    soup = BeautifulSoup(file)
    company_name = soup.find_all(class_ = "i-emp")[0].get_text()
    print company_name  

    #get review date
    review_date = soup.find_all(class_ = "SL_date")[0].get_text()
    print review_date 

    #get word's occurences and position inside "interview questions"
    questions = str(soup.find_all(class_ = "questions"))
    splitter = re.compile('\\W*')
    interview_question = [s.lower() for s in splitter.split(questions) if s!= '']
    print interview_question



def main():
    words = getQueryWords()
    createDictionary(words)

main()

