#this is a login bot using instapy!
from instapy import instapy

username_input = input("enter your username: ")
password_input = input("enter your password: ")

session = instapy.InstaPy(username=username_input , password=password_input)
session.login()
