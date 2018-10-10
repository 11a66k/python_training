# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="222", header="1111", footer="2222"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))




