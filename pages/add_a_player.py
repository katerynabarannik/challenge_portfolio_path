import time
from pages.base_page import BasePage


class AddAPlayer(BasePage):
    add_player_button_xpath = "//*/div[2]//button/span[1]"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    age_field_xpath = "//*[@name='age']"
    main_position_field_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*/div[3]/button[1]"
    expected_position = "goalkeeper"
    def click_on_the_add_player_button(self):
        time.sleep(5)
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)


    def click_on_the_submit_button(self):
        time.sleep(5)
        self.click_on_the_element(self.submit_button_xpath)
