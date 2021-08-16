#this is a login bot using selenium!
from selenium import webdriver


#this is just for firefox and you should have the geckodriver.exe
browser = webdriver.Firefox()

#instagram url
browser.get('https://www.instagram.com/')



#the part that you gave username and password
username = input("username: ")
password = input("password: ")

#defining the username and password places
username_input = browser.find_element_by_css_selector("div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")
password_input = browser.find_element_by_css_selector("div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")

#using and writng username and password on their places
username_input.send_keys(username)
password_input.send_keys(password)

#defining login button and pressing it
login_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
login_button.click()
