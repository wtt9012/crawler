from bs4 import BeautifulSoup
import urllib2
import re
import errno
import json

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

def getSubContent(text, start, end):
    size = len(text)
    content = []
    flag = 0
    i = 0
    while(i != size):
        if flag and text[i] == end:
            return content
        if flag == 1:
            content.append(text[i])
        if text[i] == start:
            flag = 1
        i += 1

def getPosition(text, word):
    size = len(text)
    i = 0
    while(i != size):
        if text[i] == word:
            return i
        i += 1
    return -1

def getOccurences(text, word):
    size = len(text)
    i = 0
    count = 0
    while(i != size):
        if text[i] == word:
            count += 1
        i += 1
    return count

def getCompanyName(soup):
    company_name = soup.find_all(class_ = "i-emp")[0].get_text()
    return company_name.encode('ascii')

def getReviewDate(soup):
    review_date = soup.find_all(class_ = "SL_date")[0].get_text()
    return review_date.encode('ascii')

def createDictionary(words):
    dictionary = {}
    i = 1
    while (i < 291):
        try:
            file = open('/Users/jackking/Desktop/project/' + str(i))
        except IOError as e:
            if e.errno == errno.ENOENT:
                i += 1
                file = open('/Users/jackking/Desktop/project/' + str(i))
            else:
                raise e

            
        soup = BeautifulSoup(file)
    
        questions = str(soup.find_all(class_ = "questions"))
        splitter = re.compile('\\W*')
        interview_question = [s.lower() for s in splitter.split(questions) if s!= '']
        content = getSubContent(interview_question, 'notranslate', 'tt')
        
        for word in words:
            if content and any (word.lower() == c for c in content):
                company_name = getCompanyName(soup)
                review_date = getReviewDate(soup)
                position = getPosition(content, word.lower())
                occurences = getOccurences(content, word.lower())
                value = (i, company_name, review_date, position, occurences)
                value_list = []

                if dictionary.get(word, 'not found') != 'not found':
                    value_list = dictionary.get(word)
                    value_list.append(value)
                else:
                    value_list.append(value)
                    dictionary[word] = value_list
        
        i += 1

    output = open('Index.log', 'w')
    #for key, value in dictionary.items():
    try:
        output.write(str(dictionary))
    except Exception as er:
        print er
    finally:
        output.close()
    return dictionary

def main():
    print "Getting query words......"
    words = getQueryWords()
    print "Buiding index......"
    dictionary = createDictionary(words)
    print "Successful saved index into Index.log"
    print "Key: query word,  Value: (docID, company name, review date, position, occurrences)"
    print "Index Testing:"
    print "Search by keyword 'java':"
    print dictionary.get('Java')

main()

