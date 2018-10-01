# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_untitled_test_case(self):
        wb = self.wd
        self.open_page(wb)
        self.login(wb)
        self.create_new_contact(wb)
        self.fill_contact_form(wb)
        self.submin_form(wb)
        self.logout(wb)

    def logout(self, wb):
        wb.find_element_by_link_text("Logout").click()

    def submin_form(self, wb):
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, wb):
        wb.find_element_by_name("firstname").click()
        wb.find_element_by_name("firstname").clear()
        wb.find_element_by_name("firstname").send_keys("rick")
        wb.find_element_by_name("lastname").click()
        wb.find_element_by_name("lastname").clear()
        wb.find_element_by_name("lastname").send_keys("mortiy")
        wb.find_element_by_name("address").click()
        wb.find_element_by_name("address").clear()
        wb.find_element_by_name("address").send_keys("USA")
        wb.find_element_by_name("home").click()
        wb.find_element_by_name("home").clear()
        wb.find_element_by_name("home").send_keys("+1000000")
        wb.find_element_by_name("email").click()
        wb.find_element_by_name("email").clear()
        wb.find_element_by_name("email").send_keys("123@32.32")

    def create_new_contact(self, wb):
        wb.find_element_by_link_text("add new").click()

    def login(self, wb):
        wb.find_element_by_name("user").send_keys("admin")
        wb.find_element_by_xpath("//form[@id='LoginForm']/label[2]").click()
        wb.find_element_by_name("pass").click()
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys("secret")
        wb.find_element_by_xpath("//input[@value='Login']").click()

    def open_page(self, wb):
        wb.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
