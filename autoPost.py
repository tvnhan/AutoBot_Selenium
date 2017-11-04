# -*- coding: utf-8 -*-
#author: @tcchtnn
# Nov 5th 2017

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    print("hello")
    #infomation of account
    userEmail = "" #input your email here
    pwd = ""  # input your password here

    #infomation of post
    message = "Hello, I am a autobot. I will destroy the world!!! \n kakaka. "
    group_links = ["https://www.facebook.com/groups/1947000132181181/"]

    #declear the webdriver
    profile = webdriver.ChromeOptions()
    # profile.set_preference("browser.cache.disk.enable", False)
    # profile.set_preference("browser.cache.memory.enable", False)
    # profile.set_preference("browser.cache.offline.enable", False)
    # profile.set_preference("network.http.use-cache", False)

    driver = webdriver.Chrome()
    driver.implicitly_wait(15) #seconds
    wait = WebDriverWait(driver, 10)

    #Login to facebook
    driver.get("http://www.facebook.org")
    elem = driver.find_element_by_id("email")
    elem.send_keys(userEmail)
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)
    driver.implicitly_wait(5) #seconds

    print("Logined")

    for group in group_links:

        #Goto the facebook group
        driver.get(group)

        # Click the post box
        post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
        post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
        post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
        sleep(10)
        post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
        post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")

        # Enter the text we want to post to Facebook
        post_box.send_keys(message)
        sleep(10)

        print("insert message")
        # Get the 'Post' button and click on it
        try:
            another_layer_cancle_button = driver.find_element_by_xpath(
                "//*[@class='layerCancel _4jy0 _4jy3 _517h _51sy _42ft']")
            another_layer_cancle_button.click()
            sleep(5)
        except ValueError as e:
            print("got it :-) ", e)


        print("get post button")
        #get post button
        try:
            post_button = driver.find_element_by_xpath(
                "//*[@class='_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
            post_button.click()
            sleep(5)
        except ValueError as e:
            print("got it :-) ", e)
        print("FINISH")

if __name__ == '__main__':
    main()
