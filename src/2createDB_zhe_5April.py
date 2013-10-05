import sqlite3

def createDB():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "create table data (docID, content, company_name, review_date)"
    cursor.execute(sql)
    conn.commit()

def main():
    createDB()

main()
