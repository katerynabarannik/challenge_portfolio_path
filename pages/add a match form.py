from pages.base_page import BasePage


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

    pass
