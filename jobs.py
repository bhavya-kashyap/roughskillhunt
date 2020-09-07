import time, pymysql


class Jobs:
   def __init__(self):
      self.jid = int(time.time())
      self.status = 'Hiring'
      return 
     
   def create_j(self, title, description, category, email, employer, location, contact):
      db = pymysql.connect("localhost","root","Mproject@2020","skillhunt" )
      cur = db.cursor()
      self.jid = str(self.jid)
      contact = int(contact)
      cur.execute('INSERT into jobs(jid, status, title, description, category, email, employer, location, contact) values("%s", "%s", "%s", "%s", "%s", "%s","%s", "%s","%d")'%(self.jid, self.status, title, description, category, email, employer, location, contact))
      db.commit()
      db.close()
      return True 

def getjobs():
   db = pymysql.connect("localhost","root","Mproject@2020","skillhunt" )
   cur = db.cursor()
   sql =  "select category, title, email, employer, contact, location from jobs"
   cur.execute(sql)
   lt = list(cur.fetchall())
   a = []
   for i in lt:
      a.append(list(i))
   return a
