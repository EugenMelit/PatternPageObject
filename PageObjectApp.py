from BasePageApp import BasePage
from selenium.webdriver.common.by import By
from selenium. webdriver. common. keys import Keys

class YourStorLocator:
    LOCATOR_FIRST_NAME = (By.CSS_SELECTOR, '#input-firstname')
    LOCATOR_LAST_NAME = (By.CSS_SELECTOR, '#input-lastname')
    LOCATOR_EMAIL = (By.CSS_SELECTOR, '#input-email')
    LOCATOR_TELEFONE = (By.CSS_SELECTOR, '#input-telephone')
    LOCATOR_PASSWORD = (By.CSS_SELECTOR, '#input-password')
    LOCATOR_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#input-confirm')
    LOCATOR_PRIVACY_POLICY = (By.XPATH, '//*[@id="content"]/form/div/div/input[1]')
    LOCATOR_BTN_CONTINUE = (By.CLASS_NAME, 'btn btn-primary')
    LOCATOR_BAR_NAVIGATION = (By.CLASS_NAME, 'breadcrumb')
class SearchHelper(BasePage):
    def fill_fields_and_submit(self):

        first_name = self.find_element(YourStorLocator.LOCATOR_FIRST_NAME)
        first_name.send_keys("Eugen")
        last_name = self.find_element(YourStorLocator.LOCATOR_LAST_NAME)
        last_name.send_keys("Ivanov")
        email = self.find_element(YourStorLocator.LOCATOR_EMAIL)
        email.send_keys("melik@ukr.net")
        telefone = self.find_element(YourStorLocator.LOCATOR_TELEFONE)
        telefone.send_keys('0675903187')
        password = self.find_element(YourStorLocator.LOCATOR_PASSWORD)
        password.send_keys('1234567')
        password_confirm = self.find_element(YourStorLocator.LOCATOR_PASSWORD_CONFIRM)
        password_confirm.send_keys('1234567')
        btn_privacy_policy = self.find_element(YourStorLocator.LOCATOR_PRIVACY_POLICY).click()

        btn_continue = self.find_element(YourStorLocator.LOCATOR_BTN_CONTINUE).click()

    def chek_register_succsess(self):
        all_list = self.find_elements(YourStorLocator.LOCATOR_BAR_NAVIGATION, time=2)
        register_succsess = []
        for i in all_list:
            register_succsess.append(i.text)
        return register_succsess



