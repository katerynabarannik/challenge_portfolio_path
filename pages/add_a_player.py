import time
from pages.base_page import BasePage


class AddAPlayer(BasePage):
    add_player_button_xpath = "//*/div[2]//button/span[1]"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        time.sleep(4)
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    pass

