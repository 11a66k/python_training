class ContactHelper:
    def __init__(self, app):
        self.app = app


    def submin_form(self):
        wb = self.app.wd
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_form(self, contact):
        wb = self.app.wd
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

    def create_new(self):
        wb = self.app.wd
        wb.find_element_by_link_text("add new").click()