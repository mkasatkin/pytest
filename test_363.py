import pytest
from selenium import webdriver
import math
import time



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestStepikUFO():

    @pytest.mark.parametrize('language', ["https://stepik.org/lesson/236895/step/1",
                                          "https://stepik.org/lesson/236896/step/1",
                                          "https://stepik.org/lesson/236897/step/1",
                                          "https://stepik.org/lesson/236898/step/1",
                                          "https://stepik.org/lesson/236899/step/1",
                                          "https://stepik.org/lesson/236903/step/1",
                                          "https://stepik.org/lesson/236904/step/1",
                                          "https://stepik.org/lesson/236905/step/1"])
    def test_open_and_find_solution(self, browser, language):
        browser.implicitly_wait(10)
        link = {language}
        browser.get(link)
        st = browser.find_element_by_css_selector("textarea")
        answer = math.log(int(time.time()))
        st.send_keys(str(answer))







