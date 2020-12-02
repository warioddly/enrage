import smtplib
import re
from subprocess import call

def send_spam(email, password, target_email, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(email, password)
    except smtplib.SMTPAuthenticationError:
        print("[!] allow access for https://www.google.com/settings/security/lesssecureapps")
    server.sendmail(email, target_email, message)
    
def check_login(email):
    check = re.search("@gmail.com", email)
    if check == "@gmail.com":
        return email
    else:
        email = email + "@gmail.com"
        return email

call(["clear"])
print("--ENRAGE--\n")
email = input("[+] inter your email > ")
email = check_login(email)
password = input("[+] inter your email password > ")
target_email = input("[+] inter target email > ")
target_email = check_login(target_email)
message = input("[+] input message > ")
try:
    amount = int(input("[+] amount of message (default 10) > "))
except ValueError:
    amount = 10

sent_messages = 1
try:
    print("\n")
    for i in range(amount):
        send_spam(email, password, target_email, message)
        print("\r[+] " + str(sent_messages) + " messages sent", end="")
        sent_messages += 1
except KeyboardInterrupt:
    print("\n[-] You Stopped Spam")    
print("\n[+] Thanks for using ENRAGE\n")
