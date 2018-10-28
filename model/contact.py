class Contact:

    def __init__(self, first_name=None, last_name=None, address=None, phone_home=None, email=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_home = phone_home
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.last_name)

    def __eq__(self, other):
        return self.id == other.id and self.last_name == other.last_name