from flask import Flask
from flask import Flask, url_for, request, redirect, jsonify, render_template, session
import pymysql
import otp, jobs, checkuser, candidates, sendmail


app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
   return render_template("index.html")

@app.route('/check', methods = ['POST','GET'])
def check():
   if request.method == 'POST':
      return render_template("newpost.html")
"""
      if 'phone' in session:
         phone = session['phone']
         return redirect("http://192.168.43.20/newpost.html", code=302)
      else:
         return redirect("http://192.168.43.20/login.html", code=302)
"""
@app.route('/sendmail', methods = ['POST', 'GET'])
def sendmail():
   if request.method == 'POST':
      email = request.form['mail']
      message = request.form['message']
      password = request.form['password']
      sendmail.send(email, password, message)
   return redirect(url_for("index"))
         
@app.route('/check1', methods = ['POST','GET'])
def check1():
   if request.method == 'POST':
      if 'phone' in session:
         phone = session['phone']
         return render_template("jobpost.html")
      else:
         return render_template("login.html")

@app.route('/newpost', methods = ['POST', 'GET'])
def newpost():
   if request.method == 'POST':
      title = request.form['title']
      location = request.form['address']
      contact = request.form['contact']
      cate = request.form['category']
      mail = request.form['email']
      employer = request.form['employer']
      description = request.form['jdesc']
      j = jobs.Jobs()
      j.create_j(title, description, cate, mail, employer, location, contact)
      if j:
         print('job created', j.jid)
         lt = jobs.getjobs()
         print("lt received requesting render template")
   return redirect("http://192.168.43.20/bro.html", code=302) 
   

@app.route('/phoneno', methods = ['POST', 'GET'])
def phoneno():
   if request.method == 'POST':
      cont = request.form['contact']
      print(cont)
      a = checkuser.checkuser(cont)
      if a:
         otp.generate_otp(cont)
         return render_template("otpverify.html")
      else:
         return render_template("signup.html")
      
@app.route('/otpverify', methods = ['POST', 'GET'])
def otpverify():
   if request.method == 'POST':
      votp = request.form['otp']
      a = otp.verify_otp(votp)
      print( a, type(a))
      if a:
          #session['name'] = name_of_i
          return redirect(url_for('newpost'))
      else:
          return redirect(url_for('phoneno'))

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
   if request.method == 'POST':
      name = request.form['name']
      city = request.form['address']
      contact = int(request.form['contact'])
      category = request.form['category']
      education = request.form['education']
      description = request.form['desc']
      c = candidates.Candidates(contact)
      c.create_c(name, contact, city, description, category, education)
      if c:
         print('candidate created', c.name, c.contact)
      session["phone"] = contact
   return render_template("browsejobs.html") 

if __name__ == '__main__':
   app.run('192.168.43.20', 5000, True)
