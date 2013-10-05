import sqlite3

def selectDB(cursor):
    sql = "select * from data where docID = ?"
    cursor.execute(sql, ["1"])
    print cursor.fetchall()
  
def main():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
  
    selectDB(cursor)

    conn.commit()
main()
