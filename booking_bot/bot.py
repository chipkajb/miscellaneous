from pdb import set_trace as bp
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.website.com'
date = '01/01/2020'
time_slot = -1
add_quantity = True

email = 'email@email.com'
pwd = 'pwd123'

# open website
driver = webdriver.Chrome(executable_path='/home/jordan/workspace/booking_bot/chromedriver_linux64/chromedriver')
driver.get(url)
driver.maximize_window()

# login
driver.find_elements_by_xpath("//button[@id='ga-global-nav-log-in-link']")[0].click()
driver.find_elements_by_xpath("//input[@id='rec-acct-sign-in-email-address']")[0].send_keys(email)
driver.find_elements_by_xpath("//input[@id='rec-acct-sign-in-password']")[0].send_keys(pwd)
driver.find_elements_by_xpath("//button[@type='submit' and @title='Log In']")[0].click()

booked = False
attempt_counter = 1
while not booked:
    print('Attempt {}'.format(attempt_counter))

    # select date
    try:
        driver.find_element_by_name('tourCalendarWithKey').send_keys('')
        for i in range(len(date)):
            webdriver.ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
        driver.find_element_by_name('tourCalendarWithKey').send_keys(date)
    except:
        pass
    
    # add quantity
    try:
        if add_quantity:
            driver.find_elements_by_xpath("//button[@id='guest-counter']")[0].click()
            driver.find_elements_by_xpath(
                        "//button[@type='button' and @aria-label='Add Vehicle 7-Day Entrys']")[0].click()
            driver.find_elements_by_xpath(
                    "//button[@type='button' and @class='sarsa-button sarsa-button-link sarsa-button-md']")[0].click()
    except:
        pass
    
    # select starting time
    success = False
    counter = 0
    while not success:
        try:
            driver.find_elements_by_xpath("//div[@class='te-radio-pill-time']")[time_slot].click()
            success = True
        except:
            counter += 1
            if counter > 200:
                break
            pass
    
    # add to cart
    try:
        driver.find_elements_by_class_name(
                "sarsa-button.sarsa-button-primary.sarsa-button-md.sarsa-button-fit-container")[0].click()
    except:
        pass
    
    # check if we are in cart
    success = False
    counter = 0
    while not success:
        try:
            driver.find_elements_by_xpath("//input[@id='first-name']")[0].send_keys('')
            success = True
            booked = True
        except:
            counter += 1
            if counter > 200:
                break
            pass

    attempt_counter += 1
