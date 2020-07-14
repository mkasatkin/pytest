import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["https://stepik.org/lesson/236895/step/1",
                                      "https://stepik.org/lesson/236896/step/1",
                                      "https://stepik.org/lesson/236897/step/1",
                                      "https://stepik.org/lesson/236898/step/1",
                                      "https://stepik.org/lesson/236899/step/1",
                                      "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236904/step/1",
                                      "https://stepik.org/lesson/236905/step/1"])

def test_open_and_find_solution(browser, language):
    link = language
    browser.get(link)
    browser.implicitly_wait(10)
    st = browser.find_element_by_css_selector("textarea")
    answer = math.log(int(time.time()))
    st.send_keys(str(answer))
    st2 = browser.find_element_by_xpath("//section/div/div[2]/div[4]/button")
    st2.click()
    browser.implicitly_wait(10)
    st3 = browser.find_element_by_xpath("//section/div/div[1]/div/pre")
    x = st3.text
    assert x == "Correct!", "Fatal Error"








