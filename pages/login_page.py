from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[@type='password']"
    sign_in_button_xpath = "//*/button/span[1]"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = 'Scouts panel - sign in'
    title_of_box_xpath = "//*/div[1]/h5"
    header_of_box = "Scouts Panel"
    language_dropdown_xpath = "//*[@aria-haspopup]"
    POLISH_xpath = "//*[@data-value='pl']"
    ENGLISH_xpath = "//*[@data-value='en']"
    FAIlMESSAGE_xpath = "//div[3]/span"
    Polish_language = "Polski"
    English_language = "English"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.wait_for_visibility_of_element_located(self.sign_in_button_xpath)
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_title_of_header(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)

    def sign_in_to_the_system(self):
        self.type_in_email('user01@getnada.com')
        self.type_in_password('Test-1234')
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        self.click_on_the_element(self.sign_in_button_xpath)

    def check_language_is_switched(self):
        if self.POLISH_xpath:
            self.assert_element_text(self.driver, self.language_dropdown_xpath, self.Polish_language)
        elif self.ENGLISH_xpath:
            self.assert_element_text(self.driver, self.language_dropdown_xpath, self.English_language)


    def switch_language(self, language):
        self.wait_for_element_to_be_clickable(self.language_dropdown_xpath)
        self.click_on_the_element(self.language_dropdown_xpath)
        if language == "Polish":
            self.wait_for_element_to_be_clickable(self.POLISH_xpath)
            self.click_on_the_element(self.POLISH_xpath)
        else:
            self.wait_for_element_to_be_clickable(self.ENGLISH_xpath)
            self.click_on_the_element(self.ENGLISH_xpath)
