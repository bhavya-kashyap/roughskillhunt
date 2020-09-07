import pymysql

def checkuser(phone):
   db = pymysql.connect("localhost","root","Mproject@2020","skillhunt" )
   cur = db.cursor()
   sql = 'select phone from can'
   lt = cur.execute(sql)
   db.commit()
   db.close()
   if lt==0:
      return 0
   else:
      return 1
