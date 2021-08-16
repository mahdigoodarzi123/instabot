from selenium import webdriver
import os
from time import sleep

#I was using chrome so i selected this path for chromedrive.exe
path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path , 'chromedriver.exe')

browser = webdriver.Chrome()


browser.get("https://www.instagram.com/")

sleep(5)


#login information's
username = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys('your username')
sleep(2)
password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys('your password')


#login buttom
sleep(2)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()


#the first not now buttom
sleep(10)
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()


#the second not now buttom
sleep(10)
browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()


#clicking on expelor
browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()


#tag search part
sleep(2)
browser.get("https://www.instagram.com/explore/tags" + "your tag")

#opening third(idk why?) post (copy,paste xpath of the post that you want)
sleep(3)
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[3]').click()


#like third post (copy,paste xpath of the post that you want)
sleep(3)
browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()

#comment part (copy,paste xpath of the post that you want)
sleep(3)
browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys('instagram robot checker')
browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]').click()
