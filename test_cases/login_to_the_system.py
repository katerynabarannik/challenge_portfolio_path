import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT



class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.check_title_of_header()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_for_url_to_appear()
        dashboard_page.title_of_page()


    def test_login_to_the_system_with_empty_fields(self):
        user_login = LoginPage(self.driver)
        user_login.click_on_the_sign_in_button()
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot('D:\TC_6.png')
        user_login.check_empty_fields_message()

    def test_login_to_the_system_with_invalid_password(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Rest')
        user_login.click_on_the_sign_in_button()
        self.driver.save_screenshot('D:\TC_7.png')
        user_login.check_invalid_data_message()
        time.sleep(5)

    def test_sign_in_and_out_of_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.log_in_log_out()
        self.driver.implicitly_wait(5)

    def test_change_language(self):
        user_login = LoginPage(self.driver)
        user_login.switch_language('Polish')
        time.sleep(5)

    def test_sign_in(self):
        user_login = LoginPage(self.driver)
        user_login.sign_in_to_the_system()
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot('D:\TC_10.png')

    @classmethod
    def tearDown(self):
        self.driver.quit()

