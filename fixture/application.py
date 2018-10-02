from selenium import webdriver
from fixture.session import SessionHelper


class Applicaion:


    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)




    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def sumbit_group_creation(self,):
        wd = self.wd
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()


    def fiil_group_form(self, group):
        # fill group form
        wd = self.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def init_group_creation(self):
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()



    def open_home_page(self ):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")




    def submin_form(self):
        wb = self.wd
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, contact):
        wb = self.wd
        wb.find_element_by_name("firstname").click()
        wb.find_element_by_name("firstname").clear()
        wb.find_element_by_name("firstname").send_keys(contact.first_name)
        wb.find_element_by_name("lastname").click()
        wb.find_element_by_name("lastname").clear()
        wb.find_element_by_name("lastname").send_keys(contact.last_name)
        wb.find_element_by_name("address").click()
        wb.find_element_by_name("address").clear()
        wb.find_element_by_name("address").send_keys(contact.address)
        wb.find_element_by_name("home").click()
        wb.find_element_by_name("home").clear()
        wb.find_element_by_name("home").send_keys(contact.phone_home)
        wb.find_element_by_name("email").click()
        wb.find_element_by_name("email").clear()
        wb.find_element_by_name("email").send_keys(contact.email)

    def create_new_contact(self):
        wb = self.wd
        wb.find_element_by_link_text("add new").click()





    def destroy(self):
        self.wd.quit()
