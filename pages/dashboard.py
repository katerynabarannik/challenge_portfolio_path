import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts.futbolkolektyw.pl/'
    dev_team_contact_hyperlink_xpath = "//a[@href='https://app.slack.com/client/T3X4CAKNU/C3XTEGXB6']"
    players_field_xpath = "//*[text()='Players']"
    image_xpath = "//*[@title='Logo Scouts Panel']"
    scouts_panel_field_xpath = "//*[h2='Scouts Panel']"
    events_count_field_xpath = "//*//div[2]/div[4]/div"
    scouts_panel_header_xpath = "//*/header//h6"
    dev_team_contact_xpath = "//*/div[3]//a/span[1]"
    activity_field_xpath = "//*//div[3]/div[3]//h2"
    polski_field_xpath = "//*[text()='Polski']"
    shortcuts_field_xpath = "//*[text()='Shortcuts']"
    matches_count_field_xpath = "//*//div[2]/div[2]/div"
    add_player_button_xpath = "//*/div[2]//button/span[1]"
    last_created_match_xpath = "//div[3]//a[3]/button"
    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.players_field_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def wait_for_url_to_appear(self):
        url = ""
        while url == "":
            self.driver.get('https://scouts.futbolkolektyw.pl/en')
            self.wait_for_visibility_of_element_located(self.add_player_button_xpath)
            break

    def click_on_last_created_match_link(self):
        self.wait_for_element_to_be_clickable(self.last_created_match_xpath)
        self.click_on_the_element(self.last_created_match_xpath)

