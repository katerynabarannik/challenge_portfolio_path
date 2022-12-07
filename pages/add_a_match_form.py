from pages.base_page import BasePage
import os
import time
import unittest
from selenium import webdriver

from pages.add_a_player import AddAPlayer
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class AddAMatch (BasePage):
    match_at_home_button_xpath = "//*[@value='true']"
    match_out_home_button_xpath = "//*[@value='false']"
    my_team_score_field_xpath = "//input[@name='myTeamScore']"
    enemy_team_score_field_xpath = "//input[@name='enemyTeamScore']"
    enemy_team_field_xpath = "//*[@name='enemyTeam']"
    my_team_field_xpath = "//*[@name='myTeam']"
    league_field_xpath = "//*[@name='league']"
    number_field_xpath = "//*[@name='number']"
    date_field_xpath = "//*[@name='date']"
    time_played_field_xpath = "//*[@name='timePlayed']"
    player_field_on_players_page = "//*[@id='MUIDataTableBodyRow-0993714736296742-3']"
    matches_button_on_players_page = "//*[text()='Matches']"
    add_match_button = "//*[text()='Add match']"
    def click_on_added_player(self):
        self.wait_for_element_to_be_clickable(self.player_field_on_players_page)
        self.click_on_the_element(self.player_field_on_players_page)

    def click_on_matches_button(self):
        self.wait_for_visibility_of_element_located(self.matches_button_on_players_page)
        self.click_on_the_element(self.matches_button_on_players_page)

    def click_on_the_add_match_button(self):
        self.wait_for_element_to_be_clickable(self.add_match_button)
        self.click_on_the_element(self.add_match_button)
        self.wait_for_visibility_of_element_located(self.match_at_home_button_xpath)
