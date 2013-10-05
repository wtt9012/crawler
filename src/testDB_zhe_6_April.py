import sqlite3

def selectDB(cursor):
    sql = "select * from search where wordID = ?"
    cursor.execute(sql, ['Guidewire'])
    print cursor.fetchall()
  
def main():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
  
    selectDB(cursor)

    conn.commit()
main()
