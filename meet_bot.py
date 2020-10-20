
# google meet bot


######################################################

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import playsound
import os
from gtts import gTTS


####################################################



class Meetbot:

    def __init__(self,username,password,meetlink):

        self.username = username
        self.password = password
        self.meetlink = meetlink
        self.number_of_stud = 60
        self.left_limit = 30

        self.driver = webdriver.Firefox()

        self.login_gmail()

        
        # login into the gmail account 
        
    def login_gmail(self):

        # getting into the google login page

        time.sleep(2)
        
        self.driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        time.sleep(2)        
        # passing the email id
        
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(self.username)
        time.sleep(2)
            
        next_button1 = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
        next_button1.click()
        time.sleep(2)

        # passing the password
        
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(self.password)       
        time.sleep(2)
            
        next_button2 = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
        next_button2.click()
        time.sleep(4)

        self.joining_meet()

    # function for joining into the meet
    
    def joining_meet(self):

        # redirecting to the google meet join page

        self.driver.get(self.meetlink)
        time.sleep(6)

        # turning off the mic

        mic_off = self.driver.find_element_by_xpath(
                "/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[3]/div[1]/div/div/div")
        mic_off.click()
        time.sleep(2)

        # turning off the camera
        
        cam_off = self.driver.find_element_by_xpath(
                "/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div/div")
        cam_off.click()
        time.sleep(2)

        # joining the class

        join_button = self.driver.find_element_by_xpath(
                "/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div")
        join_button.click()

        # waiting for some time before the initialisation of infinite while loop
        
        time.sleep(20)

        self.bore_class()

    def bore_class(self):

        # infinite while loop working until the number of students in the class is less than 30

        while True:

                try:

                    time.sleep(4)
                    people_number = self.driver.find_element_by_xpath("//*[contains(@class,'wnPUne N0PJ8e')]").text
                    people_number = int(people_number)                    
        
                except:
                    pass

                if people_number <=30:
                    break
        
                else:
                    pass

                print(people_number)


        time.sleep(1)

        self.driver.close()


##################################################################################

# main


if __name__ == "__main__":

    def voice(txt):
        speech=gTTS(text=txt,lang='en',slow=False)
        speech.save("a.mp3")
        playsound.playsound("a.mp3")
        os.remove("a.mp3")
                
    voice("Enter Your Mail")
    username = input("Enter Your E-mail : ")
    voice("Enter the password")
    password = input("Enter the password: ")
    voice("Enter the class link")
    meetlink = input("Enter the google meet class link: ")

    meet_bot = Meetbot(username, password, meetlink)

    voice("This session is over")
    print("This session is Over")
    

    
            

            

#################################################################################
