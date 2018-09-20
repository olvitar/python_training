from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 25)

driver.get("https://coursehunters.net/")
driver.find_element_by_link_text("Sign In").click()
driver.find_element_by_xpath("//app-root/div/ng-component/div/form/div[1]/input").click()
driver.find_element_by_xpath("//app-root/div/ng-component/div/form/div[1]/input").clear()
driver.find_element_by_xpath("//app-root/div/ng-component/div/form/div[1]/input").send_keys("olvitar84@gmail.com")
driver.find_element_by_xpath("//app-root/div/ng-component/div/form/div[2]/input").click()
driver.find_element_by_xpath("//app-root/div/ng-component/div/form/div[2]/input").clear()
driver.find_element_by_xpath("//app-root/div/ng-component/div/form/div[2]/input").send_keys("Vbhjy_30")
driver.find_element_by_xpath("//app-root/div/ng-component/div/form/div[3]/button").click()
driver.save_screenshot('screenshot.png')
driver.get("https://coursehunters.net/")
driver.save_screenshot('screenshot1.png')

driver.find_element_by_class_name('style-scope.iron-icon').click()

driver.find_element_by_id("searchField").click()
driver.find_element_by_id("searchField").clear()
driver.find_element_by_id("searchField").send_keys("python")
driver.find_element_by_css_selector("button.submit-btn.search-form__button").click()
driver.find_element_by_link_text("Программирование на Python для тестировщиков").click()

driver.find_element_by_link_text("Categories").click()

print ("Test is OK")
driver.quit()