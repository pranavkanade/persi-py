import smtplib

sender = 'sakshi_jamgaonkar@persistent.co.in'
receivers = ['sakshi_jamgaonkar@persistent.co.in']

message = """From: From Person <from@fromdomain.com>
To: Sakshi <sakshi_jamgaonkar@persistent.co.in>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
#except SMTPException:
except Exception as error:
   print "Error: unable to send email", error
