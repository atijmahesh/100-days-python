import smtplib
import datetime as dt
import random

my_email = "unsecureemail679@gmail.com"
password = "qsal lhlp rfpg xhcy"
connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 2:
    lines = []
    with open("quotes.txt") as quotes_file:
        lines = quotes_file.readlines()
    line = random.choice(lines)
    connection.sendmail(
    from_addr=my_email, 
    to_addrs=my_email,
    msg=f"Subject: Motivation!\n\n{line}."
    )   
