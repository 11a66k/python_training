class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def sumbit_creation(self, ):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
        self.return_to_page()

    def fiil_form(self, group):
        # fill group form
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def init_creation(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()