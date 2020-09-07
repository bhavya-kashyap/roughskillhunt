import smtplib, ssl

port = 587
smtp_server="smtp.gmail.com"
receiver = "bkkashyapbhavya97@gmail.com"

def sendmail(mail, password, message):
   sender = mail
   message = message
   server = smtplib.SMTP(smtp_server, port)
   server.ehlo()
   server.starttls()
   server.ehlo()
   server.login(mail, password)
   print("logged in")
   server.sendmail(sender, receiver, message)
   print("email sent")
   return 1
