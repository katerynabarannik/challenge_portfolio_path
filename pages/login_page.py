import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@type='password']"
    sign_in_button_xpath = "//*/button/span[1]"
    login_url = ('https://scouts.futbolkolektyw.pl/en/')
    expected_title = 'Scouts panel - sign in'
    title_of_box_xpath = "//*/div[1]/h5"
    header_of_box = "Scouts Panel"
    language_dropdown_xpath = "//*[@aria-haspopup]"
    POLISH_xpath = "//*[@data-value='pl']"
    ENGLISH_xpath = "//*[@data-value='en']"
    FAIlMESSAGE_xpath = "//div[3]/span"
    Polish_language = "Polski"
    English_language = "English"
    sign_out_button_xpath = "//ul[2]/div[2]"
    invalid_data_message = "Identifier or password invalid."
    empty_fields_message = "Please provide your username or your e-mail."

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
        self.wait_for_visibility_of_element_located(self.sign_out_button_xpath)

    def switch_language(self, language):
        self.wait_for_element_to_be_clickable(self.language_dropdown_xpath)
        self.click_on_the_element(self.language_dropdown_xpath)
        if language == "Polish":
            self.wait_for_element_to_be_clickable(self.POLISH_xpath)
            self.click_on_the_element(self.POLISH_xpath)
            self.assert_element_text(self.driver, self.language_dropdown_xpath, self.Polish_language)

        else:
            self.wait_for_element_to_be_clickable(self.ENGLISH_xpath)
            self.click_on_the_element(self.ENGLISH_xpath)
            self.assert_element_text(self.driver, self.language_dropdown_xpath, self.English_language)

    def click_on_the_sign_out_button(self):
        self.wait_for_visibility_of_element_located(self.sign_out_button_xpath)
        self.wait_for_element_to_be_clickable(self.sign_out_button_xpath)
        self.click_on_the_element(self.sign_out_button_xpath)

    def log_in_log_out(self):
        list_of_mails = ['user01@getnada.com', 'user02@getnada.com']
        list_of_passwords = ['Test-1234', 'Test-1234']
        for a in list_of_mails:
            for b in list_of_passwords:
              self.type_in_email(a)
              self.type_in_password(b)
              self.click_on_the_sign_in_button()
              self.click_on_the_sign_out_button()
              self.wait_for_visibility_of_element_located(self.sign_in_button_xpath)
              time.sleep(5)
            break

    def check_invalid_data_message(self):
        self.wait_for_visibility_of_element_located(self.FAIlMESSAGE_xpath)
        self.assert_element_text(self.driver,
                                 self.FAIlMESSAGE_xpath,
                                 self.invalid_data_message)

    def check_empty_fields_message(self):
        self.wait_for_visibility_of_element_located(self.FAIlMESSAGE_xpath)
        self.assert_element_text(self.driver,
                                 self.FAIlMESSAGE_xpath,
                                 self.empty_fields_message)