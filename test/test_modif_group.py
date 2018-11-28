
from model.group import Group
import random



def test_modif_group_name(app, db, chech_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(name="nee")
    group.id = random_group.id
    app.group.modif_group_by_id(random_group.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if chech_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



