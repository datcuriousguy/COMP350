import pytest
from pyls import checkFileNames, list_files


def test_checkFileNames():
    files = list_files()
    assert '/' and '*' in files


def test_list_files():
    assert '.py' in list_files()
