from bs4 import BeautifulSoup
import urllib2
import sqlite3
import re
import errno

def getContent(text, start, end):
    size = len(text)
    content = []
    flag = 0
    i = 0
    while(i != size):
        if flag and text[i] == end:
            return str(content)
        if flag == 1:
            content.append(text[i])
        if text[i] == start:
            flag = 1
        i += 1

def processFile():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    i = 1
    while(i < 291):
        try:
            file = open('/afs/umich.edu/user/j/a/jackking/Desktop/549/' + str(i))
        except IOError as e:
            if e.errno == errno.ENOENT:
                i += 1
                file = open('/afs/umich.edu/user/j/a/jackking/Desktop/549/' + str(i))
            else:
                raise e
        
        soup = BeautifulSoup(file)

        #get content
        questions = str(soup.find_all(class_ = "questions"))
        splitter = re.compile('\\W*')
        interview_question = [s.lower() for s in splitter.split(questions) if s!= '']
        content = getContent(interview_question, 'notranslate', 'tt')

        #get document id
        docID = str(i)

        #get company name
        company_name = soup.find_all(class_ = "i-emp")[0].get_text().encode('ascii')

        #get review date
        review_date = soup.find_all(class_= "SL_date")[0].get_text().encode('ascii')
        
        #insert data into db
        sql = "insert into data VALUES(?, ?, ?, ?)"
        cursor.execute(sql, (docID, content, company_name, review_date))
        conn.commit()

        i += 1


def main():
    processFile()

main()
