"""Tests for helpers.py."""

import ckanext.opencity.helpers as helpers


def test_opencity_hello():
    assert helpers.opencity_hello() == "Hello, opencity!"
