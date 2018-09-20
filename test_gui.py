from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def test_gui():
    driver = webdriver.Chrome()
    driver.get("http://selenium2.ru/")
    assert driver.current_url == "https://selenium2.ru/"
    search_field = driver.find_element_by_name("searchword")
    search_field.clear()
    search_field.send_keys("python" + Keys.ENTER)
    result = driver.find_element_by_css_selector("div.searchintro")
#    assert result.text == "Total: 44 results found."
    assert "No results found." not in driver.page_source
    driver.quit()