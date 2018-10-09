class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def sumbit_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
        self.return_to_page()

    def fiil_form(self, group):
        self.fill_group_form(group)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_header", group.header)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def init_creation(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_firsrt_group()
        wd.find_element_by_name("delete").click()
        self.return_to_page()

    def select_firsrt_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modif_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        #open modification form
        self.select_firsrt_group()
        wd.find_element_by_name("edit").click()
        #fill group form
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        #submit modification
        self.return_to_page()


    def sumbit_modif(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.return_to_page()