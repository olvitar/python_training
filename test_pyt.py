# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from tokens import PYT_LOGIN, PYT_PASSWORD
import  unittest

class test_pyt(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
    
    def test_test_pyt(self):

        wd = self.wd
        self.open_home_page(wd)
        assert "Python" in wd.title
        wd.find_element_by_link_text("Documentation").click()
        wd.find_element_by_link_text("Python Videos").click()
        self.open_home_page(wd)
        self.open_PyPi_page(wd)
        self.PyPi_login(wd, username = PYT_LOGIN, password = PYT_PASSWORD)
        self.search_method(wd, "pytest")
        assert "No results found." not in wd.page_source
        wd.find_element_by_css_selector("span.package-snippet__name").click()
        wd.find_element_by_link_text("Software Development :: Testing").click()
        self.logout(wd)


    def logout(self, wd):
        wd.find_element_by_css_selector("button.horizontal-menu__link.dropdown__trigger").click()
        wd.find_element_by_css_selector("button.dropdown__link").click()

    def search_method(self, wd, search_word):
        wd.find_element_by_id("search").click()
        wd.find_element_by_id("search").clear()
        wd.find_element_by_id("search").send_keys(search_word)
        wd.find_element_by_css_selector("button.search-form__button").click()

    def PyPi_login(self, wd, username, password):
        wd.find_element_by_link_text("Log in").click()
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_css_selector("input.button.button--primary").click()

    def open_PyPi_page(self, wd):
        wd.find_element_by_link_text("PyPI").click()

    def open_home_page(self, wd):
        wd.get("https://www.python.org/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
