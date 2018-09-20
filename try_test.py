# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

success = True
wd = webdriver.Firefox()
wait = WebDriverWait(wd, 22)


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://www.python.org/")
    wd.find_element_by_css_selector("button").click()
    wd.find_element_by_link_text("Success Stories").click()
    wd.find_element_by_css_selector("button").click()
    wd.find_element_by_link_text("About").click()
    wd.find_element_by_css_selector("button").click()
    wd.find_element_by_link_text("Docs").click()
    wd.find_element_by_link_text("Audio/Visual Talks").click()
    wd.find_element_by_css_selector("button").click()
    wd.find_element_by_link_text("PyPI").click()
    wd.find_element_by_link_text("Log in").click()
    wd.find_element_by_id("username").click()
    wd.find_element_by_id("username").clear()
    wd.find_element_by_id("username").send_keys("oliver")
    wd.find_element_by_id("password").click()
    wd.find_element_by_id("password").clear()
    wd.find_element_by_id("password").send_keys("Vbhjy_30")
    wd.find_element_by_css_selector("input.button.button--primary").click()
    wd.find_element_by_id("search").click()
    wd.find_element_by_id("search").clear()
    wd.find_element_by_id("search").send_keys("python")
    wd.find_element_by_css_selector("button.search-form__button").click()
    wd.find_element_by_xpath("//form[@id='classifiers']//button[.='Topic']").click()
    wd.find_element_by_xpath("//form[@id='classifiers']//button[.='Topic']").click()
    wd.find_element_by_id("search").click()
    wd.find_element_by_id("search").clear()
    wd.find_element_by_id("search").send_keys("pytest")
    wd.find_element_by_css_selector("button.search-form__button").click()
    wd.find_element_by_css_selector("button.horizontal-menu__link.dropdown__trigger").click()
    wd.find_element_by_css_selector("button.dropdown__link").click()
    print("Everything is Ok")
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
