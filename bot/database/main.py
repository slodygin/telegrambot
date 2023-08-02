# todo: Database engine
import sqlite3
#from bot.database import *
connection = None
cursor = None
def  get_connection():
  global connection
  global cursor
  if not connection:
     connection = sqlite3.connect('sqlite3.db')
  if not cursor:
     cursor = connection.cursor()
     cursor.execute("""CREATE TABLE IF NOT EXISTS users(id VARCHAR(255),cur_status INTEGER);""")
     connection.commit()
     cursor.execute("""CREATE TABLE IF NOT EXISTS schedule(description VARCHAR(255));""")
     connection.commit()
  print("DEBUG: connection1=",connection)
  print("DEBUG: cursor1=",cursor)
  return connection,cursor
