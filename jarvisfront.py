import pyttsx3
import pyjokes
import re
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


web_login_details = {
    "linkedin" : ['//input[@id="username"]', '//input[@id="password"]'],
    "instagram" : ['//input[@name="username"]', '//input[@name="password"]'],
    "github" : ['//input[@name="login"]', '//input[@name="password"]'],
    "facebook" : ['//input[@name="email"]', '//input[@name="pass"]'],
    "twitter" : ['//input[@name="username"]', '//input[@autocomplete="current-password"]'],
    "discord" : ['//input[@name="email"]', '//input[@name="password"]']
}
web_search_details = {
    "google" : ["https://www.google.com", '//input[@class="search-field"]'],
    "yahoo" : ["https://in.search.yahoo.com/", '//input[@class="sbq"'],
    "wikipedia" : ["https://wikipedia.org", '//input[@id="searchInput"]'],
    "youtube" : ["https://youtube.com", '//input[@class="ytd-searchbox"]'],
    "weather" : ["https://weather.com", '//input[@id="LocationSearch_input"'],
    "twitter" :["https://twitter.com/explore", '//input[@class"r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-xyw6el r-13rk5gd r-1dz5y72 r-fdjqy7 r-13qz1uu"'],
    "github" : ["https://github.com", '//input[@class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"'],
    "linkedIn" : ["https://in.linkedin.com/jobs", '//input[@class="dismissable-input__input font-sans text-md text-color-text bg-color-transparent flex items-center flex-1 focus:outline-none"'],
    "msn" : ["https://www.msn.com", '//input[@type="search"'],
    "imdb" : ["https://imdb.com", '//input[@class="imdb-header-search__input searchTypeahead__input react-autosuggest__input"']
}


class Website:
    def __init__(self, sitename, search_info):
        self.sitename = sitename
        self.search_info = search_info

    def open_web_and_search(self):
        if self.search_info == False:
            if self.sitename not in web_login_details.keys():
                browser = webdriver.Chrome("C:\Program Files\chromedriver.exe")
                browser.get(f"https://www.google.com/search?q={self.sitename}")
                print(f"Jarvisfront: Searching web for '{self.sitename}'")
                speak(f"Searching web for '{self.sitename}'")
            else:
                self.login_and_use()
        else:
            browser = webdriver.Chrome("C:\Program Files\chromedriver.exe")
            print(f"Jarvisfront: Opening {self.sitename} in web")
            speak(f"Opening {self.sitename} in web")
            browser.get(web_search_details[self.sitename][0])
            browser.implicitly_wait(5)
            print(f"Jarvisfront: Searhing for {self.search_info} on {self.sitename}")
            speak(f"Searhing for {self.search_info} on {self.sitename}")
            search_bar = browser.find_element(By.XPATH, web_search_details[self.sitename][1])
            search_bar.click()
            search_bar.send_keys(self.search_info)
            search_bar.send_keys(Keys.ENTER)
        time.sleep(43200)

    def login_and_use(self):
        speak(f"Enter username of your {self.sitename}")
        username_str = input(f"Enter your {self.sitename} username: ")
        speak(f"Enter your {self.sitename} password")
        password_str = input(f"Enter your {self.sitename} password: ")
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(self.sitename)
        browser.implicitly_wait(5)
        username = browser.find_element(By.XPATH, web_login_details[self.sitename][0])
        username.send_keys(username_str)
        password = browser.find_element(By.XPATH, web_login_details[self.stiename][1])
        password.send_keys(password_str)
        password.send_keys(Keys.ENTER)


sys_apps = {
    "explorer" : "explorer",
    "cmd" : "cmd",
    "notepad" : "notepad",
    "word" : "winword",
    "excel" : "excel",
    "onenote" : "onenote",
    "edge" : "msedge",
    "powerpoint" : "powerpnt",
    "windows media player" : "wmplayer",
    "outlook" : "outlook",
    "calculator" : "calc",
    "visual studio code" : "code"
}


class Applications:
    def __init__(self, app_name):
        self.app_name = app_name
    status = True
    def open_app(self):
        try:
            for name in sys_apps:
                if name in self.app_name:
                    print("Jarvisfront: Opening", self.app_name)
                    speak(f"Opening {self.app_name}")
                    os.startfile(sys_apps[name])
                    break
            else:
                print("Jarvisfront: Opening", self.app_name)
                speak(f"Opening {self.app_name}")
                os.startfile(self.app_name)
        except:
            print("-The requested application was not found in system. Redirecting to web...")
            self.status = False
            


class TimeAndDate:
    data = datetime.datetime.now()

    @classmethod
    def time_now(cls):
        speak(cls.data.strftime("%I %M %p"))
        print("Time: "+ cls.data.strftime("%I:%M %p"))

    @classmethod
    def date_tdy(cls):
        speak(cls.data.strftime("%B %d, %Y"))
        print("Date: " + cls.data.strftime("%B %d, %Y"))

    @classmethod    
    def day_tdy(cls):
        speak(cls.data.strftime("%A"))
        print("Day: "+cls.data.strftime("%A"))
    
    @classmethod
    def dec_func(cls, date_or_time):
        if date_or_time == "date":
            cls.date_tdy()
        else:
            cls.time_now()

def say_a_joke():
    joke = pyjokes.get_joke(language="en", category="neutral")
    print(joke)
    speak(joke)


def speak(user_command):
    speech = pyttsx3.init("sapi5", True)
    speech.setProperty("rate", 178)
    speech.say(user_command)
    speech.runAndWait()

