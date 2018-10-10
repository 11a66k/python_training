class ContactHelper:
    def __init__(self, app):
        self.app = app


    def fill_form(self, contact):
        self.fill_contact_form(contact)

    def fill_contact_form(self, contact):
        self.change_field_valuee("firstname", contact.first_name)
        self.change_field_valuee("lastname", contact.last_name)
        self.change_field_valuee("address", contact.address)
        self.change_field_valuee("home", contact.phone_home)
        self.change_field_valuee("email", contact.email)


    def change_field_valuee(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()


    def modif_first_first_name(self, new_contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()




    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")


