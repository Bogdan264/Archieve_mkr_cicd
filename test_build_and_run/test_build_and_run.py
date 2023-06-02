
import pytest
import BookStoreApp.views as views
import BookStoreApp.models as models


def test_check_book():
    assert views.check_book("Ромео і Джульєта") == True


def test_check_category():
    assert views.check_category("Детектив") == True