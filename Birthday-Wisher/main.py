##################### Normal Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas

letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day):data_row.to_list() for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    letter_file = "letter_templates/" + random.choice(letter_list)
    with open(letter_file, "r") as f:
        data = f.read()
        data = data.replace("[NAME]", birthdays_dict[(today)][0])
    print(data)

    my_email = "unsecureemail679@gmail.com"
    password = "qsal lhlp rfpg xhcy"
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)  
    connection.sendmail(
    from_addr=my_email, 
    to_addrs=birthdays_dict[(today)][1],
    msg=f"Subject: Happy Birthday!\n\n{data}."
    )