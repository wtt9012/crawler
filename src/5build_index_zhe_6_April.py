from bs4 import BeautifulSoup
import urllib2
import re
import sqlite3

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
            words.append(link.get_text().encode('ascii'))
            flag = 0
        if flag == 1: 
            words.append(link.get_text().encode('ascii'))
    return words

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

def createDictionary(words):
    dictionary = {}
    
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    sql = 'select * from data '
    for row in c.execute(sql):
        docID = row[0]
        content = row[1]
        company = row[2]
        review_date = row[3]
        
        value1 = (docID, review_date, -1, 0)
        value_list1 = []

        if dictionary.get(company, 'not found') != 'not found':
            value_list1 = dictionary.get(company)
            value_list1.append(value1)
        else:
            value_list1.append(value1)
        dictionary[company] = value_list1    


        for word in words:
            if content and any (word.lower() == c for c in content):
                docID = row[0]
                company = row[2]
                review_date = row[3]
                position = getPosition(content, word.lower())
                occurences = getOccurences(content, word.lower())
                
                value2 = (docID, review_date, position, occurences)
                value_list2 = []

                if dictionary.get(word, 'not found') != 'not found':
                    value_list2 = dictionary.get(word)
                    value_list2.append(value2)
                else:
                    value_list2.append(value2)
                dictionary[word] = value_list2
    
    return dictionary

def saveDictionary(dictionary):
   conn = sqlite3.connect('mydatabase.db')
   c = conn.cursor()
   
   for key, value in dictionary.items():
       for element in value:
           sql = 'insert into search values(?, ?, ?, ?, ?)'
           c.execute(sql, (key, element[0], element[1], element[2], element[3]))
           conn.commit()
   print 'save successfully'

def main():
    print 'getting query words......'
    words = getQueryWords()
    print 'building dictionary......'
    dictionary = createDictionary(words)
    #print dictionary.get('Guidewire')
    print 'saving dictionary......'
    saveDictionary(dictionary)

main()
    

    
