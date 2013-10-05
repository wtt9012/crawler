import sqlite3

def selectDB(cursor):
    filename = "0000"
    file = open(filename, "w")
    for i in range(1,5000):
    	sql = "select content from data where docID = ?"
    	cursor.execute(sql, [str(i)])
    	question = str(cursor.fetchall())
	question = str(question).replace("'","") 
   	question = str(question).replace("[","") 
    	question = str(question).replace("]","") 
    	question = str(question).replace("(","") 
    	question = str(question).replace(")","")
    	question = str(question).replace(",","")
    	question = str(question).replace("\""," ")
	file.write(question)
        print i
  
def main():
    
    conn = sqlite3.connect("0test.db")
    cursor = conn.cursor()
  
    selectDB(cursor)

    conn.commit()
main()
