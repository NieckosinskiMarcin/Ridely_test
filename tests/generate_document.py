from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time as _time
import unittest
from pages.documentWizardPage import documentWizardPage
import os as _os
from pathlib import Path

class GenerateDocument(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("drivers/chromedriver.exe")

    def test_generate_document(self):
        driver = self.driver
        driver.get("https://test-ask.ztable.se/doc-wizard")
        self.applicant_name = "Marian"
        self.commitment = "przestrzeganie zasad"
        self.money = "300"
        self.defendant_name = "Antek"
        self.additional_info = "Wyłącz netflixa"
        self.done_wrong = "ukradł jabłka"

        documentWizard = documentWizardPage(driver)
        documentWizard.property_button_click()
        documentWizard.enter_applicant_name(self.applicant_name)
        documentWizard.enter_commitment(self.commitment)
        documentWizard.fill_give_money_field(self.money)
        documentWizard.submit_button_click()
        documentWizard.enter_defendant_name(self.defendant_name)
        documentWizard.choose_additional_info(self.additional_info)
        documentWizard.enter_done_wrong_field(self.done_wrong)
        documentWizard.submit_button_click()
        documentWizard.download_button_click()

    @classmethod
    def tearDownClass(cls):
        _time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()