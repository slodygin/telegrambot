from bot.database import get_connection
def fetchall( sql, values=None):
  conn,cur = get_connection()
  cur=conn.cursor()
  print("DEBUG connection=",conn)
  print("DEBUG values=",values)
  if values == None:
    cur.execute(sql)
  else:
    cur.execute(sql, values)
  #conn.close()
  return cur.fetchone()
def insert( sql, values=None):
  conn,cur = get_connection()
  cur=conn.cursor()
  print("DEBUG connection=",conn)
  print("DEBUG values=",values)
  if values == None:
    cur.execute(sql)
  else:
    cur.execute(sql, values)
  conn.commit()
  #conn.close()
  print("DEBUG ",cur.rowcount, "record inserted")
  return cur.rowcount
def update( sql, values=None):
  conn,cur = get_connection()
  cur=conn.cursor()
  print("DEBUG connection=",conn)
  print("DEBUG values=",values)
  if values == None:
    cur.execute(sql)
  else:
    cur.execute(sql, values)
  conn.commit()
  #conn.close()
  print("DEBUG ",cur.rowcount, "record updated")
  return cur.rowcount
