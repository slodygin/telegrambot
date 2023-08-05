# todo: Database engine
import sqlite3

connection = None
cursor = None


def get_connection():
    global connection
    global cursor
    if not connection:
        connection = sqlite3.connect("sqlite3.db")
    if not cursor:
        cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id VARCHAR(255), cur_status INTEGER);")
    connection.commit()
    cursor.execute("CREATE TABLE IF NOT EXISTS schedule (description VARCHAR(255));")
    connection.commit()
    print("DEBUG: connection1=", connection)
    print("DEBUG: cursor1=", cursor)
    return connection, cursor


def fetchone(sql, values=None):
    conn, cur = get_connection()
    cur = conn.cursor()
    print("DEBUG connection=",conn)
    print("DEBUG values=",values)
    if values == None:
        cur.execute(sql)
    else:
        cur.execute(sql, values)
    #conn.close()
    return cur.fetchone()


def fetchall(sql, values=None):
    conn, cur = get_connection()
    cur = conn.cursor()
    print("DEBUG connection=",conn)
    print("DEBUG values=",values)
    if values == None:
        cur.execute(sql)
    else:
        cur.execute(sql, values)
    #conn.close()
    return cur.fetchall()


def execute(sql, values=None):
    conn, cur = get_connection()
    cur = conn.cursor()
    print("DEBUG connection=",conn)
    print("DEBUG values=",values)
    if values == None:
        cur.execute(sql)
    else:
        cur.execute(sql, values)
    conn.commit()
    #conn.close()
    print("DEBUG ",cur.rowcount, "records affected")
    return cur.rowcount
