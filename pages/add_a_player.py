import time
from os import name

from pages.base_page import BasePage


class AddAPlayer(BasePage):
    add_player_button_xpath = "//*/div[2]//button/span[1]"
    add_player_url = "https://scouts.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    age_field_xpath = "//*[@name='age']"
    main_position_field_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*/div[3]/button[1]"
    expected_position = "goalkeeper"
    second_position_field_xpath = "//*[@name='secondPosition']"
    add_language_button_xpath = "//*/div[15]//span[1]"
    languages_field_xpath = "//*[@name = 'languages[0]']"
    clear_button_xpath = "//*/button[2]/span[1]"
    phone_field_xpath = "//*[@name='phone']"
    weight_field_xpath = "//*[@name='weight']"
    height_field_xpath = "//*[@name='height']"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_xpath = "//li[1]"
    left_leg_xpath = "//li[2]"
    club_field_xpath = "//*[@name='club']"
    level_field_xpath = "//*[@name='level']"
    district_dropdown_xpath = "//*[@id='mui-component-select-district']"
    opole_xpath = "//li[8]"
    achievements_field_xpath = "//*[@name='achievements']"
    add_link_to_youtube_button_xpath = "//div[19]/button"
    youtube_field_xpath = "//div[19]//input"
    required_message_xpath = "//div/p"

    """Click on the element"""
    def click_on_the_add_player_button(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        self.click_on_the_element(self.add_player_button_xpath)

    def click_on_the_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_the_add_language_button(self):
        self.wait_for_visibility_of_element_located(self.add_language_button_xpath)
        self.click_on_the_element(self.add_language_button_xpath)

    def click_on_the_clear_button(self):
        self.wait_for_element_to_be_clickable(self.clear_button_xpath)
        self.click_on_the_element(self.clear_button_xpath)

    def select_leg(self, leg):
        self.wait_for_element_to_be_clickable(self.leg_dropdown_xpath)
        self.click_on_the_element(self.leg_dropdown_xpath)
        if leg == "right":
            self.wait_for_element_to_be_clickable(self.right_leg_xpath)
            self.click_on_the_element(self.right_leg_xpath)
        else:
            self.wait_for_element_to_be_clickable(self.left_leg_xpath)
            self.click_on_the_element(self.left_leg_xpath)

    def click_on_the_add_youtube_button(self):
        self.wait_for_element_to_be_clickable(self.add_link_to_youtube_button_xpath)
        self.click_on_the_element(self.add_link_to_youtube_button_xpath)

    def click_on_district_button(self):
        self.wait_for_element_to_be_clickable(self.district_dropdown_xpath)
        self.click_on_the_element(self.district_dropdown_xpath)

    def click_on_the_opole_button(self):
        self.wait_for_element_to_be_clickable(self.opole_xpath)
        self.click_on_the_element(self.opole_xpath)

    """type in data"""

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.second_position_field_xpath, second_position)

    def type_in_language_name(self, language):
        self.field_send_keys(self.languages_field_xpath, language)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)

    def type_in_club(self, club):
        self.field_send_keys(self.club_field_xpath, club)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_field_xpath, achievements)

    def type_in_level(self, level):
        self.field_send_keys(self.level_field_xpath, level)

    def add_link(self, youtube):
        self.field_send_keys(self.youtube_field_xpath, youtube)

    """assertions"""
    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_title
    def check_required_message_is_visible(self):
        try:
            self.wait_for_visibility_of_element_located(self.required_message_xpath)
            not_found = False
        except:
            not_found = True

        assert not_found

