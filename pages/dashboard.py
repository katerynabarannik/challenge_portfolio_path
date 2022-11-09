from pages.base_page import BasePage


class Dashboard(BasePage)

    kla_kla_hyperlink_xpath = "//a[@href="https://app.slack.com/client/T3X4CAKNU/C3XTEGXB6"]"
    players_field_xpath = "//*[text()="Players"]"
    image_xpath = "//*[@title="Logo Scouts Panel"]"
    main_paige_icon_xpath = "//*[@class="MuiSvgIcon-root jss29 jss146"]"
    players_icon_xpath = "//*[@class="MuiSvgIcon-root jss29 jss158"]"
    scouts_panel_field_xpath = "//*[h2="Scouts Panel"]"
    events_count_field_xpath = "//*[@style="padding: 16px; border-left: thick solid rgb(0, 150, 136);"]"
    scouts_panel_header_xpath = "//*[@id="__next"]//header//h6"
    dev_team_contact_xpath = "//*[@id="__next"]//main/div[3]//a/span[1]"
    activity_field_xpath = "//*[@id="__next"]//main/div[3]/div[3]//h2"

    pass