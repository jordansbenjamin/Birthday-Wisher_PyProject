##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random as rd
import smtplib

# 1. Update the birthdays.csv
# READ CSV
bday_df = pd.read_csv("birthdays.csv")
bday_data = bday_df.to_dict(orient='records')

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
date_today = now.date()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for bday in bday_data:
    if bday['month'] == month and bday['day'] == day:
        random_letter = f"./letter_templates/letter_{rd.randint(1,3)}.txt"
        bday_person = bday

with open(random_letter, 'r') as letter_file:
    letter = letter_file.read()
    new_letter = letter.replace("[NAME]", bday_person['name'])
            
# 4. Send the letter generated in step 3 to that person's email address.
my_email = "jordansyariefjs@gmail.com"
password = "vtoaypkicpoumgyf"

def smtp_sendmail():
    subject = f"Happy Birthday {bday_person['name']}"
    content = new_letter
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs=my_email, 
                                msg=f"Subject:{subject}\n\n{content}")
    except:
        print("connection error.")
    else:
        print("E-Mail sent successfully.")

smtp_sendmail()