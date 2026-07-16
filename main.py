import os
from dotenv import load_dotenv
import smtplib
import datetime

today = datetime.date.today()
today = (today.month, today.day)

mom = (12, 25)
dad = (9, 28)
me = (5, 25)
bro = (1, 19)

info = {
    'mom': (mom, "rohinipgurav@gmail.com"),
    'dad': (dad, "pareshgurav@gmail.com"),
    'me': (me, "sgpython452@gmail.com"),
    'bro': (bro, "spg192020@gmail.com"),
}

for name in info:
    if info[name][0] == today:
        h = True
        name = name
        PERSON_EMAIL = info[name][1]
        break
else:
    h = False

if h:

    load_dotenv()

    EMAIL = os.environ.get("EMAIL")  # Do not use child restricte account.
    PASSWORD = os.environ.get("PASSWORD")

    if not EMAIL or not PASSWORD:
        raise ValueError("EMAIL or PASSWORD not found in .env")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)

        subject = "Happy Birthday {}".format(name)
        body = "Happy Birthday {}, hope you have fun today.".format(name)

        message = f"Subject:{subject}\n\n{body}\nThis is sent from python.\n\nFrom\nSiddhaanth Gurav"
        connection.sendmail(from_addr=EMAIL, to_addrs=PERSON_EMAIL, msg=message)
    print("Today is {}'s birthday and msg is sent. \n{}".format(name, body))
else:
    print("Today is no one's birthday...")
