from model.contact import Contact



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
        self.open_home_page()
        self.contact_cache = None


    def delete_first(self):
        self.delete_by_index(0)



    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        # self.open_home_page()
        self.contact_cache = None




    def modif_first_first_name(self, new_contact):
        self.modif_contact_by_index(0)



    def modif_contact_by_index(self, index, new_contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        # self.open_home_page()
        self.contact_cache = None




    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("Last name")) > 0):
            wd.get("http://localhost/addressbook/index.php")

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cell_list = element.find_elements_by_tag_name("td")
                last_name = cell_list[1].text
                first_name = cell_list[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(last_name=last_name, first_name=first_name, id=id))
        return list(self.contact_cache)


