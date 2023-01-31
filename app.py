from flask import Flask, request
from os import environ 
import os
from email.message import EmailMessage
import ssl
import smtplib
import random

app = Flask(__name__)

@app.route('/completed', methods=['POST'])
def complete():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    branch = request.form.get('branch')
    datetime = request.form.get('datetime')
    
    date, time = datetime.split()
    date = date.split('-')
    date = f"{date[2]}-{date[1]}-{date[0]}"
    time = time.split(':')[:2]
    time = f"{time[0]}:{time[1]}"
        
    sender = 'ychqdcexqcqt26@gmail.com'
    emailPass = environ.get('EMAIL_PASS')
    receiver = email
        
    subject = 'RHB Online Appointment'
    body = """
    Hello %s,
    Thank you for using our RHB Online Appointment service.
        
    Here are the details of your appointment details:
        
    Queue Number : %d
        
    Name : %s
    Phone Number : %s
    Preferred branch : %s
    Date : %s
    Time : %s
        
    we advise you to be in the branch 10 minutes early before your schedule time.
    Thank you for choosing RHB Bank.
        
        
        
        
        
        
        
        
    This is an automatic generated message, do not reply to this email.
        
    """ % (name, random.randint(111,999) , name, phone,branch,date,time )
        
    em = EmailMessage()
    em['from'] = sender
    em['to'] = receiver
    em['subject'] = subject
    em.set_content(body)
        
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(sender,emailPass)
        smtp.sendmail(sender,receiver,em.as_string())    
        
        

    print(name)
    print(email)
    print(phone)
    print(branch)
    print(datetime)
    #dah dpt masuk data dkt api flask , tinggl nak send email je.
    return '', 200

if __name__ == '__main__':
    app.run()
