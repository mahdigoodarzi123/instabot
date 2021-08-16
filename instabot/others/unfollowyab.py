from instapy import instapy


username_input = "testtestian12"
password_input = "Asdfghjkl!@"

session = instapy.InstaPy(username=username_input , password=password_input)
session.login()



session.unfollow_users(amount=5 , nonFollowers=True , unfollow_after= 0 , sleep_delay= 600 )