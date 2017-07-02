from nose.tools import *
from ex47.game import Room


def test_init():
    r = Room("Sattar", "Sattar is noob")

    assert_equal(r.name, "Sattar")
    assert_equal(r.description, "Sattar is noob")
    assert_equal(r.paths, {})


def test_go_when_path_is_not_present():
    r = Room("Sattar", "Sattar is noob")
    assert_equal(r.go(1), None)


def test_go_when_path_is_present():
    r = Room("Sattar", "Sattar is noob")
    r.paths.update({'satt': 'Sattar'})
    assert_equal(r.go('satt'), "Sattar")


def test_add_paths():
    r = Room("Sattar", "Sattar is noob")
    r.add_paths({'satt': 'Sattar'})
    assert_equal(r.paths.get('satt'), "Sattar")
