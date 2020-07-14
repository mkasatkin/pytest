import pytest
from selenium import webdriver
import math
import time


link = "https://stepik.org/lesson/236895/step/1"
b = link

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestStepikUFO():

    @pytest.mark.xfail
    def test_open_and_find_solution('link1',
            [https://stepik.org/lesson/236895/step/1,
             https://stepik.org/lesson/236895/step/1,
    https://stepik.org/lesson/236895/step/1,
    https://stepik.org/lesson/236895/step/1,
    https://stepik.org/lesson/236895/step/1,
    https://stepik.org/lesson/236895/step/1,
    https://stepik.org/lesson/236895/step/1,
    ]):
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        st = browser.find_element_by_css_selector("textarea")
        answer = math.log(int(time.time()))
        st.send_keys(str(answer))
        s1 = browser.find_element_by_css_selector("ember239 > pre").text

    @pytest.mark.xfail
    def test_open_and_find_solutio(self, browser):
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        st = browser.find_element_by_css_selector("textarea")
        answer = math.log(int(time.time()))
        st.send_keys(str(answer))

    @pytest.mark.xfail
    def test_open_and_find_soluti(self, browser):
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        st = browser.find_element_by_css_selector("textarea")
        answer = math.log(int(time.time()))
        st.send_keys(str(answer))

    @pytest.mark.xfail
    def test_open_and_find_solut(self, browser):
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        st = browser.find_element_by_css_selector("textarea")
        answer = math.log(int(time.time()))
        st.send_keys(str(answer))

    @pytest.mark.xfail
    def test_open_and_find_solu(self, browser):
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        st = browser.find_element_by_css_selector("textarea")
        answer = math.log(int(time.time()))
        st.send_keys(str(answer))

    @pytest.mark.xfail
    def test_open_and_find_sol(self, browser):
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        st = browser.find_element_by_css_selector("textarea")
        answer = math.log(int(time.time()))
        st.send_keys(str(answer))


    @pytest.mark.xfail
    def test_open_and_find_so(self, browser):
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        st = browser.find_element_by_css_selector("textarea")
        answer = math.log(int(time.time()))
        st.send_keys(str(answer))

    @pytest.mark.xfail
    def test_open_and_find_s(self, browser):
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        st = browser.find_element_by_css_selector("textarea")
        answer = math.log(int(time.time()))
        st.send_keys(str(answer))



