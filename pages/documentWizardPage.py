from selenium.webdriver.support.ui import Select

class documentWizardPage():

    def __init__(self, driver):
        self.driver = driver
        self.property_button_xpath = "//*[@id=\"cdk-step-content-0-0\"]/form/div/div[1]/div/mat-icon"
        self.decrease_button_xpath = "//*[@id=\"cdk-step-content-0-0\"]/form/div/div[2]/div/mat-icon"
        self.applicant_name_field_id = "mat-input-0"
        self.commitment_field_id = "mat-input-1"
        self.give_money_field_id = "mat-input-2"
        self.submit_button_xpath = "//*[@id=\"cdk-step-content-0-1\"]/form/div/button[2]"
        self.submit_button_class = "mat-stepper-next"
        self.back_button_xpath = "//*[@id=\"cdk-step-content-0-1\"]/form/div/button[1]"
        self.defendant_name_field_id = "mat-input-3"
        self.done_wrong_field_id = "mat-input-4"
        self.additional_field_id = "mat-input-5"
        self.download_button_xpath = "//*[@id=\"cdk-step-content-0-3\"]/div[1]/div/button"
        self.from_beginning_button_xpath = "//*[@id=\"cdk-step-content-0-3\"]/div[2]/button[2]"

    def property_button_click(self):
        self.driver.find_element_by_xpath(self.property_button_xpath).click()

    def enter_applicant_name(self, name):
        self.driver.find_element_by_id(self.applicant_name_field_id).clear()
        self.driver.find_element_by_id(self.applicant_name_field_id).send_keys(name)

    def enter_commitment(self, commitment):
        self.driver.find_element_by_id(self.commitment_field_id).clear()
        self.driver.find_element_by_id(self.commitment_field_id).send_keys(commitment)

    def fill_give_money_field(self, amount):
        self.driver.find_element_by_id(self.give_money_field_id).clear()
        self.driver.find_element_by_id(self.give_money_field_id).send_keys(amount)

    def submit_button_click(self):
        self.driver.execute_script("button = document.evaluate('//*[@id=\"cdk-step-content-0-1\"]/form/div/button[2]',document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;button.click();")

    def enter_defendant_name(self, name):
        self.driver.find_element_by_id(self.defendant_name_field_id).clear()
        self.driver.find_element_by_id(self.defendant_name_field_id).send_keys(name)

    def enter_done_wrong_field(self, what_wrong):
        self.driver.find_element_by_id(self.done_wrong_field_id).clear()
        self.driver.find_element_by_id(self.done_wrong_field_id).send_keys(what_wrong)

    def choose_additional_info(self, additional_info):
        Select(self.driver.find_element_by_id(self.additional_field_id)).select_by_visible_text(additional_info)

    def download_button_click(self):
        self.driver.find_element_by_xpath(self.download_button_xpath).click()