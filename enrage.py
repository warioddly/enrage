import smtplib

def send_spam(email, password, target_email, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(email, password)
    except smtplib.SMTPAuthenticationError:
        print("[!] allow access for https://www.google.com/settings/security/lesssecureapps")
    except smtplib.SMTPSenderRefused:
        print("imo")
    server.sendmail(email, target_email, message)

email = input("[+] inter your email > ")
password = input("[+] inter your email password > ")
target_email = input("[+] inter target email > ")
message = input("[+] input message > ")
try:
    amount = int(input("[+] number of message (default 10) > "))
except ValueError:
    amount = 10

sent_messages = 1
for i in range(amount):
    send_spam(email, password, target_email, message)
    print("\r[+] " + str(sent_messages) + " messages sent", end="")
    sent_messages += 1
print("\n[+] Thanks for using OFF3\n")