from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 25)
    driver.get("https://www.bigaads.com/index.php")
    driver.find_element_by_name("username").send_keys("test.oliver.q@hotmail.com" + Keys.RETURN)
    driver.find_element_by_name("password").send_keys("Vbhjy_2018" + Keys.RETURN)
    driver.find_element_by_name("submit").send_keys(Keys.RETURN)
    driver.get("https://www.bigaads.com/BonusAds.php")

    driver.find_element_by_css_selector("button.allpageinside_allthepage_inside_pagein_adstoclickonce_actions_view").click()
    driver.find_element_by_xpath("//div[@id='allpageinside_allthepage_inside_pagein_viewadsporter']/a/button").click()
    element = wait.until(EC.element_to_be_clickable((By.ID, 'body_headerviewads_countdown_confirm_button')))
    element.click()

    driver.find_element_by_css_selector("button.allpageinside_allthepage_inside_pagein_adstoclickonce_actions_view").click()
    driver.find_element_by_xpath("//div[@id='allpageinside_allthepage_inside_pagein_viewadsporter']/a/button").click()
    element = wait.until(EC.element_to_be_clickable((By.ID, 'body_headerviewads_countdown_confirm_button')))
    element.click()

    driver.find_element_by_css_selector("button.allpageinside_allthepage_inside_pagein_adstoclickonce_actions_view").click()
    driver.find_element_by_xpath("//div[@id='allpageinside_allthepage_inside_pagein_viewadsporter']/a/button").click()
    element = wait.until(EC.element_to_be_clickable((By.ID, 'body_headerviewads_countdown_confirm_button')))
    element.click()

    driver.find_element_by_css_selector("button.allpageinside_allthepage_inside_pagein_adstoclickonce_actions_view").click()
    driver.find_element_by_xpath("//div[@id='allpageinside_allthepage_inside_pagein_viewadsporter']/a/button").click()
    element = wait.until(EC.element_to_be_clickable((By.ID, 'body_headerviewads_countdown_confirm_button')))
    element.click()

    driver.find_element_by_css_selector("button.allpageinside_allthepage_inside_pagein_adstoclickonce_actions_view").click()
    driver.find_element_by_xpath("//div[@id='allpageinside_allthepage_inside_pagein_viewadsporter']/a/button").click()
    element = wait.until(EC.element_to_be_clickable((By.ID, 'body_headerviewads_countdown_confirm_button')))
    element.click()

    driver.find_element_by_css_selector("button.allpageinside_allthepage_inside_pagein_adstoclickonce_actions_view").click()
    driver.find_element_by_xpath("//div[@id='allpageinside_allthepage_inside_pagein_viewadsporter']/a/button").click()
    element = wait.until(EC.element_to_be_clickable((By.ID, 'body_headerviewads_countdown_confirm_button')))
    element.click()

    driver.find_element_by_css_selector("button.allpageinside_allthepage_inside_pagein_adstoclickonce_actions_view").click()
    driver.find_element_by_xpath("//div[@id='allpageinside_allthepage_inside_pagein_viewadsporter']/a/button").click()
    element = wait.until(EC.element_to_be_clickable((By.ID, 'body_headerviewads_countdown_confirm_button')))
    element.click()

    driver.find_element_by_css_selector("button.allpageinside_allthepage_inside_pagein_adstoclickonce_actions_view").click()
    driver.find_element_by_xpath("//div[@id='allpageinside_allthepage_inside_pagein_viewadsporter']/a/button").click()
    element = wait.until(EC.element_to_be_clickable((By.ID, 'body_headerviewads_countdown_confirm_button')))
    element.click()

    driver.find_element_by_css_selector("button.allpageinside_allthepage_inside_pagein_adstoclickonce_actions_view").click()
    driver.find_element_by_xpath("//div[@id='allpageinside_allthepage_inside_pagein_viewadsporter']/a/button").click()
    element = wait.until(EC.element_to_be_clickable((By.ID, 'body_headerviewads_countdown_confirm_button')))
    element.click()

    driver.find_element_by_css_selector("button.allpageinside_allthepage_inside_pagein_adstoclickonce_actions_view").click()
    driver.find_element_by_xpath("//div[@id='allpageinside_allthepage_inside_pagein_viewadsporter']/a/button").click()
    element = wait.until(EC.element_to_be_clickable((By.ID, 'body_headerviewads_countdown_confirm_button')))
    element.click()