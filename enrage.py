import smtplib
import re
from subprocess import call
import threading

class ENRAGE:
    def __init__(self):
        call("cls", shell=True)
        print("--ENRAGE--\n")
        self.launch()
    
    def data_retrieval(self):
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
        

    def thread(self):
        timer = threading.Timer(1, self.thread)
        timer.start()

    def send_spam(self, email, password, target_email, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        try:
            server.login(email, password)
        except smtplib.SMTPAuthenticationError:
            print("[!] allow access for https://www.google.com/settings/security/lesssecureapps")
        server.sendmail(email, target_email, message)
        
    def check_login(self, email):
        check = re.search("@gmail.com", self.email)  
        if str(check) in "None":
            email += "@gmail.com"
            return email
        else:
            return email
    
    def launch(self):
        self.data_retrieval()


ENRAGE()