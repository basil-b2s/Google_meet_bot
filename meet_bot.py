

# google meet bot


######################################################

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



####################################################



class Meetbot:

    def __init__(self,username,password,meetlink):

        self.username = username
        self.password = password
        self.meetlink = meetlink

        # notification settings (camera , mic)
        self.opt = Options()
        self.opt.add_argument("--disable-infobars")
        self.opt.add_argument("start-maximized")
        self.opt.add_argument("--disable-extensions")
        
        # Pass the argument 1 to allow and 2 to block
        
        self.opt.add_experimental_option("prefs", { \
                "profile.default_content_setting_values.media_stream_mic": 1, 
                "profile.default_content_setting_values.media_stream_camera": 1,
                "profile.default_content_setting_values.notifications": 2
              })

        self.driver = webdriver.Chrome(chrome_options=self.opt, executable_path='.\Chromedriver\chromedriver')

        self.login_gmail()

        
        # login into the gmail account through stackoverflow ( since google does't allow automated webrowser login directly )
        
    def login_gmail(self):

        # getting into the google login page through stackoverflow 

        self.driver.get("https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A1125b5ebe8db8eeb%2C10%3A1601450831%2C16%3A5584e909d121ad66%2C0845646c5915346ad7f918f93b9e0ff2cf02cb510d1080b3d27f579f1ab31c93%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%225c2ac33309a6465f9783bd731a8f42ab%22%7D&response_type=code&flowName=GeneralOAuthFlow")
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
                "/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div/div/div")
        mic_off.click()
        time.sleep(2)

        # turning off the camera
        
        cam_off = self.driver.find_element_by_xpath(
                "/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div/div")
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
                    print(people_number)
        
                except:
                    pass

                if people_number <=1:
                    break
        
                else:
                    pass


        time.sleep(3)

        self.driver.close()


##################################################################################

# main


if __name__ == "__main__":

    username = input("Enter Your Mail : ")
    password = input("Enter the password: ")
    meetlink = input("Enter the class link: ")

    meet_bot = Meetbot(username, password, meetlink)
            

            

#################################################################################

