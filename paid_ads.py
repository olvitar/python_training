from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tokens import ADV_LOGIN, ADV_PASSWORD

driver = webdriver.Firefox()

def login():
    driver.get("https://www.bigaads.com/index.php")
    driver.find_element_by_name("username").send_keys(ADV_LOGIN)
    driver.find_element_by_name("password").send_keys(ADV_PASSWORD)
    driver.find_element_by_name("submit").send_keys(Keys.RETURN)
    driver.get("https://www.bigaads.com/Paidads.php")
    driver.save_screenshot('screenshot1.png')  # make a screenshot of the paige

def paid_adv():
    driver.find_element_by_css_selector(
        "button.allpageinside_allthepage_inside_pagein_adstoclickonce_actions_view").click()
    driver.find_element_by_xpath("//div[@id='allpageinside_allthepage_inside_pagein_viewadsporter']/a/button").click()
    element = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.ID, 'body_headerviewads_countdown_confirm_button')))
    element.click()

def logout():
    driver.find_element_by_partial_link_text('logout').click()

#start
login()
try:
    i: int = 0
    while i < 21:
        paid_adv()
        i += 1
        print("You watched ", i, " advertisement")
    print("Everything is Ok")
    logout()
except:
    print('You watched all bonus adverts for today or some issue is occurred. Check the screenshot.')
    footer = driver.find_element_by_class_name("socials") #find element Footer
    footer.location_once_scrolled_into_view  #scroll page to the element Footer
    driver.save_screenshot('screenshot1.png')  # make a screenshot of the paige
finally:
    driver.quit()
