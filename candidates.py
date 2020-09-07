import time, pymongo, pymysql



class Profile:
   def __init__(self):
      return
   
   def profid(self):
      return int(time.time())

   def create_pdf(self):
      pass

class Candidates:
   def __init__(self,phone):
      p = Profile()
      self.prof = str(int(p.profid()/1000))
      self.exp = []
      self.rating = 0
      return

   def set_exp(self):
      client = pymongo.MongoClient("mongodb://localhost:27017/")
      db = client["skillhunt"]
      col = db["experience"]
      db.col.insertOne({ "phone" : "{}".format(self.phone), "exp" : [] })
      client.close()
      return True

   def create_c(self, name, contact, city, description, category, education):
      self.name=name
      self.contact = int(contact)
      self.city=city
      self.description=description
      self.education=education
      self.rating = int(self.rating)
      print(self.name, contact, self.prof, city, description, self.rating, category)

      con = pymysql.connect("localhost","root","Mproject@2020","skillhunt" )
      cur = con.cursor()
      
      cur.execute('INSERT into can(name, phone, prof, location, description, rating, category) values("%s", "%d", "%s", "%s", "%s", "%d","%s")'%(name, contact, self.prof, city, description, self.rating, category))

      con.commit()
      con.close()
      return True

   def rate(self, rate):
      self.rating = int((self.rating+rate)/2)
      return self.rating

   def get_c(self):
      return self.name, self.phone, self.prof, self.city, self.description, self.category, self.education, self.experience, self.rating

def add_exp(phone, experi):
   client = pymongo.MongoClient("mongodb://localhost:27017/")
   db = client["skillhunt"]
   col = db["experience"]
   
   col.update({"phone": phone}, {"$push": {"exp": '{}'.format(experi)}})
   
   client.close()
   return True
