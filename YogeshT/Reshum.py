import os
import smtplib
import imghdr
from email.message import EmailMessage
import pandas as p

 # Reading and storing data
data = p.read_csv("students.csv")
print(type(data))
section1 = data.get("NAME")
print(section1)


# Converting data into lists:

list_of_HR = list(data.get("Talent acquision HR"))
list_of_names = list(data.get("NAME"))
list_of_contact = list(data.get("CONTACT NO"))
list_of_emails = list(data.get("EMAIL ID"))
list_of_date = list(data.get("DATE"))
list_of_time = list(data.get("TIME"))
list_of_levels = list(data.get("L1/L2"))
list_of_panels = list(data.get("PANEL"))


# Combining list_of_date and list_of_time

list_of_date_and_time = []

for i in range(len(list_of_date)):
  list_of_date_and_time.append(str(list_of_date[i]) + " at " + str(list_of_time[i]))

print(list_of_date_and_time)
















'''
EMAIL_ADDRESS = "hirefreelancersnow@gmail.com"
EMAIL_PASSWORD = "yogeshtekwani"
msg = EmailMessage()
msg['Subject'] = 'Interview Details'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'YourAddress@gmail.com'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    subject = "Email Testing Successfull....!!!!"
    body = "If you have recieved this email, it means Yogesh Tekwani has successfully learnt about spamming emails ! ; ) \n\n"
    msg = f'Subject:{subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, "hirefreelancersnow@gmail.com", msg)


'''