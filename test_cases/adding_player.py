import os
import time
import unittest
from selenium import webdriver

from pages.add_a_player import AddAPlayer
from pages.login_page import LoginPage

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_adding_player(self):
        user_login = LoginPage(self.driver)
        user_login.sign_in_to_the_system()
        add_a_player_page = AddAPlayer(self.driver)
        add_a_player_page.click_on_the_add_player_button()
        add_a_player_page.type_in_name('Manuel')
        add_a_player_page.type_in_surname('Neuer')
        add_a_player_page.type_in_phone('0985458521')
        add_a_player_page.type_in_weight('85')
        add_a_player_page.type_in_height('195')
        add_a_player_page.type_in_age('03271986')
        add_a_player_page.select_leg('right')
        add_a_player_page.type_in_club('Bayern')
        add_a_player_page.type_in_level('master')
        add_a_player_page.type_in_main_position('goalkeeper')
        add_a_player_page.type_in_second_position('striker')
        add_a_player_page.click_on_district_button()
        add_a_player_page.click_on_the_opole_button()
        add_a_player_page.type_in_achievements('Golden Glove')
        add_a_player_page.click_on_the_add_language_button()
        add_a_player_page.type_in_language_name('German')
        add_a_player_page.click_on_the_add_youtube_button()
        add_a_player_page.add_link("www.youtube.com")
        add_a_player_page.click_on_the_submit_button()
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot('D:\TC_5.png')
        add_a_player_page.title_of_page()


    def test_adding_player_with_valid_data_in_required_fields(self):
        user_login = LoginPage(self.driver)
        user_login.sign_in_to_the_system()
        add_a_player_page = AddAPlayer(self.driver)
        add_a_player_page.click_on_the_add_player_button()
        add_a_player_page.type_in_name('Andriy')
        add_a_player_page.type_in_surname('Shevchenko')
        add_a_player_page.type_in_age('09291976')
        add_a_player_page.type_in_main_position('striker')
        add_a_player_page.click_on_the_submit_button()
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot('D:\TC_1.png')


    def test_adding_player_with_empty_required_field(self):
        user_login = LoginPage(self.driver)
        user_login.sign_in_to_the_system()
        add_a_player_page = AddAPlayer(self.driver)
        add_a_player_page.click_on_the_add_player_button()
        add_a_player_page.type_in_name('Andriy*')
        add_a_player_page.type_in_second_position('+g0alkeeper')
        add_a_player_page.click_on_the_submit_button()
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot('D:\TC_2.png')

    def test_clearing_the_form(self):
        user_login = LoginPage(self.driver)
        user_login.sign_in_to_the_system()
        add_a_player_page = AddAPlayer(self.driver)
        add_a_player_page.click_on_the_add_player_button()
        add_a_player_page.click_on_the_add_language_button()
        add_a_player_page.type_in_language_name('English')
        add_a_player_page.click_on_the_clear_button()
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot('D:\TC_3.png')

    def test_leaving_empty_form(self):
        user_login = LoginPage(self.driver)
        user_login.sign_in_to_the_system()
        add_a_player_page = AddAPlayer(self.driver)
        add_a_player_page.click_on_the_add_player_button()
        add_a_player_page.click_on_the_submit_button()
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot('D:\TC_4.png')

    @classmethod
    def tearDown(self):
        self.driver.quit()


