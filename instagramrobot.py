from time import sleep
from selenium import webdriver
import os
import random



path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path , 'chromedriver.exe')



#this is the oart for not showing the webbrowser
# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# browser = webdriver.Chrome(options=option)




browser = webdriver.Chrome()


# account generetor based on class
class Account():
    def __init__(self , username , password):
        self.username = username
        self.password = password



def getusername():
    usrname = input("username: ")
    return usrname

def getpassword():
    passwd = input("password: ")
    return passwd







def classinfo():
    username = getusername()
    password = getpassword()
    accnt = Account(username=username , password=password)
    return accnt



    


def login():



    AccountCredential = classinfo()



   
    

    browser.get("https://www.instagram.com")
    sleep(5)

    try:
        browser.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        sleep(10)
    except:
        pass
    

    sleep(3)
    username = AccountCredential.username
    password = AccountCredential.password
    sleep(5)
    UsernameEntry = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    UsernameEntry.send_keys(username)
    
    sleep(5)
    PasswordEntry = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    PasswordEntry.send_keys(password)


    sleep(5)
    loginbutton = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    loginbutton.click()

    sleep(5)

    print("I'M IN!")


def hashtaglike():
    login()

    
    # thi is the part that it will search for your hashtag in explore
    sleep(2)
    tag = input('pls enter ur tag: ')
    browser.get('https://instagram.com/explore/tags/' + tag)
    howmany = int(input("how many post do you want me to like? "))
    sleep(7)
    # thi is the part that it will search for your hashtag in explore




    
    # this is a part that will click on the first post in the tag
    post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[1]/div[1]/a/div/div[2]')
    post.click()
    sleep(5)
    # this is a part that will click on the first post in the tag


#====================== this is the first like button in hastag
    fliking = browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[2]')
    fliking.click()
    sleep(1)
    print("LIKED")
    sleep(5)


    # this is the part that will click on the first next button
    nxtpostp1 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/button')
    nxtpostp1.click()
    sleep(7)
    # this is the part that will click on the first next button



#====================== this is the second like button in hastag
    tliking = browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
    tliking.click()
    sleep(1)
    print("LIKED")
    sleep(5)



    # this is the part that will click on the other next buttons
    for i in (1 , (howmany-3)):
        nextpost = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/button')
        nextpost.click()
        sleep(7)
    # this is the part that will click on the other next buttons


    #====================== this is the liking button in hastag in loop
        bliking = browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
        bliking.click()
        sleep(5)
        print("LIKED\n")



def hashtagsave():
    login()

    sleep(2)
    tag = input('pls enter ur tag: ')
    browser.get('https://instagram.com/explore/tags/' + tag)
    sleep(2)
    print("I'M IN HASHTAG PART")
    hwomany = int(input("how many post do you want me to save? "))
    sleep(5)



    #===============this is for opening the first post in tag
    post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[1]/div[1]/a/div/div[2]')
    post.click()
    sleep(2)
    print("I OPENED THE FIRST POST!")
    sleep(3)

    #===============this is for saving the first post in tag
    sleep(3)
    fsaving = browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div')
    fsaving.click()
    sleep(5)
    print("SAVED!\n")



    #===============this is for the first next post button
    nxtpostp1 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/button')
    nxtpostp1.click()
    sleep(2)
    print("I CLICKED ON THE NEXT POST BUTTON")
    sleep(5)


    #==============this is for saving the second post in tag
    ssaving = browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div')
    ssaving.click()
    sleep(3)
    print("SAVED!\n")




    #==============this is a while loop for the next post button
    for i in (1 , (hwomany-3)):
        nextpost = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/button')
        nextpost.click()
        sleep(2)
        print("I CLICKED ON THE NEXT POST BUTTON")
        sleep(5)
        

        #==================this is saving part for loop in hashtag
        saving = browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div')
        saving.click()
        sleep(5)
        print("SAVED!\n")





def hashtagcommenter():
    login()

    CommonComment = [ 'NICE' , 'AWESOME' , 'PERFECT' , 'WOW']
    cmnt  = random.choice(CommonComment)
    


    tag = input('enter ur tag: ')
    browser.get('https://instagram.com/explore/tags/' + tag)
    sleep(2)
    print("I'M IN HASHTAG PART")
    howmany = int(input("how many post do ypou want me to comment? "))
    sleep(5)


    #===========================opening the first pst in tags
    post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[1]/div[1]/a/div/div[2]')
    post.click()
    sleep(2)
    print("I OPENED THE FIRST POST!")
    sleep(3)
    #===========================clicking on the comment button
    sleep(10)
    browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button').click()
    #============================sendng the word for commenting
    browser.find_element_by_class_name('Ypffh').send_keys(cmnt)
    #============================ckicking on the ppost for posting the comment
    browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button').click()
    sleep(2)
    print('COMMENTED!')


    #===============this is for the first next post button
    nxtpostp1 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/button')
    nxtpostp1.click()
    sleep(2)
    print("I CLICKED ON THE NEXT POST BUTTON")
    sleep(5)



    #=============this is for commentning on the second next button
    sleep(10)
    browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button').click()
    #============================sendng the word for commenting
    browser.find_element_by_class_name('Ypffh').send_keys(cmnt)
    #============================ckicking on the ppost for posting the comment
    browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button').click()
    sleep(2)
    print('COMMENTED!')





    #==============this is a while loop for the next post button
    for i in (1 , (howmany-3)):
        nextpost = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/button')
        nextpost.click()
        sleep(2)
        print("I CLICKED ON THE NEXT POST BUTTON")
        sleep(5)


        sleep(10)
        browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button').click()
        #============================sendng the word for commenting
        browser.find_element_by_class_name('Ypffh').send_keys(cmnt)
        #============================ckicking on the ppost for posting the comment
        browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button').click()
        sleep(2)
        print('COMMENTED!')





def unfollowers():
    login()



    browser.get('https://instagram.com/testtestian12/')
    sleep(3)


    # following are here!!!!
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]').click()
    sleep(5)

    followingusername =[]
    i = 1

    try:
        while(True):
            creds = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/ul/div/li[' + str(i) + ']' ).text

            credslst = creds.split('\n')
            followingusername.append(credslst[0])
            i += 1



    except:
        print(followingusername)
    browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[1]/div/div[3]/div/button').click()
    sleep(5)


    # followers are here!!!
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]').click()
    sleep(5)


    followerusername = []
    j = 1


    try:
        while(True):

            credents = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/ul/div/li[' + str(j) + ']').text
            credentslst = credents.split('\n')
            followerusername.append(credentslst[0])
            j += 1

    

    except:
        print(followerusername)


    #creating a list from assholes!
    l3 = [x for x in followingusername if x not in followerusername]
    print( f"assholes who are not following you are: {l3}")



    #unfollowing them!!
    for item in l3:
        browser.get('https://www.instagram.com/' + item)
        sleep(3)
        answer = input("do you want to unfollow this person?(y for yes and n for no) ")
        if answer == "y":
            try:
                browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button').click()
                sleep(1)
                browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
                sleep(2)
            except:
                browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button').click()
                sleep(1)
                browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
                sleep(2)




command = input("what do you want?(login for login\n\
    hlike for liking the post in nhastag part\n\
        hsave for saving the post in nhastag part\n\
            hcomment for commenting the post in nhastag part\n\
                findunfollower for finding unfollowers!\n")


if command == "login":
    login()

if command == "hlike":
    hashtaglike()

if command == "hsave":
    hashtagsave()

if command == "hcomment":
    hashtagcommenter()

if command == "findunfollower":
    unfollowers()