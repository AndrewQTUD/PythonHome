from selenium import webdriver
import time
import threading


while True:
    web = webdriver.Chrome()

    web.get('https://docs.google.com/forms/d/e/1FAIpQLSdPzvXQr9p6uQ3wTUfQgc8KBtMNTq5R07KQ0YE1DqJMxzTzdg/viewform')

    time.sleep(4)

    name = "hello Olivia"
    name1 = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name1.send_keys(name)
    time.sleep(1)

    email = "Did you like what I did?"
    email1 = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email1.send_keys(email)

    interestIn = web.find_element_by_xpath('//*[@id="i17"]/div[2]')
    interestIn.click()

    achievement = "It's funny?"
    ach = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')
    ach.send_keys(achievement)

    tf = "Thought you might like it :)"
    timeframe = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')
    timeframe.send_keys(tf)

    submitBtn = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submitBtn.click()
