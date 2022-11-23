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

    def
    pass
