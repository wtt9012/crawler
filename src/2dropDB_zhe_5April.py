import sqlite3

def dropDB(cursor):
    sql = "drop table data"
    cursor.execute(sql)
  
def main():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
  
    dropDB(cursor)

    conn.commit()
main()
