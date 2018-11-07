import re
from random import randrange
from model.contact import Contact


def test_random_contact_on_home_page_from_edit_page(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(first_name="rick", last_name="mortiy", address="USA",
                      phone_home="a", phone_mobile="b", phone_work="c",
                      email="123@32.32", email2="123", email3="2"))
    contacts_list = app.contact.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_home_page == merge_phones_like_one_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_home_page == merge_emails_like_one_home_page(contact_from_edit_page)



def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_home_page == merge_phones_like_one_home_page(contact_from_edit_page)


def test_phones_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.phone_home == contact_from_edit_page.phone_home
    assert contact_from_view_page.phone_mobile == contact_from_edit_page.phone_mobile
    assert contact_from_view_page.phone_work == contact_from_edit_page.phone_work


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_one_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,[contact.phone_home,
                                                                contact.phone_mobile,contact.phone_work]))))

def merge_emails_like_one_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))

