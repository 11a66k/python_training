from sys import maxsize


class Contact:

    def __init__(self, first_name=None, last_name=None, address=None, phone_home=None, phone_mobile=None, phone_work=None, phone_secondary=None, email=None, id=None, all_phones_home_page=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.phone_secondary = phone_secondary
        self.email = email
        self.all_phones_home_page = all_phones_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
