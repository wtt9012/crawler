import sqlite3

def createDB1(cursor):
    sql = "create table data (docID, content, company_name, review_date)"
    cursor.execute(sql)

def createDB2(cursor):
    sql = "create table search (wordID, docID, review_date, position, occurences)"
    cursor.execute(sql)

def main():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    createDB2(cursor)

    conn.commit()

main()
